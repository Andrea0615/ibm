//----------------------------------------------------------
// ACCIÓN PRINCIPAL: Proyecto Aurelion
// Objetivo: Generar un resumen de ventas (diario, mensual o total),
//            con detalle de medios de pago y productos más vendidos.
//----------------------------------------------------------
Accion Proyecto Aurelion ES

Ambiente
   // Registro principal de las ventas realizadas
   Ventas = registro
      id_venta: N(3)                          // Identificador numérico de la venta
      fecha = registro                        // Subregistro para almacenar la fecha
         año: N(4)
         mes: N(2)
         dia: N(2)
      Fin registro
      nombre_cliente: AN(50)                  // Nombre completo del cliente
      mail: AN(30)                            // Correo del cliente
      medio_pago: AN("tarjeta", "qr", "transferencia", "efectivo") // Forma de pago usada
   Fin registro
   arch_ventas: archivo de Ventas ordenado por id_venta   // Archivo maestro de ventas
   reg_v: Ventas                                          // Variable registro para leer una venta

   // Registro con el detalle de cada producto vendido por venta
   Detalle_ventas = registro
      id_venta: N(3)                         // Relación con la venta
      id_producto: N(2)                      // Código del producto
      nombre_producto: AN(30)                // Nombre del producto
      cantidad: N(1)                         // Cantidad vendida
      precio_unitario: N(4)                  // Precio por unidad
      importe: N(5)                          // Importe total (precio * cantidad)
   Fin registro
   arch_detalle: archivo de Detalle_ventas ordenado por id_venta  // Archivo detalle
   reg_d: Detalle_ventas                                        // Variable registro para detalle

   // Registro maestro de productos
   Productos = registro
      id_producto: N(3)
      nombre_producto: AN(30)
      categoria: AN(20)
      precio_unitario: N(4)
   Fin registro
   arch_productos: archivo de Productos ordenado por id_producto   // Archivo maestro de productos
   reg_p: Productos                                                // Variable para leer productos

   // Registro auxiliar para acumular ventas por producto
   Producto_acum = registro
      nombre: AN(30)
      cantidad: N(4)
      importe: real
   Fin registro
   aux: Producto_acum                         // Variable auxiliar para intercambio (ordenamiento)

   // Arreglo de 100 posiciones para acumular los productos vendidos
   productos: arreglo[1..100] de Producto_acum

   // Variables de control y acumuladores
   i, j: entero
   plazo: AN("diarias", "mensuales", "total") // Tipo de resumen que se desea generar
   mes: N(2)
   dia: N(2)
   pago: AN("tarjeta", "qr", "transferencia", "efectivo")

   // Totales generales y por medios de pago
   tot_diario: real
   tot_mensual: real
   tot_total: real
   tot_qr: real
   tot_tarjeta: real
   tot_efectivo: real
   tot_transferencia: real
