import pandas as pd
from datetime import datetime

def guardar_ventas():
    """
    Guarda los datos de ventas en el archivo "ventas.xlsx".

    Parameters:
    None

    Returns:
    None
    """
    ventas = cargar_ventas()
    if ventas is not None:
        ventas.to_excel("ventas.xlsx", index=False)
        print("Datos de ventas guardados exitosamente.")
    else:
        print("No hay datos de ventas para guardar.")


def cargar_ventas():
    """
    Carga los datos de ventas desde el archivo "ventas.xlsx".

    Returns:
    DataFrame or None: DataFrame con los datos de ventas, o None si el archivo no existe.
    """
    try:
        ventas = pd.read_excel("ventas.xlsx")
        return ventas
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.xlsx'.")
        return None

def guardar_ventas_excel(ventas):
    """
    Guarda los datos de ventas en el archivo "ventas.xlsx".

    Parameters:
    ventas (DataFrame): DataFrame que contiene los datos de ventas.

    Returns:
    None
    """
    if ventas is not None:
        ventas.to_excel("ventas.xlsx", index=False)
        print("Datos de ventas guardados exitosamente.")
    else:
        print("No hay datos de ventas para guardar.")


def cargar_datos():
    """
    Carga los datos del inventario desde el archivo "inventario.xlsx".

    Returns:
    DataFrame or None: DataFrame con los datos del inventario, o None si el archivo no existe.
    """
    try:
        datos = pd.read_excel("inventario.xlsx")
        return datos
    except FileNotFoundError:
        print("No se encontró el archivo 'inventario.xlsx'.")
        return None


def buscar_articulo(datos):
    """
    Busca un artículo en el inventario por su nombre.

    Parameters:
    datos (DataFrame): DataFrame que contiene los datos del inventario.

    Returns:
    None
    """
    nombre_articulo = input("Artículo a buscar: ")
    articulo_encontrado = datos[datos['Nombre'].str.contains(nombre_articulo, case=False)]
    if articulo_encontrado.empty:
        print("No se encontraron artículos con ese nombre.")
    else:
        print(articulo_encontrado)

def agregar_cantidad_existencia(datos):
    """
    Agrega más cantidad en existencia a un producto existente en el inventario.

    Parameters:
    datos (DataFrame): DataFrame que contiene los datos del inventario.

    Returns:
    DataFrame: DataFrame actualizado del inventario.
    """
    id_articulo = input("Ingrese el ID del artículo al que desea agregar cantidad en existencia: ")
    cantidad_nueva = int(input("Cantidad adicional en Existencia: "))
    
    # Convertir el ID del artículo ingresado a un entero
    id_articulo = int(id_articulo)
    
    # Verificar si el ID del artículo existe en el inventario
    if id_articulo in datos["ID"].values:
        # Incrementar la cantidad en existencia del artículo
        datos.loc[datos["ID"] == id_articulo, "Cant. Existencia"] += cantidad_nueva
        print("Cant. Existencia actualizada exitosamente.")
    else:
        print("No se encontró ningún artículo con ese ID en el inventario.")
    
    return datos



def agregar_articulo(datos):
    """
    Agrega un nuevo artículo al inventario y actualiza el archivo "inventario.xlsx".

    Parameters:
    datos (DataFrame): DataFrame que contiene los datos del inventario.

    Returns:
    DataFrame: DataFrame actualizado del inventario.
    """
    id_articulo = input("Ingrese el ID del nuevo artículo: ")
    nombre = input("Nombre del nuevo artículo: ")
    categoria = input("Categoría del nuevo artículo: ")
    precio = float(input("Precio del nuevo artículo: "))
    cantidad = int(input("Cant. Existencia del nuevo artículo: "))
    
    # Formato del nombre del artículo
    nombre = nombre.lower().capitalize()  # Primer letra mayúscula, resto minúsculas
    
    nuevo_articulo = {'ID': id_articulo, 'Nombre': nombre, 'Categoría': categoria, 'Precio': precio, 'Cant. Existencia': cantidad}
    nuevo_datos = pd.DataFrame([nuevo_articulo])
    
    datos = pd.concat([datos, nuevo_datos], ignore_index=True)
    datos.drop_duplicates(subset="ID", keep="first", inplace=True)
    
    # Guardar los cambios en el archivo "inventario.xlsx"
    datos.to_excel("inventario.xlsx", index=False)
    print("Nuevo artículo agregado al inventario.")
    
    return datos


def vender_articulo(datos):
    """
    Registra la venta de un artículo y actualiza el inventario.

    Parameters:
    datos (DataFrame): DataFrame que contiene los datos del inventario.

    Returns:
    DataFrame: DataFrame actualizado del inventario.
    """
    nombre_articulo = input("Ingrese el nombre del artículo vendido: ").lower()  # Convertir a minúsculas
    cantidad_vendida = int(input("Cantidad vendida: "))
    
    articulo = datos[datos['Nombre'].str.lower() == nombre_articulo]  # Convertir a minúsculas para la comparación
    
    if not articulo.empty:
        nombre_articulo = articulo.iloc[0]['Nombre']  # Mantener el formato del nombre del artículo en el inventario
        existencia_actual = articulo.iloc[0]['Cant. Existencia']
        if existencia_actual >= cantidad_vendida:
            datos.loc[datos['Nombre'].str.lower() == nombre_articulo.lower(), 'Cant. Existencia'] -= cantidad_vendida
            datos.to_excel("inventario.xlsx", index=False)
            print(f"Se han vendido {cantidad_vendida} unidades de {nombre_articulo}.")
        else:
            print(f"No hay suficientes unidades en existencia de {nombre_articulo}.")
    else:
        print(f"El artículo {nombre_articulo} no existe en el inventario.")
    
    return datos



def main():
    """
    Función principal del programa.
    """
    datos = cargar_datos()
    if datos is not None:
        print("Inventario:")
        print(datos)

        ventas = cargar_ventas()

        while True:
            print("\n1. Agregar artículo")
            print("2. Buscar artículo")
            print("3. Vender artículo")
            print("4. Ver inventario")
            print("5. Ver ventas")
            print("6. Añadir cantidad en existencia")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                datos = agregar_articulo(datos)
            elif opcion == "2":
                buscar_articulo(datos)
            elif opcion == "3":
                datos = vender_articulo(datos)
                guardar_ventas()  # Aquí se llama a guardar_ventas sin argumentos
            elif opcion == "4":
                print("Inventario:")
                print(datos)
            elif opcion == "5":
                if ventas is not None:
                    print("Ventas:")
                    print(ventas)
                else:
                    print("No hay ventas registradas.")
            elif opcion == "6":
                datos = agregar_cantidad_existencia(datos)
            elif opcion == "7":
                guardar_ventas(ventas)  # Aquí se llama a guardar_ventas sin argumentos
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
