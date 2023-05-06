from SpeechAndTalk import * 
import re 
import numpy as np
from collections import Counter
from sklearn.preprocessing import StandardScaler
def Standard_Scaler (df, col_names):
    features = df[col_names]
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)
    df[col_names] = features
    return df
def IQR_method (df,n,features):
    """
    Takes a dataframe and returns an index list corresponding to the observations 
    containing more than n outliers according to the Tukey IQR method.
    """
    outlier_list = []
    
    for column in features:
                
        # 1st quartile (25%)
        Q1 = np.percentile(df[column], 25)
        # 3rd quartile (75%)
        Q3 = np.percentile(df[column],75)
        
        # Interquartile range (IQR)
        IQR = Q3 - Q1
        
        # outlier step
        outlier_step = 1.5 * IQR
        
        # Determining a list of indices of outliers
        outlier_list_column = df[(df[column] < Q1 - outlier_step) | (df[column] > Q3 + outlier_step )].index
        
        # appending the list of outliers 
        outlier_list.extend(outlier_list_column)
        
    # selecting observations containing more than x outliers
    outlier_list = Counter(outlier_list)        
    multiple_outliers = list( k for k, v in outlier_list.items() if v > n )
    
    # Calculate the number of records below and above lower and above bound value respectively
    df1 = df[df[column] < Q1 - outlier_step]
    df2 = df[df[column] > Q3 + outlier_step]
    
    print('Total number of deleted outliers:', df1.shape[0]+df2.shape[0])
    
    return multiple_outliers
def preguntarValorNumerico(datos,variablePreguntada,nombreDataset,contexto):
    respuesta_jackie ="Ahora, dime que valor le das a: " + variablePreguntada
    Jackie_Habla(respuesta_jackie)
    while True:
        escucha = jackie_Escucha()
        valor = re.sub(r'[^0-9.,]', '', escucha)
        valor = valor.replace(",",".")
        if valor == "":
            respuesta_jackie = "Perdona, no entendí eso, puedes repetirme el valor de " + variablePreguntada
            Jackie_Habla(respuesta_jackie)
        elif ("cancelar" in escucha):
            respuesta_jackie = "Cancelando Función de predecir " + contexto
            Jackie_Habla(respuesta_jackie)
            break
        else:
            datos[nombreDataset] = [float(valor)]
            respuesta_jackie = "valor de " + variablePreguntada + "confirmado de: " + str(valor)
            Jackie_Habla(respuesta_jackie)
            break
def preguntarBool(datos,variablePreguntada,nombreDataset,contexto,variableTrue,variableFalse):
    respuesta_jackie = "Dime si es " + variableTrue + "o es "+ variableFalse
    Jackie_Habla(respuesta_jackie)
    while True:
        escucha = jackie_Escucha()
        if ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de "+ contexto)
            break
        elif variableTrue in escucha or "si" in escucha:
            datos[nombreDataset] = [1]
            respuesta_jackie = "tipo confirmado como " + variableTrue
            Jackie_Habla(respuesta_jackie)
            break
        elif variableFalse in escucha or "no" in escucha: 
            datos[nombreDataset] = [0]
            respuesta_jackie = "tipo confirmado como " + variableFalse
            Jackie_Habla(respuesta_jackie)
            break
        elif variableFalse in escucha and variableTrue in escucha: 
            respuesta_jackie = "Perdona, no entendí eso, puedes repetirme el " + variablePreguntada
            Jackie_Habla(respuesta_jackie)
        else:
            respuesta_jackie = "Perdona, no entendí eso, puedes repetirme el " + variablePreguntada
            Jackie_Habla(respuesta_jackie)
def preguntarCategoria(datos,variablePreguntada,nombreDataset,contexto,lista):
    listaValores = [s.lower() for s in lista]
    respuesta_jackie = "Dime si el " + variablePreguntada + " es "
    for x in listaValores:
        respuesta_jackie = respuesta_jackie + " " + x
    Jackie_Habla(respuesta_jackie)
    counter = 0
    while True:
        escucha = jackie_Escucha()
        print(escucha)
        if ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de "+ contexto)
            break
        elif any(item in escucha for item in listaValores):
            f = False
            for c in listaValores:
                if (c in escucha):
                    datos[nombreDataset] = [counter]
                    respuesta_jackie = "Se le ha asignado el valor de " + c + " a " + variablePreguntada
                    print(counter) 
                    Jackie_Habla(respuesta_jackie)
                    f = True
                    break
                counter += 1
            if f:
                break
        else:
            respuesta_jackie = "Perdona, no entendí eso, puedes repetirme el " + variablePreguntada
            Jackie_Habla(respuesta_jackie)
    return
def preguntarCategoriaCiudad(datos,variablePreguntada,nombreDataset,contexto,lista):
    listaValores = [s.lower() for s in lista]
    respuesta_jackie = "Dime si el " + variablePreguntada + " es "
    for x in listaValores:
        respuesta_jackie = respuesta_jackie + " " + x
    Jackie_Habla(respuesta_jackie)
    counter = 0
    while True:
        escucha = jackie_Escucha()
        print(escucha)
        if ("cancelar" in escucha):
            Jackie_Habla("Cancelando Función de "+ contexto)
            break
        elif any(item in escucha for item in listaValores):
            f = False
            for c in listaValores:
                if (c in escucha):
                    nombreDataset = nombreDataset
                    datos[nombreDataset] = [counter]
                    respuesta_jackie = "Se le ha asignado el valor de " + c + " a " + variablePreguntada
                    print(counter) 
                    Jackie_Habla(respuesta_jackie)
                    f = True
                    break
                counter += 1
            if f:
                break
        else:
            respuesta_jackie = "Perdona, no entendí eso, puedes repetirme el " + variablePreguntada
            Jackie_Habla(respuesta_jackie)
    return
