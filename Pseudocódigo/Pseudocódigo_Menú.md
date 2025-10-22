

//----------------------------------------------------------
// ACCIÓN PRINCIPAL: Menú de Documentación del Proyecto Aurelion
// Objetivo: Permitir al usuario consultar secciones específicas
//           de un archivo de documentación (.md) de forma interactiva.
//----------------------------------------------------------


Accion Menu_Documentacion_Aurelion ES


Ambiente
    // Variables y archivos principales
    archivo_md: AN(100)              // Ruta del archivo de documentación Markdown
    eleccion: AN(2)                  // Opción seleccionada del menú
    respuesta: AN(2)                 // Respuesta para volver o no al menú
    contenido: AN(1000)              // Contenido leído de la sección solicitada
    seccion_num: N(2)                // Número de la sección a leer


    // Función para validar si el usuario desea volver al menú
    Funcion volver_menu(respuesta: AN(2)) regresa logico
        Si respuesta = "si" Entonces
            volver_menu := Verdadero
        Sino
            Si respuesta = "no" Entonces
                volver_menu := Falso
            Sino
                Esc("Respuesta no válida. Por favor, ingresa si o no")
                volver_menu := Nulo
            FinSi
        FinSi
    FinFuncion


    // Función para leer una sección del archivo Markdown
    Funcion leer_seccion(archivo: AN(100), seccion_num: N(2)) regresa AN(1000)
        Definir contenido: AN(1000)
        Definir en_seccion: logico
        Definir linea: AN(200)
        Definir inicio: AN(10)


        en_seccion := Falso
        inicio := ConvertirATexto(seccion_num) + "."


        Abrir E/(archivo)
        Mientras NFDA(archivo) Hacer
            Leer(archivo, linea)
            linea := QuitarEspacios(linea)


            // Detectar inicio de la sección
            Si IniciaCon(linea, inicio) Y No en_seccion Entonces
                en_seccion := Verdadero
                Continuar
            FinSi


            // Detectar nuevo encabezado (otra sección)
            Si en_seccion Y Coincide(linea, "^[0-9]+.") Entonces
                Romper
            FinSi


            // Acumular líneas del contenido
            Si en_seccion Entonces
                contenido := contenido + linea + "\n"
            FinSi
        FinMientras
        Cerrar(archivo)


        Si contenido ≠ "" Entonces
            leer_seccion := contenido
        Sino
            leer_seccion := "Sección vacía o no encontrada."
        FinSi
    FinFuncion


Proceso
    // Inicialización del archivo de documentación
    archivo_md := "Documentación.md"


    // Menú interactivo principal
    Mientras Verdadero Hacer
        Esc("Bienvenido al Proyecto Aurelion del Grupo 7.")
        Esc("Seleccione una opción:")
        Esc("1. Tema")
        Esc("2. Problemática")
        Esc("3. Solución")
        Esc("4. Fuentes de Datos")
        Esc("5. Estructura Base de Datos")
        Esc("6. Información Programa y Pasos")
        Esc("7. Pseudocódigo del menú")
        Esc("8. Diagrama del menú")
        Esc("9. Sugerencias de Copilot del menú")
        Esc("10. Pseudocódigo de Solución")
        Esc("11. Diagrama de Solución")
        Esc("12. Sugerencias de Copilot de Solución")
        Esc("13. Salir")


        Leer(eleccion)


        Segun eleccion Hacer
            = "1": Esc("Tema.")
            = "2": Esc("Problemática.")
            = "3": Esc("Solución.")
            = "4": Esc("Fuentes de Datos.")
            = "5": Esc("Estructura Base de Datos.")
            = "6": Esc("Información Programa y Pasos.")
            = "7": Esc("Pseudocódigo del menú.")
            = "8": Esc("Diagrama del menú.")
            = "9": Esc("Sugerencias de Copilot del menú.")
            = "10": Esc("Pseudocódigo de Solución.")
            = "11": Esc("Diagrama de Solución.")
            = "12": Esc("Sugerencias de Copilot de Solución.")
            = "13":
                Esc("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
                Romper
            Otro:
                Esc("Opción no válida, por favor elige una opción del 1 al 13")
                Continuar
        FinSegun


        // Mostrar contenido de la sección elegida (excepto opción 13)
        Si eleccion ≠ "13" Entonces
            seccion_num := ConvertirANumero(eleccion)
            contenido := leer_seccion(archivo_md, seccion_num)
            Esc(contenido)


            Esc("¿Deseas volver al menú principal? (si/no): ")
            Leer(respuesta)


            Si volver_menu(respuesta) = Falso Entonces
                Esc("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
                Romper
            Sino
                Si volver_menu(respuesta) = Nulo Entonces
                    Continuar
                FinSi
            FinSi
        FinSi
    FinMientras


Fin Accion
