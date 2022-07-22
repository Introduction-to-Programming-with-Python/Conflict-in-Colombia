from PIL.Image import NONE
from numpy import mat
import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter
from pandas.core.frame import DataFrame
from pandas.core.indexes import datetimes
import matplotlib.image as mpimg
import matplotlib.patches as mpatches

def requerimiento_0(ruta_archivo:str)->DataFrame:

    """

    Funcion
    
        Cargar el archivo de datos

    Entradas

        ruta_archivo: str correspondiente a la ruta del archivo que 
        se quiere cargar

    Salida

        Estructura de datos con la informacion del archivo
        inresado: DataFrame

    """

    return pd.read_csv(ruta_archivo)

def requerimiento_1(data: DataFrame):

    """

    Funcion
    
        Muestra la distribución de los desmovilizados según grupo armado

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

    Salida

        Grafica: plt

    """

    # Se eliminan las filas las cuales en la columna del grupo armado
    # cotienen datos desconocidos
    data = data.iloc[:, :][data.ExGrupo != 'SIN DATO'][data.ExGrupo != 'SIN DATO MINDEFENSA']
    
    # Se calcula el total de filas del DataFrame reultante de la
    # filtracion anterior
    total = data.shape[0]

    # Se obtiene una lista de todos los grupos armados
    grupos = list((data.iloc[:, 1].unique()))

    # Se crea un diccionario para almancenar los porcentajes de cada
    # grupo armado
    gruposInfo = {}

    # Se itera en cada grupo armado, se calcula su porcentaje y se 
    # almacena en el diccionario
    for i in grupos:
        conteo = (data.iloc[:, 1][data.ExGrupo == i].value_counts())[0]
        porcentaje = (conteo/total) * 100
        gruposInfo[i] = porcentaje


    # Se prepara la grafica y se muestra
    labels = 'AUC', 'FARC', "ELN", "ERG", "ERP", "EPL"

    sizes = [
                gruposInfo["AUC"],
                gruposInfo["FARC"],
                gruposInfo["ELN"],
                gruposInfo["ERG"],
                gruposInfo["ERP"],
                gruposInfo["EPL"] 
            ]

    legendLabels = [
                        f"{'AUC'},{round(gruposInfo['AUC'], 1)}",
                        f"{'FARC'},{round(gruposInfo['FARC'], 1)}",
                        f"{'ELN'},{round(gruposInfo['ELN'], 1)}",
                        f"{'ERG'},{round(gruposInfo['ERG'], 1)}",
                        f"{'ERP'},{round(gruposInfo['ERP'], 1)}",
                        f"{'EPL'},{round(gruposInfo['EPL'], 1)}"
                    ]   

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=360)
    ax1.axis('equal')
    plt.title(f"Diagrama de torta segun ex grupo armado")
    plt.legend( loc='lower left', labels=legendLabels)
    plt.show()

def requerimiento_2(data: DataFrame, añoInicial: int, añoFinal: int):

    """

    Funcion
    
        Muestra la tendencia del número de desmovilizados por un rango
        de años

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

        añoInicial: int del año inicial para el rango

        añoFinal: int del año final para el rango

    Salida

        Grafica: plt

    """

    # Se filtra el DataFrame para conservar unicamente las filas
    # en las cuales el año que se encuentra en la columna del año de 
    # desmovilizacion entra dentro del rango ingresado por el usuario
    dataRange = data.iloc[:, :][data.AnioDesmovilizacion >= añoInicial][data.AnioDesmovilizacion <= añoFinal]
    
    # Se obtiene la lista de los años que se encuentran en el DataFrame
    # resultante de la operacion anterior
    activity = list((dataRange.iloc[:, 2].unique()))

    # Se crea una nueva lista para almacenar el conteo por departamento
    cat = []

    # Se calula el conteo por departamento y se inserta la cantidad en la
    # lista creada anteriormente
    for i in activity:
        cantidad = data.iloc[:, :][data.AnioDesmovilizacion == i].shape[0]
        cat.append(cantidad)

    # Se prepara la grafica y se muestra
    fig, ax = plt.subplots()
    ax.plot(activity, cat)
    plt.ylabel("Numero de desmovlizados")
    plt.xlabel("Año de desmovilizacion")
    plt.show()

