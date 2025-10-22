# Archivo de documentación
# Se asigna la ruta del archivo .md que contiene la documentación
archivo_md = r"Documentación.md"


# Función para preguntar si el usuario desea volver al menú
def volver_menu(respuesta):
    if respuesta == "si":
        return True
    elif respuesta == "no":
        return False
    else:
        print("Respuesta no válida. Por favor, ingresa si o no")
        return None
   
# Función para leer una sección del archivo por número
import re


def leer_seccion(archivo, seccion_num):
    contenido = []
    en_seccion = False
    inicio = f"{seccion_num}."


    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            # Detecta inicio de sección
            if linea.startswith(inicio) and not en_seccion:
                en_seccion = True
                continue
            # Detecta otro encabezado de sección diferente
            elif en_seccion and re.match(r"^\d+\.", linea):
                break
            elif en_seccion:
                contenido.append(linea)


    return "\n".join(contenido) if contenido else "Sección vacía o no encontrada."


# Menú interactivo principal
while True:
    eleccion = input(
        "Bienvenido al Proyecto Aurelion del Grupo 7. A continuación elija una de las opciones: \n"
        "1. Tema \n"
        "2. Problemática\n"
        "3. Solución\n"
        "4. Fuentes de Datos\n"
        "5. Estructura Base de Datos\n"
        "6. Información Programa y Pasos\n"
        "7. Pseudocódigo del menú \n"
        "8. Diagrama del menú\n"
        "9. Sugerencias de Copilot del menú\n"
        "10. Pseudocódigo de Solución\n"
        "11. Diagrama de Solución\n"
        "12. Sugerencias de Copilot de Solución\n"
        "13. Salir\n"
    )


    if eleccion == "1":
        print("Tema.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "2":
        print("Problemática.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "3":
        print("Solución.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "4":
        print("Fuentes de Datos.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "5":
        print("Estructura Base de Datos.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "6":
        print("Información Programa y Pasos.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "7":
        print("Para consultar el pseudocódigo del menú a ruta es la siguiente.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "8":
        print("Para consultar el diagrama del menú la ruta es la siguiente.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "9":
        print("Sugerencias de Copilot del menú.")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue




    elif eleccion == "10":
        print("Pseudocódigo de Solución")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue




    elif eleccion == "11":
        print("Diagrama de Solución")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue


    elif eleccion == "12":
        print("Sugerencias de Copilot de Solución")
        print(leer_seccion(archivo_md, int(eleccion)))
        respuesta = input("¿Deseas volver al menú principal? (si/no): ")
        if volver_menu(respuesta) is False:
            print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
            break
        elif volver_menu(respuesta) is None:
            continue




    elif eleccion == "13":
        print("Proceso finalizado. ¡Tus reportes de ventas te esperan la próxima vez!")
        break


    else:
        print("Opción no válida, por favor elige una opción del 1 al 13")


# Fin del programa
