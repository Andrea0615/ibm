1. Tema.
 Retail - Análisis del Flujo de Efectivo de tiendas para el pago a proveedores

2. Problemática. 
 Para la gran mayoría de tiendas, el flujo de caja de chica diaria resulta de gran importancia  para el sostenimiento de sus negocios. Estas tiendas al subsistir de transacciones minoristas, consecuentemente, no cuentan con una base fija de ingresos diariamente. Esto posiciona a las mismas en una situación económicamente vulnerable  ante las volatilidades que puedan existir en el ejercicio de la compra-venta. Si los tenderos no disponen de la liquidez suficiente al momento que los proveedores los visitan, estos no podrían continuar con el abastecimiento de nuevas mercaderías para el negocio.

3. Solución. 
 Desarrollar un sistema en Python que permita registrar las entradas a la caja chica (efectivo, transferencias, qr), calcular automáticamente el saldo disponible y generar reportes que faciliten la previsión de pagos a proveedores. De esta manera, los tenderos podrán anticipar faltantes de efectivo, tomar decisiones financieras más informadas y asegurar la continuidad del abastecimiento de mercaderías para su negocio.

4. Fuentes de Datos.
  Hay una sola base de datos conformada por 4 entidades en formato CSV de la tienda Aurelion:
   Tabla de Clientes: ruta(Base_de_datos/clientes.csv)
   Tabla de Detalles de Venta: ruta(Base_de_datos/detalle_ventas.csv)
   Tabla de Productos: ruta(Base_de_datos/productos.csv)
   Tabla de Ventas: ruta(Base_de_datos/ventas.csv)
  
5. Estructura Base de Datos.
  **Definicion**
    Cada entidad de la base de datos contiene registros organizados en filas y columnas:
     Cliente: Cada registro representa un cliente, con su ID, nombre, correo electrónico, ciudad y fecha de alta.
     Detalle_ventas: Cada registro representa un producto vendido en una venta específica, con cantidad, precio unitario e importe total.
     Productos: Cada registro corresponde a un producto disponible, indicando su ID, nombre, categoría y precio unitario.
     Venta: Cada registro representa una venta realizada, incluyendo fecha, nombre y correo del cliente, y el medio de pago utilizado. 
  **Relación**
    Los datos permiten relacionar clientes, ventas y productos para análisis de transacciones y comportamiento de ventas.
  **Estructura, tipos y escala**
    Tabla: cliente con una cantidad de registros de 100 clientes. 
      id_cliente: Entero(3)
      Nombre_cliente: Alfanumérico(50)
      mail: Alfanumérico(30)
      ciudad: Alfanumérico(30)
      fecha_alta = registro
         año: Entero(4)
         mes: Entero(2)
         dia: Entero(2)
      Fin registro
    Fin tabla

    Tabla: Detalle_ventas con una cantidad de registros de 341 detalles de ventas.
     id_venta: Entero(3)
     id_producto: Entero(2)
     nombre de producto: Entero(30)
     cantidad: Entero(1)
     precio_unitario: Entero(4)
     importe: Entero(5)
    Fin tabla

    Tabla: Productos con una cantidad de registros de 100 productos.
     id_producto: Entero(3)
     nombre_producto: Alfanumérico(30)
     categoria: Alfanumérico(20)
     precio_unitario: Entero(4)
    Fin tabla

    Tabla: Ventas con una cantidad de registros de 120 ventas.
     id_venta: Entero(3)
     fecha = registro
        año: Entero(4)
        mes: Entero(2)
        dia: Entero(2)
     fin registro
     nombre_cliente: Alfanumérico(50)
     mail: Alfanumérico(30)
     medio_pago: Alfanumérico(“tarjeta”, “qr”, “transferencia”)
    Fin registro

