from SpeechAndTalk import * 
import re
from usarModelos import *
from util import * 
import pandas as pd
from datetime import date
# Función para predecir la calidad de un vino
def WinePrediction():
    params = {
        }
    Jackie_Habla("Haz accedido a la función para probar la calidad del vino, a continuación, me diras las carácteristicas del vino del cual deseas predecir su calidad, para terminar pronuncia la palabra cancelar")
    ###############################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el porcentaje de acidez fija en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme la acidez fija del vino")
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["fixed acidity"] = [float(valor)]
            respuesta = "acidez fija del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el porcentaje de acidez volatil en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme la acidez fija")
        elif ("%" in escucha or "por ciento"):
            valor = float(valor) / 100
            params["volatile acidity"] = [valor]
            respuesta = "acidez fija del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["volatile acidity"] = [float(valor)]
            respuesta = "acidez fija del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el porcentaje de ácido cítrico en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el porcentaje de ácido cítrico")
        elif ("%" in escucha or "por ciento"):
            valor = float(valor) / 100
            params["citric acid"] = [valor]
            respuesta = " porcentaje de ácido cítrico del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["citric acid"] = [float(valor)]
            respuesta = "porcentaje de ácido cítrico del vino confirmado de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el valor de azúcar residual en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el valor de azúcar residual del vino")
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["residual sugar"] = [float(valor)]
            respuesta = " azúcar residual del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el valor de los cloruros en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el valor de los cloruros")
        elif ("%" in escucha or "por ciento"):
            valor = float(valor) / 100
            params["chlorides"] = [valor]
            respuesta = "el valor de los cloruros del vino confirmado de: " + str(valor)
            Jackie_Habla(respuesta)
            break
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["chlorides"] = [float(valor)]
            respuesta = "el valor de los cloruros del vino confirmado de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el valor de dióxido de sulfuro en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el valor de dióxido de sulfuro del vino")
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["free sulfur dioxide"] = [float(valor)]
            respuesta = " dióxido de sulfuro del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el valor total de dióxido de sulfuro en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el valor total de dióxido de sulfuro del vino")
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["total sulfur dioxide"] = [float(valor)]
            respuesta = " total dióxido de sulfuro del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el porcentaje de densidad en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el porcentaje de densidad")
        elif ("%" in escucha or "por ciento"):
            valor = float(valor) / 100
            params["density"] = [valor]
            respuesta = " porcentaje de densidad del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["density"] = [float(valor)]
            respuesta = "porcentaje de densidad del vino confirmado de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el pe hache del vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el pe hache del vino")
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["pH"] = [float(valor)]
            respuesta = " pe hache del vino confirmado de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el porcentaje de sulfatos en el vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el porcentaje de sulfatos")
        elif ("%" in escucha or "por ciento"):
            valor = float(valor) / 100
            params["sulphates"] = [valor]
            respuesta = " porcentaje de sulfatos del vino confirmada de: " + str(valor)
            Jackie_Habla(respuesta)
            break
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["sulphates"] = [float(valor)]
            respuesta = "porcentaje de sulfatos del vino confirmado de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime cual es el porcentaje de alcohol del vino")
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        if valor == "":
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el porcentaje de alcohol")
        elif ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        else:
            params["alcohol"] = [float(valor)]
            respuesta = " porcentaje de alcohol del vino confirmado de: " + str(valor)
            Jackie_Habla(respuesta)
            break
    ################################################################################################################################################
    Jackie_Habla("Ahora, Dime si el vino es claro o es oscuro")
    while True:
        escucha = jackie_Escucha()
        if ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de predecir la calidad del vino")
            break
        elif "claro" in escucha:
            params["white"] = [1]
            respuesta = "tipo de alcohol confirmado como claro"
            Jackie_Habla(respuesta)
            break
        elif "oscuro" in escucha: 
            params["white"] = [0]
            respuesta = "tipo de alcohol confirmado como oscuro"
            Jackie_Habla(respuesta)
            break
        elif "oscuro" in escucha and "claro" in escucha: 
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el tipo de alcohol")
        else:
            Jackie_Habla("Perdona, no entendí eso, puedes repetirme el tipo de alcohol")
    ################################################################################################################################################
    """
    test = {
    "fixed acidity" : [5.7],
    "volatile acidity" : [0.68],
    "citric acid" : [0.49],
    "residual sugar" : [1.8],
    "chlorides" : [ 0.044 ],
    "free sulfur dioxide" : [21.0],
    "total sulfur dioxide" : [108.0],
    "density":[0.99574],
    "pH":[3.30],
    "sulphates":[0.59],
    "alcohol":[9.5],
    "white":[0]
    }
    """
    print(params)
    response = PredecirPrecioVino(params)
    if response[0] == 1:
        Jackie_Habla("Según los datos ofrecidos por ti el vino tiene una muy buena calidad según lo estándares de que me diste")
    else:
            Jackie_Habla("Según los datos ofrecidos por ti el vino tiene una mala calidad según lo estándares de que me diste")

def CirrosisPrediction():   
    return
