from pandas import DataFrame
import desmovilizados as file

def ejecutarRequerimiento_0() -> DataFrame:
    archivo = input("Ingrese el nombre del archivo CSV: ")
    archivo = "./data/" + archivo + ".csv"

    return file.requerimiento_0(archivo)

def ejecutarRequerimiento_1(data: DataFrame):
    return file.requerimiento_1(data)

def ejecutarRequerimiento_2(data: DataFrame):
    añoIncial = int(input("Inserte el año incial para el rango: "))
    añoFinal = int(input("Inserte el año final para el rango: "))
    return file.requerimiento_2(data, añoIncial, añoFinal)

def ejecutarRequerimiento_3(data: DataFrame):
    desmovilizacion = input("Inserte el tipo de desmovilizacion: ")
    return file.requerimiento_3(data, desmovilizacion)

def ejecutarRequerimiento_4(data: DataFrame):
    return file.requerimiento_4(data)

def ejecutarRequerimiento_5(data: DataFrame):
    return file.requerimiento_5(data)

def ejecutarRequerimiento_6(data: DataFrame):
    return file.requerimiento_6(data)

def ejecutarRequerimiento_7(data: DataFrame):
    departamento = input("Inserte el departamento en el cual desea consultar la informacion: ")
    functionOutput = file.requerimiento_7(data, departamento)
    return f"\nEl grupo con más desmovilizados en {departamento} es {functionOutput}.\n"

def ejecutarRequerimiento_8(data: DataFrame):
    grupo = input("Inserte el grupo en el cual desea consultar la informacion: ")
    functionOutput = file.requerimiento_8(data, grupo)
    return f"\nEl total de desmovilizados en el grupo {grupo} es de {functionOutput}.\n"

def ejecutarRequerimiento_9(data: DataFrame):
    functionOutput = file.requerimiento_9(data)
    return f"\n{functionOutput}\n"

def ejecutarRequerimiento_10(data: DataFrame):
    return file.requerimiento_10(data)

def mostrar_menu():

    """

        Muestra las opciones que el usuario puede ejecutar.

    """
    
    print("0. Cargar el archivo de datos.")
    print("1. Consultar la distribución de los desmovilizados según grupo armado.")
    print("2. Consultar la tendencia del número de desmovilizados por un rango de años.")
    print("3. Consultar un top de 5 departamentos por tipo de desmovilización.")
    print("4. Consultar la distribución  del número de hijos  que tienen los desmovilizados según su sexo.")
    print("5. Consultar la ocupación de los individuos que hayan recibido algún beneficio o desembolso.")
    print("6. Construir una matriz de departamento vs ex grupo")
    print("7. Consultar el grupo con más desmovilizados por departamento dado.")
    print("8. Consultar la cantidad de personas por grupo.")
    print("9. Consultar el número de evaluados por estrato.")
    print("10. Consultar el ex grupo con mayor desmovilización por departamento.")

def iniciar_aplicacion():

    """
        
        Ejecuta el programa para el usuario.
        
    """

    continuar  = True
    while continuar:
        mostrar_menu()
        opcion_seleccionada = input("\nEscriba el indice de la opcion que desea ejecutar: ")
        if opcion_seleccionada == "0":
            data = ejecutarRequerimiento_0()
            print(data)
            print("\nLos datos se han cargado correctamente.\n")
        elif opcion_seleccionada == "1":
            ejecutarRequerimiento_1(data)
        elif opcion_seleccionada == "2":
            ejecutarRequerimiento_2(data)
        elif opcion_seleccionada == "3":
            ejecutarRequerimiento_3(data)
        elif opcion_seleccionada == "4":
            ejecutarRequerimiento_4(data)
        elif opcion_seleccionada == "5":
            print(ejecutarRequerimiento_5(data))
        elif opcion_seleccionada == "6":
            print(ejecutarRequerimiento_6(data))
        elif opcion_seleccionada == "7":
            print(ejecutarRequerimiento_7(data))
        elif opcion_seleccionada == "8":
            print(ejecutarRequerimiento_8(data))
        elif opcion_seleccionada == "9":
            print(ejecutarRequerimiento_9(data))
        elif opcion_seleccionada == "10":
            print(ejecutarRequerimiento_10(data))
        else:
            continuar = False

#PROGRAMA PRINCIPAL
iniciar_aplicacion()