def requerimiento_3(data: DataFrame, desmovilizacion: str):

    """

    Funcion
    
        Muestra un top de 5 departamentos por tipo de desmovilización

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

        desmovilizacion: str del tipo de desmovilizacion sobre el cual
        se quiere consultar la informacion

    Salida

        Grafica: plt

    """

    # Se filtra el DataFrame para conservar unicamente las filas
    # en las cuales el tipo de desmovilizacion que se encuentra en la
    # columna de tipo de desmovilizacion sea el tipo ingresado por el 
    # usuario
    data = data.iloc[:, :][data.TipoDeDesmovilizacion == desmovilizacion]

    # Se obtiene la lista de departamentos del DataFrame resultante de la
    # operacion anterior
    departamentosList = list(data.iloc[:, 5].unique())

    # Se crea un nuevo diccionario para almacenar el conteo de
    # desmovilizaciones por cada departamento, donde las llaves seran 
    # el departamento y los valores, los respectivos conteos
    conteo = {}

    # Se calcula y carga la informacion al dicccionario creado
    # anteriormente
    for i in departamentosList:
        cantidad = data.iloc[:, :][data.DepartamentoDeResidencia == i].shape[0]
        conteo[i] = cantidad

    # Se ordena el diccionario por el valor de sus llaves, de mayor
    # a menor
    top = dict(sorted(conteo.items(), key=itemgetter(1), reverse=True))

    # Se obtiene la lista de llaves del diccionario resultante de la
    # operacion anterior, las cuales son los departamentos
    departamentos = list(top.keys())
    departamentos.reverse()

    # Se obtiene la lista de valores del diccionario, los cuales son
    # el conteo de desmovilizaciones en cada departamento
    conteos = list(top.values())
    conteos.reverse()

    # Se prepara la grafica y se muestra
    plt.barh(departamentos[-5:], conteos[-5:])
    plt.ylabel("Departamento de residencia")
    plt.show()

def requerimiento_4(data: DataFrame):

    """

    Funcion
    
        Muestra la distribución  del número de hijos  que tienen los
        desmovilizados según su sexo

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

    Salida

        Grafica: plt

    """
    # Se filtran unicamente las columnas que se van a usar del DataFrame,
    # se prepara la grafica y se muestra.
    data = data.loc[:, ["Sexo", "NumDeHijos"]].boxplot(by="Sexo", rot=90,figsize=(15,10))  
    plt.title("Numero de hijos por sexo")
    plt.xlabel("Sexo")
    plt.ylabel("Numero de hijos")
    plt.show()