6. Información Programa y Pasos.
   **Información**
   Nombre del programa:
     Menú de Documentación del Proyecto Aurelion
   Objetivo principal:
     - Permitir al usuario consultar de forma interactiva las distintas secciones de un archivo de documentación en formato Markdown (.md).
     - El sistema despliega un menú con opciones numeradas, y según la elección del usuario, muestra el contenido correspondiente leído directamente desde el archivo.
   Entradas:
     - Elección: opción del menú seleccionada por el usuario.
     - Respuesta: confirmación del usuario para volver o salir.
     - archivo_md: archivo Markdown con la documentación.
   Salidas:
     - Contenido textual de la sección elegida.
     - Mensajes informativos, de error o finalización.
   Archivos utilizados:
     - Documentación.md: contiene las secciones numeradas con los contenidos del proyecto.
   Variables principales:
     - Archivo_md AN(100): Ruta o nombre del archivo de documentación.
     - Eleccion	AN(2):	Opción seleccionada del menú.
     - Respuesta	AN(2):	Indica si el usuario desea volver o salir.
     - Contenido	AN(1000):	Texto leído de la sección solicitada.
     - Seccion_num	N(2):	Número de la sección a consultar.
   Funciones Auxiliares:
     - volver_menu(respuesta):
        Evalúa si el usuario desea regresar al menú principal.
        Devuelve Verdadero si la respuesta es "si".
        Devuelve Falso si la respuesta es "no".
        Devuelve Nulo si la respuesta no es válida (mensaje de error mostrado).
     - leer_seccion(archivo, seccion_num):
        Lee el contenido de una sección específica del archivo .md.
        Abre el archivo indicado.
        Busca la línea que comience con el número de la sección (por ejemplo 3.).
        Acumula las líneas hasta detectar una nueva sección.
        Devuelve el texto leído o un mensaje de error si no encuentra contenido.
    **Pasos** 
    Inicialización:
     - Se asigna a archivo_md el nombre "Documentación.md".
     Mostrar menú:
     - Se despliega una lista numerada del 1 al 13, con las secciones disponibles:
      1-Tema
      2-Problemática
      3-Solución
      4-Fuentes de Datos
      5-Estructura Base de Datos
      6-Información Programa y Pasos
      7-Pseudocódigo del menú
      8-Diagrama del menú
      9-Sugerencias de Copilot del menú
      10-Pseudocódigo de Solución
      11-Diagrama de Solución
      12-Sugerencias de Copilot de Solución
      13-Salir
    Leer elección:
     - El usuario ingresa la opción deseada.
    Evaluar opción:
     - Si la opción es válida (1–12), se convierte a número y se llama a leer_seccion para mostrar el contenido.
     - Si la opción es "13", se muestra un mensaje de salida y termina el proceso.
     - Si la opción es inválida, se solicita nuevamente una elección correcta.
    Mostrar contenido:
     - Se imprime el texto leído de la sección correspondiente.
    Volver al menú o salir:
     - Se pregunta: “¿Deseas volver al menú principal? (si/no)”
     - Si el usuario responde "si", se repite el menú.
     - Si responde "no", se muestra el mensaje de finalización.
     - Si la respuesta no es válida, se muestra un aviso y se vuelve a preguntar.
    Finalización:
     - El programa termina cuando el usuario elige "13" o responde "no" al volver al menú.
   
7. Pseudocódigo del menú.
    Pseudocódigo: ruta(Pseudocódigo/Pseudocódigo_Menú.md)
   
8. Diagrama del menú.
    Diagrama de flujo: ruta(Diagrama/Diagrama_Menú.jpeg)

