import pandas as pd 
from download_csv import downloads_csv
from create_db import create_db
from sqlalchemy import create_engine , exc
from decouple import config
import logging
import datetime

# se crea una variavle que contiene la fecha y hora actual
current_time =  datetime.datetime.now().strftime('[%d-%m-%Y %H:%M] ')

#se establecen los parametros para el logging de eventos
logging.basicConfig(filename='info.log', filemode='a', format='%(levelname)s - %(message)s' , level=logging.INFO)

#se comprueba si existe la base de datos de no ser asi se crea la misma
create_db()


engine = create_engine(config('DATABASE_URL'))

#se descarga los archivos csv
files_names = downloads_csv()

#se abren los archivos csv
df_museos = pd.read_csv(files_names[0] )
df_salas_de_cine = pd.read_csv(files_names[1])
df_bibliotecas_populares = pd.read_csv(files_names[2])

df_salas_de_cine_cantidades = df_salas_de_cine.groupby(["Provincia"],as_index=False)[["Pantallas",'Butacas','espacio_INCAA']].count()


#se renombran las columnas necesarias para que cumplan con los requisitos del desafio
df_museos.rename(
    columns={
    'Cod_Loc' : 'cod_localidad',
    'IdProvincia': 'id_provincia',
    'IdDepartamento': 'id_departamento',
    'categoria' : 'Categoría',
    'provincia' : 'Provincia',
    'localidad' : 'Localidad',
    'nombre': 'Nombre',
    'CP':'Código postal',
    'telefono' : 'Número de teléfono',
    },inplace=True
    )

df_salas_de_cine.rename(
    columns={
    'Cod_Loc' : 'Cod_localidad',
    'IdProvincia' : 'Id_provincia',
    'IdDepartamento'  : 'Id_departamento',
    'CP': 'Código postal',
    'Teléfono' : 'Número de teléfono',
    },inplace=True
    )

df_bibliotecas_populares.rename(
    columns={
    'Cod_Loc' : 'Cod_localidad',
    'IdProvincia' : 'Id_provincia',
    'IdDepartamento'  : 'Id_departamento',
    'CP': 'Código postal',
    'Teléfono' : 'Número de teléfono',
    },inplace=True
    )


#se un unico dataframe con el contenido de las tres fuentes de datos
df_completo = pd.concat([df_museos, df_salas_de_cine, df_bibliotecas_populares], axis=0)



registros_totales_por_categoria = df_completo.groupby(["Categoría"] ,as_index=True )[['Categoría']].size().to_frame(name = 'Total por categoria' )
registros_totales_por_fuente = df_completo.groupby(["fuente"] ,as_index=True )[['fuente']].size().to_frame(name = 'Total por fuente' )
registros_por_provincia_y_categoria = df_completo.groupby(["Provincia","Categoría"], as_index=True )[['Categoría']].size().to_frame(name = 'Total por provincia y categoria' )
#se crea una tabla con los registros totales
registros_totoales = pd.concat([registros_totales_por_categoria, registros_totales_por_fuente, registros_por_provincia_y_categoria], axis=0 ).reset_index()



#se conservan solo las columnas necesarias en el dataframe
df_completo = df_completo[[
    'Cod_localidad',
    'Id_provincia',
    'Id_departamento',
    'Categoría',
    'Provincia',
    'Localidad',
    'Nombre',
    'Domicilio',
    'Código postal',
    'Número de teléfono',
    'Mail',
    'Web',
    ]]



#se agrega una columna con la fecha y hora actual 
df_salas_de_cine_cantidades['Fecha y hora registro'] = current_time
registros_totoales['Fecha y hora registro'] = current_time
df_completo['Fecha y hora registro'] = current_time


#se cargan los datos a la base de datos
try:
    with engine.begin() as conn:
        df_salas_de_cine_cantidades.to_sql('datos_salas_de_cine', conn, if_exists='replace', index = False)
        registros_totoales.to_sql('registros_totoales', conn, if_exists='replace', index = False)
        df_completo.to_sql('tabla_completa', conn, if_exists='replace', index = False)
        print("la base de datos se a actualizado con exito!")
        logging.info(current_time + 'la base de datos se a actualizado con exito!.')
except exc.SQLAlchemyError:
        print("Error al actualizar la tabla base de datos.")
        logging.error(current_time + 'Error al actualizar la base de datos. ' )