Proceso 

   // Apertura de archivos en modo lectura
   Abrir E/(arch_ventas)
   Abrir E/(arch_detalle)
   Abrir E/(arch_productos)
   Leer(arch_ventas, reg_v)
   Leer(arch_detalle, reg_d)

   // Solicitar al usuario qué tipo de resumen desea
   Esc("Ingrese que plazo de resumen de ventas que quiere conocer: diarias/mensuales/total")
   Leer(plazo)

   // Inicialización de acumuladores
   tot_diario := 0
   tot_mensual := 0
   tot_total := 0
   tot_qr := 0
   tot_tarjeta := 0
   tot_efectivo := 0
   tot_transferencia := 0
   mes := " "
   dia := " "
   pago := " "

   // Inicializa el arreglo de productos con datos del archivo de productos
   Para i := 1 hasta 100 hacer
      Leer(arch_productos, reg_p)
      productos[i].nombre := reg_p.nombre_producto
      productos[i].cantidad := 0
      productos[i].importe := 0
   Fin para

   //---------------------------------------------------------
   // CASO 1: RESUMEN DIARIO
   //---------------------------------------------------------
   Si plazo = "diarias" entonces
      Esc("Ingrese el mes (01-12)")
      Leer(mes)
      Esc("Ingrese día (01-31)")
      Leer(dia)

      Mientras NFDA(arch_ventas) hacer    // Recorre todas las ventas
         Si reg_v.fecha.mes = mes y reg_v.fecha.dia = dia Entonces 
            pago := reg_v.medio_pago      // Guarda el tipo de pago de esa venta

            // Relaciona ventas con detalle de productos vendidos
            Si reg_v.id_venta = reg_d.id_venta Entonces
               Mientras reg_v.id_venta = reg_d.id_venta Hacer
                  tot_diario := tot_diario + reg_d.importe    // Acumula el total diario

                  // Acumula por medio de pago
                  segun pago hacer
                     = tarjeta: tot_tarjeta := tot_tarjeta + reg_d.importe
                     = efectivo: tot_efectivo := tot_efectivo + reg_d.importe
                     = qr: tot_qr := tot_qr + reg_d.importe
                     = transferencia: tot_transferencia := tot_transferencia + reg_d.importe
                  fin segun

                  // Busca el producto dentro del arreglo y acumula cantidad e importe
                  Para i := 1 hasta 100 hacer
                     Si productos[i].nombre = reg_d.nombre_producto Entonces
                        productos[i].cantidad := productos[i].cantidad + reg_d.cantidad
                        productos[i].importe := productos[i].importe + reg_d.importe
                     Fin si
                  Fin para
                  Leer(arch_detalle, reg_d)
               Fin mientras
            Fin si
            Leer(arch_ventas, reg_v)
         Sino
            Esc("El dia y el mes ingresado no se realizo ninguna venta")
         Fin si
      Fin Mientras

   //---------------------------------------------------------
   // CASO 2: RESUMEN MENSUAL
   //---------------------------------------------------------
   Sino
      Si plazo = "mensuales" Entonces
         Esc("Ingrese el mes (01-12)")
         Leer(mes)
         Mientras NFDA(arch_ventas) Hacer
            Si reg_v.fecha.mes = mes Entonces
               pago := reg_v.medio_pago
               Si reg_v.id_venta = reg_d.id_venta Entonces
                  Mientras reg_v.id_venta = reg_d.id_venta Hacer
                     tot_mensual := tot_mensual + reg_d.importe
                     segun pago hacer
                        = tarjeta: tot_tarjeta := tot_tarjeta + reg_d.importe
                        = efectivo: tot_efectivo := tot_efectivo + reg_d.importe
                        = qr: tot_qr := tot_qr + reg_d.importe
                        = transferencia: tot_transferencia := tot_transferencia + reg_d.importe
                     fin segun

                     Para i := 1 hasta 100 hacer
                        Si productos[i].nombre = reg_d.nombre_producto Entonces
                           productos[i].cantidad := productos[i].cantidad + reg_d.cantidad
                           productos[i].importe := productos[i].importe + reg_d.importe
                        Fin si
                     Fin para
                     Leer(arch_detalle, reg_d)
                  Fin mientras
               Fin si
               Leer(arch_ventas, reg_v)
            Sino
               Esc("El mes ingresado no se realizo ninguna venta")
            Fin si
         Fin Mientras

   //---------------------------------------------------------
   // CASO 3: RESUMEN TOTAL (todas las ventas)
   //---------------------------------------------------------
      Sino
         Si plazo = "total" Entonces
            Mientras NFDA(arch_ventas) Hacer
               pago := reg_v.medio_pago
               Mientras NFDA(arch_detalle) Hacer
                  tot_total := tot_total + reg_d.importe
                  segun pago hacer
                     = tarjeta: tot_tarjeta := tot_tarjeta + reg_d.importe
                     = efectivo: tot_efectivo := tot_efectivo + reg_d.importe
                     = qr: tot_qr := tot_qr + reg_d.importe
                     = transferencia: tot_transferencia := tot_transferencia + reg_d.importe
                  fin segun

                  Para i := 1 hasta 100 hacer
                     Si productos[i].nombre = reg_d.nombre_producto Entonces
                        productos[i].cantidad := productos[i].cantidad + reg_d.cantidad
                        productos[i].importe := productos[i].importe + reg_d.importe
                     Fin si
                  Fin para
                  Leer(arch_detalle, reg_d)
               Fin Mientras
               Leer(arch_ventas, reg_v)
            Fin Mientras
         Sino
            Esc("Valor no valido")    // En caso de ingreso incorrecto
         Fin si
      Fin si
   Fin si

   //---------------------------------------------------------
   // ORDENAR PRODUCTOS POR IMPORTE DE VENTA (DESCENDENTE)
   //---------------------------------------------------------
   Para i := 1 hasta 99 Hacer
      Para j := i+1 hasta N Hacer       // Comparación de cada producto con los siguientes
         Si productos[j].importe > productos[i].importe Entonces
            aux := productos[i]         // Intercambia posiciones si el siguiente tiene más ventas
            productos[i] := productos[j]
            productos[j] := aux
         Fin si
      Fin Para
   Fin Para

   //---------------------------------------------------------
   // MOSTRAR RESULTADOS EN PANTALLA
   //---------------------------------------------------------
   Esc("......... RESUMEN DE VENTAS .........")
   Esc(" ")

   Segun plazo hacer
      = diario: Esc("El importe de las ventas en el mes", mes, "y dia", dia, "es de un total de:", tot_diario)
      = mensual: Esc("El importe de las ventas en el mes", mes,"es de un total de:", tot_mensual)
      = total: Esc("El importe total de ventas es de:", tot_total)
   fin segun

   Esc("--------------------------------------------")
   Esc("IMPORTE TOTAL POR MEDIO DE PAGO")
   Esc("  Tarjeta = $", tot_tarjeta)
   Esc("  Efectivo = $", tot_efectivo)
   Esc("  QR = $", tot_qr)
   Esc("  Transferencia = $", tot_transferencia)
   Esc("--------------------------------------------")
   Esc("LISTA DE PRODUCTOS MAS VENDIDOS DE FORMA DESCENDENTE") 
   Esc("PRODUCTO   CANTIDAD   IMPORTE")

   // Muestra solo los productos con ventas
   Para i := 1 hasta 100 Hacer
      Si productos[i].importe > 0 Entonces
         Esc(productos[i].nombre, "     ", productos[i].cantidad, "     ", productos[i].importe)
      Fin si
   Fin Para

   // Cierre de archivos
   Cerrar(arch_ventas)
   Cerrar(arch_detalle)
   Cerrar(arch_productos)

Fin Accion