def HepatitisPrediction():
    params = {}
    Jackie_Habla("Haz accedido a la función para predecir el tipo de hepatitis que posee un paciente, a continuación te preguntaré características de ese paciente, con el fin de predecir su tipo de hepatitis")
    preguntarValorNumerico(params,"edad","Age","predecir tipo de hepatitis")
    preguntarBool(params,"sexo","Sex","predecir tipo de hepatitis","masculino","femenino")
    preguntarValorNumerico(params,"niveles de albumim","ALB","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de Fosfatasa alcalina","ALP","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de la enzima A ELE TE","ALT","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de la enzima A ESE TE","AST","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de bilirubina","BIL","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de la enzima CE HACHE E","CHE","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de colesterol","CHOL","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de células inmunitarias que atacan el hígado","CREA","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de la enzima Ge Ge Te","GGT","predecir tipo de hepatitis")
    preguntarValorNumerico(params,"niveles de proteínas","PROT","predecir tipo de hepatitis")
    res = PredecirTipoHepatitis(params)
    if res[0] == 1:
        Jackie_Habla("Según el análisis de los datos que me proporcionaste, el paciente tiene hepatitis de tipo A")
    else: 
        Jackie_Habla("Según el análisis de los datos que me proporcionaste, el paciente tiene hepatitis de tipo B")
    return 
def StrokePrediction():
    params = {}
    Jackie_Habla("Haz accedido a la función para predecir si una persona tiene riesgo de sufrir un ataque cerebrovascular, a continuación te preguntaré características de esa persona, con el fin de predecir su riesgo")
    preguntarBool(params,"sexo","gender","predecir riesgo cerebrovascular","femenino","masculino")
    preguntarValorNumerico(params,"edad","age","predecir riesgo cerebrovascular")
    Jackie_Habla("¿Tiene hipertensión?")
    preguntarBool(params,"hipertensión","hypertension","predecir riesgo cerebrovascular","sí","no")
    Jackie_Habla("¿Tiene enfermedades del corazón?")
    preguntarBool(params,"enfermedades del corazón","heart_disease","predecir riesgo cerebrovascular","sí","no")
    Jackie_Habla("¿Está casado?")
    preguntarBool(params,"si esta casado","ever_married","predecir riesgo cerebrovascular","si","no")
    preguntarCategoria(params,"modalidad de trabajo","work_type","predecir riesgo cerebrovascular",['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    preguntarBool(params,"tipo de residencia","Residence_type","predecir riesgo cerebrovascular",'urbano', 'rural')
    preguntarValorNumerico(params,"nivel de glucosa en sangre","avg_glucose_level","predecir riesgo cerebrovascular")
    preguntarValorNumerico(params,"Indice de grasa Corporal","bmi","predecir riesgo cerebrovascular")
    preguntarCategoria(params,"Frecuencia de Fumado","smoking_status","predecir riesgo cerebrovascular",['formerly smoked', 'never smoked', 'smokes', 'Unknown'])
    res = PredecirAccidenteCerebroVascular(params)
    if res[0] == 0:
        Jackie_Habla("Según los datos proporcionados concluyen que la persona no es propensa a tener un accidente cerebroVascular")
    else:
        Jackie_Habla("Según los datos proporcionados concluyen que la persona es propensa a tener un accidente cerebroVascular")
    return
def AvocadoPrediction():
    params = {}
    lista_Regiones = ['Albany', 'Atlanta', 'BaltimoreWashington', 'Boise', 'Boston',
       'BuffaloRochester', 'California', 'Charlotte', 'Chicago',
       'CincinnatiDayton', 'Columbus', 'DallasFtWorth', 'Denver',
       'Detroit', 'GrandRapids', 'GreatLakes', 'HarrisburgScranton',
       'HartfordSpringfield', 'Houston', 'Indianapolis', 'Jacksonville',
       'LasVegas', 'LosAngeles', 'Louisville', 'MiamiFtLauderdale',
       'Midsouth', 'Nashville', 'NewOrleansMobile', 'NewYork',
       'Northeast', 'NorthernNewEngland', 'Orlando', 'Philadelphia',
       'PhoenixTucson', 'Pittsburgh', 'Plains', 'Portland',
       'RaleighGreensboro', 'RichmondNorfolk', 'Roanoke', 'Sacramento',
       'SanDiego', 'SanFrancisco', 'Seattle', 'SouthCarolina',
       'SouthCentral', 'Southeast', 'Spokane', 'StLouis', 'Syracuse',
       'Tampa', 'TotalUS', 'West', 'WestTexNewMexico']
    Jackie_Habla("Haz accedido a la función para predecir el precio del aguacate, a continuación te preguntaré características de las ventas del aguacate, con el fin de predecir su precio")
    preguntarValorNumerico(params,"cantidad de aguacates vendidos","Total Volume","predecir el precio del aguacate")
    preguntarValorNumerico(params,"Total de bolsas usadas en la venta","Total Bags","predecir el precio del aguacate")
    Jackie_Habla("Hablame del tipo del aguacate")
    preguntarBool(params,"Tipo de aguacate","type","predecir el precio del aguacate","convencional","orgánico")
    fecha = date.today()
    params["year"] = [2023]
    params["Unnamed: 0"] = 0
    params = pd.DataFrame(params)
    for x in lista_Regiones:
        x = "region_"+x
        params[x] = [0]
    params['month'] = [fecha.month]
    params['Spring'] = params['month'].between(3,5,inclusive='both')
    params['Summer'] = params['month'].between(6,8,inclusive='both')
    params['Fall'] = params['month'].between(9,11,inclusive='both')
    params.Spring = params.Spring.replace({True: 1, False: 0})
    params.Summer = params.Summer.replace({True: 1, False: 0})
    params.Fall = params.Fall.replace({True: 1, False: 0})
    print(PredecirPrecioAguacate(params))
def marketPrediction():
    params = {}
    Jackie_Habla("Haz accedido a la función para predecir el precio de las acciones del mercado SP 500stock, a continuación se preguntaran una variables necesarias para la predicción")
    
    return