def requerimiento_5(data: DataFrame):

    """

    Funcion
    
        Muestra la la ocupación de los individuos que hayan recibido
        algún beneficio o desembolso

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

    Salida

        Grafica: plt

    """

    # Se filtra el DataFrame por las personas que han recibido algun
    # tipo de beneficio
    data = data.iloc[:, :][(data.BeneficioTRV == "Sí") | (data.BeneficioFA == "Sí") | (data.BeneficioFPT == "Sí") | (data.BeneficioPDT == "Sí") | (data.DesembolsoBIE == "Sí")]
    
    # Se extrae del DataFrame una lista de ocupaciones
    ocupacionesList = list(data.iloc[:, 11].unique())
    
    # Se crea un diccionario para almancenar las ocupaciones, las cuales
    # seran las llaves del diccionario, y el conteo de personas que
    # ejercen determinada labor y que a la vez reciben algun beneficio,
    # este conteo sera el valor de cada llave
    conteo = {}

    # Se carga la informacion al diccionario anterior
    for i in ocupacionesList:
        cantidad = data.iloc[:, :][data.OcupacionEconomica == i].shape[0]
        conteo[i] = cantidad

    # Se prepara la grafica y se muestra
    courses = list(conteo.keys())
    values = list(conteo.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(courses, values, width = 0.4)
    plt.xlabel("Ocupacion economica")
    plt.show()

def requerimiento_6(data: DataFrame):

    """

    Funcion
    
        Crea una matriz de departamento vs ex grupo, un diccionario para
        indicar la posicion de los departamento en la matriz y otro
        diccionario para indicar la poscion de los ex grupos armados en
        la matriz

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

    Salida

        output: tuple de tres posiciones que contien en la primera
        posicion la matriz, en la segunda el diccionario de posiciones de
        departamentos y en la tercera el diccionario de poscisiones de
        los ex grupos armados

    """

    # Se eliminan las filas las cuales en la columna del grupo armado
    # cotienen datos desconocidos
    data = data.iloc[:, :][(data.ExGrupo != "SIN DATO") & (data.ExGrupo != "SIN DATO MINDEFENSA")]
    
    # Se obtiene una lista de departamentos ordenada ascendente y
    # alfabeticamente
    departamentosList = sorted(list(data.iloc[:, 5].unique()))

    # Se obtiene una lista de ex grupos armados ordenada ascendente y
    # alfabeticamente
    grupoList = sorted(list(data.iloc[:, 1].unique()))

    # Se crea el diccionario de filas
    dictFilas = {}
    pos = 0
    for i in departamentosList:
        dictFilas[pos] = i
        pos += 1

    # Se crea el diccionario de columnas
    pos = 0
    dictColumnas = {}
    for i in grupoList:
        dictColumnas[pos] = i
        pos += 1

    # Se crea la matriz
    matriz = []
    for i in departamentosList:
        filaDepartamento = []
        for j in grupoList:
            conteo = data.iloc[:, :][data.DepartamentoDeResidencia == i][data.ExGrupo == j].shape[0]
            filaDepartamento.append(conteo)
        matriz.append(filaDepartamento)
    
    # Se crea la tupla de retorno
    output = (matriz, dictFilas, dictColumnas)

    return output

def requerimiento_7(data: DataFrame, departamento: str) -> str:

    """

    Funcion
    
        Consultar el grupo con más desmovilizados por departamento dado

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

        departamento: str del nombre del departamento del cual se quiere
        la informacion

    Salida

        str: str con el nombre del grupo con mas desmovilizados en el 
        departamento dado

    """

    # Se eliminan las filas las cuales en la columna del grupo armado
    # cotienen datos desconocidos
    dataClean = data.iloc[:, :][(data.ExGrupo != "SIN DATO") & (data.ExGrupo != "SIN DATO MINDEFENSA")]
    
    # Se obtiene una lista de departamentos ordenada ascendente y
    # alfabeticamente
    departamentosList = sorted(list(dataClean.iloc[:, 5].unique()))

    # Se obtiene una lista de ex grupos armados ordenada ascendente y
    # alfabeticamente
    grupoList = sorted(list(dataClean.iloc[:, 1].unique()))

    # Se crea un diccionario de filas pasa saber la posicion de cada
    # departamento en la matriz, en donde las llave seran la posicion 
    # y el valor sera el departemanto que se encuentra en esa posicion 
    dictFilas = {}
    pos = 0
    for i in departamentosList:
        dictFilas[i] = pos
        pos += 1

    # Se crea un diccionario de columnas pasa saber la posicion de cada
    # ex grupo en la matriz, en donde las llave seran el nombre del 
    # exgrupo y el valor sera la posicion de columna en la que se encuentra 
    pos = 0
    dictColumnas = {}
    for i in grupoList:
        dictColumnas[pos] = i
        pos += 1

    # Se obtiene la matriz creada en el requerimiento 6
    matriz = requerimiento_6(data)[0]

    # Se obtiene la posicion de fila en la cual se encuentra el
    # departamento en la matriz
    posDepartamento = dictFilas[departamento]

    # Se accede a la fila de la matriz en donde se encuentra la
    # informacion del departamento ingresado por el ususario
    matrizDepartamento = matriz[posDepartamento]

    # Se obtiene el valor maximo de la lista ala cual se accedio 
    # anteriormente, la cual corresponde al mayor numero de
    # desmovilzados en ese departmento
    maximo = max(matrizDepartamento)

    # Se accede a la posicion en la cual se encontro el numero maximo
    # encotrado anteriormente
    pos = matrizDepartamento.index(maximo)

    # Se encuentra el grupo al cual corresponde el numero maximo de 
    # desmovilizados
    grupo = dictColumnas[pos]

    return grupo

def requerimiento_8(data: DataFrame, grupo: str) -> int:

    """

    Funcion
    
        Consultar la cantidad de personas por grupo

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

        grupo: str del nombre del grupo del cual se quiere la informacion

    Salida

        conteo: int con la cantidad requerida

    """

    # Se eliminan las filas las cuales en la columna del grupo armado
    # cotienen datos desconocidos
    dataClean = data.iloc[:, :][(data.ExGrupo != "SIN DATO") & (data.ExGrupo != "SIN DATO MINDEFENSA")]

    # Se obtiene una lista de ex grupos armados ordenada ascendente y
    # alfabeticamente
    grupoList = sorted(list(dataClean.iloc[:, 1].unique()))

    # Se crea un diccionario de columnas pasa saber la posicion de cada
    # ex grupo en la matriz, en donde las llave seran el nombre del 
    # exgrupo y el valor sera la posicion de columna en la que se encuentra 
    pos = 0
    dictColumnas = {}
    for i in grupoList:
        dictColumnas[i] = pos
        pos += 1

    # Se obtiene la posicion de columna en la cual se enuentra el conteo
    # con respecto al grupo armado ingresado por el usuario
    posGrupo = dictColumnas[grupo]

    # Se obtiene la matriz creada en el requerimiento 6
    matriz = requerimiento_6(data)[0]
    
    # Se crea una variable para sumar la cantidad de demovilizados del 
    # grupo en cada departamento
    conteo = 0

    # Se realiza el conteo recorriendo la matriz departamento por
    # departamento y sumando el valor que se encuentra en la columna
    # correspondiente al grupo armado
    for i in matriz:
        conteo += i[posGrupo]

    return conteo

def requerimiento_9(data: DataFrame) -> tuple:

    """

    Funcion
    
        Consultar el departamento y grupo armado con mayor cantidad de
        desmovilizados

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

    Salida

        tuple: tuple con la informacion solicitada

    """

    # Se obtiene la matriz, el diccionario de filas y de columnas
    # creados en el requerimiento 6
    matriz = requerimiento_6(data)[0]
    dictFilas = requerimiento_6(data)[1]
    dictColumnas = requerimiento_6(data)[2]

    # Se crea una variable para identificar la posicion de fila por 
    # las cual se va recorriendo la matriz.
    pos = 0

    # Se crea un diccionario para almacenar el valor maximo
    # encontrado en cada fila. Las llaves seran la posicion
    # de la fila y el valor el numero maximo encontrado en
    # esta, el cual corresponde al mayor numero de demovilizados
    # en el departamento.
    dictFilasMax = {}

    for i in matriz:
        dictFilasMax[pos] = max(i)
        pos += 1

    # Se ordena el diccionario por el valor de sus llaves, de mayor
    # a menor
    dictFilasMax = dict(sorted(dictFilasMax.items(), key=itemgetter(1), reverse=True))

    # Se crea una lista con las llaves del diccionario anterior y
    # se obtiene su primer elemento, el cual corresponde a las
    # posicion del departamento en donde se dio el mayor numero
    # de desmovilizaciones
    maxDepartmentPos = (list(dictFilasMax.keys()))[0]

    # Se encuentra el departamento al cual le corresponde esta
    # posicion en la matriz
    departamento = dictFilas[maxDepartmentPos]

    # Se crea una lista con los valores del diccionario anterior y
    # se obtiene su primer elemento, el cual corresponde al mayor
    # numero de desmovilizaciones en el departamento obtenido
    # anteriormente
    maxGroupValue = (list(dictFilasMax.values()))[0]

    # Se halla la poscion de columna en la cual se encuentra el
    # valor encontrado anteriormente
    maxGroupPos = matriz[maxDepartmentPos].index(maxGroupValue)

    # Con la posicion encotrada anteriormente, se accede al
    # al nomre de grupo armado al que le corresponde esa
    # posicion
    maxGroupName = dictColumnas[maxGroupPos]

    return (departamento, maxGroupName)

def requerimiento_10(data: DataFrame):

    """

    Funcion
    
        Grafia el ex grupo con mayor desmovilización por departamento

    Entradas

        data: DataFrame con los datos necesario para la elaboracion de 
        la funcion

    Salida

        plt: plt grafica que muestra la informacion consultada

    """

    # Se crea un diccionario para almacenar las coordenadas de la 
    # ubicacion de los departamentos en la imagen. Las llaves 
    # seran los nombres de los departamentos y los valores una
    # tupla con las cordenadas del respectivo departamento
    deptos = {}

    # Se lee el archivo de coordenadas y se carga al diccionario
    # creado anteriormente
    archivo = open("./data/coordenadas.txt", encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()

    # Se eliminan las filas las cuales en la columna del grupo armado
    # cotienen datos desconocidos
    dataClean = data.iloc[:, :][(data.ExGrupo != "SIN DATO") & (data.ExGrupo != "SIN DATO MINDEFENSA")]
    
    # Se obtiene una lista de departamentos ordenada ascendente y
    # alfabeticamente
    departamentosList = sorted(list(dataClean.iloc[:, 5].unique()))

    # Se crea un diccionario en donde las llaves seran los 
    # departamento y los valores, el grupo armado con mayor
    # cantidad de desmovilizaciones en cada departamento
    info = {}

    # Se carga la informacion al diccionario creado 
    # anteriormente usando la funcion del requerimiento 7
    # ya que nos calcula el grupo armado que estamos buscando
    for i in departamentosList:
        info[i] = requerimiento_7(data, i)

    # Se carga la imagen del mapa y se convierte a matriz
    mapa = mpimg.imread("./data/mapa.png").tolist()

    # Se toma cada departamento y se pinta en su parte del
    # mapa el color que sirve para identificar el grupo 
    # armado que mayor numero de desmovilizaciones tuvo
    for i in departamentosList:

        grupo = info[i]

        if grupo == "AUC":

            kInicio = deptos[i][0] - 13
            kFin = kInicio + 14
            lInicio = deptos[i][1]
            lFin = lInicio + 14
            for k in range(kInicio, kFin):
                for l in range(lInicio, lFin):
                    mapa[k][l] = [1.0, 1.0, 0.0]
        
        if grupo == "ELN":

            kInicio = deptos[i][0] - 13
            kFin = kInicio + 14
            lInicio = deptos[i][1]
            lFin = lInicio + 14
            for k in range(kInicio, kFin):
                for l in range(lInicio, lFin):
                    mapa[k][l] = [1.0, 0.0, 0.0]
        
        if grupo == "EPL":

            kInicio = deptos[i][0] - 13
            kFin = kInicio + 14
            lInicio = deptos[i][1]
            lFin = lInicio + 14
            for k in range(kInicio, kFin):
                for l in range(lInicio, lFin):
                    mapa[k][l] = [1.0, 0.0, 1.0]
        
        if grupo == "ERG":

            kInicio = deptos[i][0] - 13
            kFin = kInicio + 14
            lInicio = deptos[i][1]
            lFin = lInicio + 14
            for k in range(kInicio, kFin):
                for l in range(lInicio, lFin):
                    mapa[k][l] = [0.0, 1.0, 1.0]
        
        if grupo == "ERP":

            kInicio = deptos[i][0] - 13
            kFin = kInicio + 14
            lInicio = deptos[i][1]
            lFin = lInicio + 14
            for k in range(kInicio, kFin):
                for l in range(lInicio, lFin):
                    mapa[k][l] = [0.0, 1.0, 0.0]
        
        if grupo == "FARC":

            kInicio = deptos[i][0] - 13
            kFin = kInicio + 14
            lInicio = deptos[i][1]
            lFin = lInicio + 14
            for k in range(kInicio, kFin):
                for l in range(lInicio, lFin):
                    mapa[k][l] = [1.0, 0.5, 0.5]

    # Se prepara la grafica y se muestra
    plt.imshow(mapa)
    AUC_color = mpatches.Patch(color=(1.0, 1.0, 0.0), label='AUC')
    ELN_color = mpatches.Patch(color=(1.0, 0.0, 0.0), label='ELN')
    EPL_color = mpatches.Patch(color=(1.0, 0.0, 1.0), label='EPL')
    ERG_color = mpatches.Patch(color=(0.0, 1.0, 1.0), label='ERG')
    ERP_color = mpatches.Patch(color=(0.0, 1.0, 0.0), label='ERP')
    FARC_color = mpatches.Patch(color=(1.0, 0.5, 0.5), label='FARC')
    plt.legend(handles=[AUC_color, ELN_color, EPL_color, ERG_color, ERP_color, FARC_color])
    plt.show()