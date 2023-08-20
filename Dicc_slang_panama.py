import sqlite3

def crear_tabla():
    # Conexión a la base de datos o creación si no existe
    conn = sqlite3.connect("slang_panameno.db")
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL UNIQUE,
            significado TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def agregar_palabra():
    palabra = input("Ingrese la nueva palabra: ")
    significado = input("Ingrese el significado de la palabra: ")

    conn = sqlite3.connect("slang_panameno.db")
    cursor = conn.cursor()
    
    # Insertar nueva palabra en la tabla
    cursor.execute("INSERT INTO palabras (palabra, significado) VALUES (?, ?)", (palabra, significado))
    
    conn.commit()
    conn.close()

def editar_palabra():
    palabra = input("Ingrese la palabra que desea editar: ")
    nuevo_significado = input("Ingrese el nuevo significado de la palabra: ")

    conn = sqlite3.connect("slang_panameno.db")
    cursor = conn.cursor()
    
    # Actualiza
    cursor.execute("UPDATE palabras SET significado = ? WHERE palabra = ?", (nuevo_significado, palabra))
    
    conn.commit()
    conn.close()

def eliminar_palabra():
    palabra = input("Ingrese la palabra que desea eliminar: ")

    conn = sqlite3.connect("slang_panameno.db")
    cursor = conn.cursor()
    
    # Eliminar la palabra de la tabla
    cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra,))
    
    conn.commit()
    conn.close()

def ver_listado_palabras():
    conn = sqlite3.connect("slang_panameno.db")
    cursor = conn.cursor()
    
    # Obtener todas las palabras y sus significados
    cursor.execute("SELECT palabra, significado FROM palabras")
    palabras = cursor.fetchall()

    for palabra, significado in palabras:
        print(f"{palabra}: {significado}")
    
    conn.close()

def buscar_significado():
    palabra = input("Ingrese la palabra que desea buscar: ")

    conn = sqlite3.connect("slang_panameno.db")
    cursor = conn.cursor()
    
    # Buscar la palabra en la tabla
    cursor.execute("SELECT significado FROM palabras WHERE palabra = ?", (palabra,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"{palabra}: {resultado[0]}")
    else:
        print(f"La palabra '{palabra}' no fue encontrada en el diccionario.")
    
    conn.close()

def main():
    crear_tabla()

    while True:
        print("\n--- Diccionario de Slang Panameño ---")
        print("a) Agregar nueva palabra")
        print("b) Editar palabra existente")
        print("c) Eliminar palabra existente")
        print("d) Ver listado de palabras")
        print("e) Buscar significado de palabra")
        print("f) Salir")

        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            agregar_palabra()
        elif opcion == "b":
            editar_palabra()
        elif opcion == "c":
            eliminar_palabra()
        elif opcion == "d":
            ver_listado_palabras()
        elif opcion == "e":
            buscar_significado()
        elif opcion == "f":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