9. Sugerencias de Copilot del Menú.
  - Se inicia el proyecto preguntandole a Copilot como conectar Git con Visual Studio con el fin de desarrollar un repositorio virtual en el que todos los participantes pudieran poner cambios en tiempo real en el código, a lo cual nos dio paso por paso como realizar la conexión, finalmente esta idea fue descartada en esta actividad pero será retomada por el grupo mas adelante.
  - Con una idea clara del proyecto que queríamos desarrollar se le pregunta a Copilot como estructurar la documentación en la cual nos basamos para el desarrollo del proyecto, dicha documentación son los 10 ítems desarrollados en el código. 
  - Teníamos pensado que el código arrojará la información referente a: según el dinero recaudado por una tienda si o no alcanzaba para pagar a los proveedores, pero como no contábamos con esos valores en la base de datos, la idea fue descartada. 
  - Le preguntamos como conectar la Documentacion.md al Programa.py, es decir, como conectar el programa main a diferentes secciones de la documentación, paso que seria mas adelante importante al momento de conectar el codigo como las bases de datos. 
  - Sumando a lo anterior se le pregunta cómo acceder a los diferentes ítems en formato lista(uno por uno), lo cual agregado al código.
  - Conforme íbamos avanzando se le fueron preguntando los errores que iba arrojando el programa desarrollado, por ejemplo nos indicaba que Python no puede encontrar el archivo Documentacion.md en la misma carpeta donde se ejecuta el programa. y nos daba la ruta correcta en el código.
  - Una vez terminado el código preguntamos por errores de sintaxis.

10. Pseudocódigo Solución.
     Pseudocódigo: ruta(Solución/Pseudocódigo_Solución.md)

11. Diagrama Solución.
     Diagrama de flujo: ruta(Solución/Diagrama_Solución.png)

