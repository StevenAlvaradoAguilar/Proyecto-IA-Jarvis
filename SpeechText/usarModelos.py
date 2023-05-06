import numpy
import pickle
import pandas as pd
#Se abren los modelos 
def predecirInventarioCompañía(pruebaModelo):
    with open('./Modelos/cantidad_de_inventario_de_la_compañía.sav' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def predecirAccionesMercado(pruebaModelo):
    with open('./Modelos/precio_acciones_del_mercado.sav' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirPrecioVino(pruebaModelo):
    with open('./Modelos/WineModel_pkl' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirTipoHepatitis(pruebaModelo):
    with open('./Modelos/hepatitis_SVM_Model' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirTipoCirrosis(pruebaModelo):
    with open('./Modelos/Cirrosis_RF_pkl' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirAccidenteCerebroVascular(pruebaModelo):
    with open('./Modelos/StrockPredict_RF_Model_pkl' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirTarifaBicicleta(pruebaModelo):
    with open('./Modelos/tarifa_viaje_bicicleta.pkl' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirPacientesCovid19(pruebaModelo):
    with open('./Modelos/cantidad_de_paciente_recuperados_de_covid19.sav' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirPrecioAguacate(pruebaModelo):
    with open('./Modelos/precio_aguacate.pkl' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res
def PredecirGrasaCorporal(pruebaModelo):
    with open('./Modelos/masa_corporal.pkl' , 'rb') as f:
        model = pickle.load(f)
    params = pd.DataFrame(pruebaModelo)
    res = model.predict(params)
    return res