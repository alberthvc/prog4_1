import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('slang_panameno.db')
cursor = conn.cursor()

# Crear la tabla para almacenar las palabras
cursor.execute('''
    CREATE TABLE IF NOT EXISTS palabras (
        id INTEGER PRIMARY KEY,
        palabra TEXT UNIQUE,
        significado TEXT
    )
''')

conn.commit()
def agregar_palabra():
    palabra = input("Ingresa la palabra: ")
    significado = input("Ingresa el significado: ")
    
    try:
        cursor.execute("INSERT INTO palabras (palabra, significado) VALUES (?, ?)", (palabra, significado))
        conn.commit()
        print("Palabra agregada exitosamente.")
    except sqlite3.IntegrityError:
        print("La palabra ya existe en el diccionario.")

def editar_palabra():
    palabra = input("Ingresa la palabra a editar: ")
    nuevo_significado = input("Ingresa el nuevo significado: ")
    
    cursor.execute("UPDATE palabras SET significado = ? WHERE palabra = ?", (nuevo_significado, palabra))
    conn.commit()
    print("Significado actualizado.")

def eliminar_palabra():
    palabra = input("Ingresa la palabra a eliminar: ")
    
    cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra,))
    conn.commit()
    print("Palabra eliminada.")

def ver_listado_palabras():
    cursor.execute("SELECT palabra, significado FROM palabras")
    palabras = cursor.fetchall()
    
    for palabra, significado in palabras:
        print(f"{palabra}: {significado}")

def buscar_significado():
    palabra = input("Ingresa la palabra a buscar: ")
    
    cursor.execute("SELECT significado FROM palabras WHERE palabra = ?", (palabra,))
    resultado = cursor.fetchone()
    
    if resultado:
        print(f"Significado: {resultado[0]}")
    else:
        print("La palabra no fue encontrada en el diccionario.")

# Menú principal
while True:
    print("\nMenú:")
    print("a) Agregar nueva palabra")
    print("c) Editar palabra existente")
    print("d) Eliminar palabra existente")
    print("e) Ver listado de palabras")
    print("f) Buscar significado de palabra")
    print("g) Salir")

    opcion = input("Elige una opción: ")

    if opcion == 'a':
        agregar_palabra()
    elif opcion == 'c':
        editar_palabra()
    elif opcion == 'd':
        eliminar_palabra()
    elif opcion == 'e':
        ver_listado_palabras()
    elif opcion == 'f':
        buscar_significado()
    elif opcion == 'g':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
conn.close()