12. Sugerencias de Copilot Solución.
  - Se le pregunta si la base de datos se puede recorrer de inicio a fin como un archivo, esto con el fin de entender cómo trabajar con un archivo csv en python mientras desarrollamos el pseudocódigo, nos indico como poner la ruta de enlace con el tipo de archivo, tanto en pseudocódigo como en el diagrama desarrollado.
  - Al momento de desarrollar el programa, como ya hemos dicho anteriormente, seria desarrollado por ítems o secciones, en un punto del desarrollo, para seleccionar un ítem, nos enviaba a todos y no discriminaba, por lo tanto le mandamos el código para que nos ayudará en el proceso de selección del ítem. 
  - Al momento de desarrollar los totales: por día, mensuales y el total general, le pedimos ayuda con la sintaxis.
  - Le ingresamos el pseudocódigo con el fin de detectar errores en la sintaxis, pero nos nos realizó cambios. 
  - A la hora de hacer el resultado de los productos más vendidos de manera descendente (los que tuvieran más importe) por diario, mensual y total; nos sugirió usar la estructura de arreglos. 
  - Se le preguntó qué tipo de ordenamiento seria el mejor para organizar el arreglo, y nos recomendó el arreglo de burbuja: 
    Para i := 1 hasta N-1 hacer
      Para j := 1 hasta N-i hacer
        Si productos[j].cantidad_vendida < productos[j+1].cantidad_vendida entonces
          aux := productos[j]
          productos[j] := productos[j+1]
          productos[j+1] := aux
        Fin si
      Fin para
    Fin para.
  - Se le preguntó por la estructura de los bucles a lo cual nos reescribió el código, cambiando sintaxis, lo cual no fue tomado, ya que confiábamos en nuestra estructura. 
  - Le preguntamos si debíamos definir el tamaño del arreglo, nos dice que sí, ya que el arreglo es una estructura de tamaño. 
  - Se le preguntó cómo integrar la imagen del diagrama de flujo el pseudocódigo, y el nos establece la ruta 
  - Le pedimos que nos ayudará con los comentarios. 

  *bitacora personal*

  Sesión 1: Al principio fue un poco difícil organizarnos porque éramos personas de diferentes países. Aun así, todos tuvimos buena actitud y logramos hacer una reunión para hablar sobre el tema y cómo podríamos resolverlo. Al inicio nuestro problema era muy amplio, queríamos abarcar muchas cosas, pero con el tiempo entendimos que era mejor enfocarlo solo en el flujo de caja chica diaria y en la necesidad de contar con dinero para pagar a los proveedores. Esto nos ayudó a tener más claro lo que queríamos lograr con el proyecto. Usamos GitHub Copilot para entender mejor las instrucciones y para revisar si lo que íbamos haciendo estaba bien, poco a poco, con prueba y error, conseguimos que el menú interactivo en Python funcionara correctamente.

  Sesión 2: Nos concentramos en completar el documento de la documentación. Lo que más tiempo nos tomó fue hacer el pseudocódigo de la solución. Lo fuimos construyendo paso a paso, explicando cada parte y viendo cómo funcionaba en la consola de Visual Studio.
    Definimos tres tareas principales para el sistema:
        -Calcular el total de ventas (diario, mensual y general).
        -Mostrar el total según el medio de pago.
        -Hacer una lista con los productos más vendidos. 
  Durante esta parte usamos mucho Copilot para resolver dudas. Nos enseñó cómo recorrer los archivos CSV, cómo poner bien las rutas y nos ayudó con la parte del cálculo de totales. También nos recomendó usar arreglos para ordenar los productos más vendidos y nos explicó cómo hacer el ordenamiento de burbuja.
  Algunas sugerencias no las tomamos, como cuando nos reescribió los bucles con otra estructura. Preferimos dejar los nuestros porque ya entendíamos bien cómo funcionaban.

  Sesión 3: En esta sesión hicimos el diagrama de flujo basado en el pseudocódigo de la solución. Esto nos ayudó a entender mejor la lógica del programa y ver todo el proceso paso a paso.También organizamos las carpetas del proyecto para que todos tuviéramos los mismos nombres y rutas, asegurando que el código de Python funcionara correctamente en todas las computadoras.

  Sesión 4: Conectamos el diagrama en formato PNG dentro de Visual Studio y ajustamos algunos detalles del menú en Python para que se viera mejor y fuera más fácil de usar. Agregamos las sugerencias de Copilot que consideramos útiles y dejamos el proyecto listo para la primera entrega. En esta parte ya todo el equipo entendía bien el funcionamiento del programa.

  Sesión 5: Cuando recibimos las observaciones del profesor, nos dimos cuenta de que nos habíamos adelantado un poco. Estábamos trabajando en el pseudocódigo de la solución general cuando todavía teníamos que centrarnos en el pseudocódigo del menú principal. Decidimos guardar la parte avanzada para después y enfocarnos ahora en el pseudocódigo del menú, junto con su diagrama de flujo. También agregamos una opción en el menú para mostrar el pseudocódigo directamente desde el programa y una sección con los nombres del grupo para hacerlo más completo.

  Sesión 6: En esta sesión mejoramos la definición del tema, la problemática y la solución. Cambiamos el enfoque para que no se tratara solo del efectivo, sino del flujo de caja diaria incluyendo todos los medios de pago: efectivo, transferencia, tarjeta y QR. Esto hizo que la idea fuera más realista. Actualizamos el código de Python y creamos un nuevo diagrama de flujo con la estructura del menú interactivo. También agregamos cuántos registros tenía cada tabla de la base de datos para que todo quedara más claro.

  Sesión 7: Por último, desarrollamos el pseudocódigo del menú, que fue la parte central del proyecto. Este pseudocódigo muestra cómo el programa permite al usuario elegir una opción del menú, leer la sección correspondiente del archivo de documentación y decidir si quiere volver al menú o salir. Con Copilot recibimos varias sugerencias. Nos ayudó a conectar el programa con el archivo de documentación, a crear la estructura que permite acceder a cada ítem del menú por número y a corregir errores de ruta cuando el archivo no se encontraba. También revisó la sintaxis general del código. Otras ideas no las usamos, como la integración de Git con Visual Studio o la lógica de calcular si se podía pagar a los proveedores, ya que no teníamos esos datos en la base de datos. Al final dejamos todo listo y ordenado. El proyecto quedó completo, con el pseudocódigo, los diagramas y la documentación final.

  Conclusión Personal: Durante todo el proceso aprendí mucho sobre cómo planear y documentar un proyecto. Me gustó trabajar en equipo porque cada quien aportó ideas diferentes y juntos pudimos resolver los problemas. Copilot fue una buena herramienta para ayudarnos con la programación, aunque también aprendí que no siempre hay que aceptar todo lo que sugiere. Al final logramos un proyecto funcional y bien hecho que muestra el trabajo y el esfuerzo de todos.