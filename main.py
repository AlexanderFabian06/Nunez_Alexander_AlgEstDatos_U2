'''Tarea 2
Programa para gestionar una biblioteca de libros utilizando una tabla hash simple 
con manejo de colisiones mediante encadenamiento.'''

'''Objetivo del programa:
Desarrollar un programa en Python de consola sencillo que gestione el catálogo y los préstamos de
una pequeña biblioteca usando estructuras de la Unidad 2: Diccionarios y conjuntos.'''

import utilidades as util

# Estructura general con el que funcionará el programa, se utilizará una tabla hash simple para almacenar los libros y sus detalles.

catalogo: dict = {}     # R1/R2: código {(título, autor)}

socios: set = set()     # R3: identificador de socios

prestamos_novela: set = set()       #R4: socios que han pedido prestado novelas

prestamos_ciencia: set = set()      # R4: socios que han pedido prestado libros de ciencia

Menu = '''
==== BILIOTECA ====
    1: "Agregar libro",
    2: "Buscar libro",
    3: "Ordenar el catálogo de libros",
    4: "Agregar socio",
    5: "Validar socio",
    6: "Registrar préstamo de libro",
    7: "Analizar préstamos de libros",
    8: "Salir",
'''

def registrar_libro ():
    '''Función para registrar un libro en el catálogo de la biblioteca.'''
    codigo = input("Ingrese el código del libro: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    if util.registrar_libro(catalogo, codigo, titulo, autor):
        print(f"Libro '{titulo}' registrado exitosamente.")
    else:
        print(f"Error: El libro con código '{codigo}' ya existe en el catálogo.")

def buscar_libro():
    '''Función para buscar un libro en el catálogo de la biblioteca.'''
    codigo = input("Ingrese el código del libro a buscar: ")
    libro = util.buscar_libro(catalogo, codigo)
    if libro:
        print(f"Libro encontrado: Código: {codigo}, Título: {libro[0]}, Autor: {libro[1]}")
    else:
        print(f"Error: No se encontró un libro con código '{codigo}'.")

def ordenar_catalogo():
    '''Función para ordenar el catálogo de libros por título.'''
    catalogo_ordenado = util.ordenar_catalogo(catalogo)
    print("Catálogo de libros ordenado por título:")
    for codigo, (titulo, autor) in catalogo_ordenado:
        print(f"Código: {codigo}, Título: {titulo}, Autor: {autor}")

def agregar_socio():
    '''Función para agregar un socio a la biblioteca.'''
    identificador = input("Ingrese el identificador del socio: ")
    if util.agregar_socio(socios, identificador):
        print(f"Socio con identificador '{identificador}' agregado exitosamente.")
    else:
        print(f"Error: El socio con identificador '{identificador}' ya existe.")

def validar_socio():
    '''Función para validar si un socio está registrado en la biblioteca.'''
    identificador = input("Ingrese el identificador del socio a validar: ")
    if util.validar_socio(socios, identificador):
        print(f"El socio con identificador '{identificador}' está registrado.")
    else:
        print(f"Error: El socio con identificador '{identificador}' no está registrado.")

def registrar_prestamo():
    '''Función para registrar un préstamo de libro a un socio.'''
    identificador = input("Ingrese el identificador del socio: ")
    if not util.validar_socio(socios, identificador):
        print(f"Error: El socio con identificador '{identificador}' no está registrado.")
        return

    codigo = input("Ingrese el código del libro a prestar: ")
    libro = util.buscar_libro(catalogo, codigo)
    if not libro:
        print(f"Error: No se encontró un libro con código '{codigo}'.")
        return

    tipo_libro = input("Ingrese el tipo de libro (novela/ciencia): ").strip().lower()
    if tipo_libro == "novela":
        prestamos_novela.add(identificador)
        print(f"Préstamo registrado: Socio '{identificador}' ha pedido prestado la novela '{libro[0]}'.")
    elif tipo_libro == "ciencia":
        prestamos_ciencia.add(identificador)
        print(f"Préstamo registrado: Socio '{identificador}' ha pedido prestado el libro de ciencia '{libro[0]}'.")
    else:
        print("Error: Tipo de libro no válido. Debe ser 'novela' o 'ciencia'.")

def analizar_prestamos():
    '''Función para analizar los préstamos de libros y mostrar estadísticas.'''
    total_novelas = len(prestamos_novela)
    total_ciencia = len(prestamos_ciencia)
    total_socios = len(socios)

    print(f"Total de socios registrados: {total_socios}")
    print(f"Total de socios que han pedido prestado novelas: {total_novelas}")
    print(f"Total de socios que han pedido prestado libros de ciencia: {total_ciencia}")

ACCIONES = { # Despacho por diccionario: acceso por clave
    "1": registrar_libro,
    "2": buscar_libro,
    "3": ordenar_catalogo,
    "4": agregar_socio,
    "5": validar_socio,
    "6": registrar_prestamo,
    "7": analizar_prestamos,
    "8": exit
}

def main():
    '''Función principal del programa que muestra el menú y gestiona las acciones del usuario.'''
    util.cargar_datos_ejempplo(catalogo, socios, prestamos_novela, prestamos_ciencia)
    while True:
        print(Menu)
        opcion = input("Seleccione una opción: ").strip()
        accion = ACCIONES.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

if __name__ == "__main__":
    main()
