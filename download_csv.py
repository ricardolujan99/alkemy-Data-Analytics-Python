import requests
import os 
import datetime
import locale
import logging
from decouple import config

#Se establece la localizacion para que los meses aparezcan en español
locale.setlocale(locale.LC_ALL, 'esp_esp')

def downloads_csv():
    #se establecen los parametros para el logging de eventos
    logging.basicConfig(filename='info.log', filemode='a', format='%(levelname)s - %(message)s' , level=logging.INFO)
    
    # se crea una variavle que contiene la fecha y hora actual
    current_time =  datetime.datetime.now().strftime('[%d-%m-%Y %H:%M] ')
 
    #se establecen la url de cada fuente de datos
    URL_CSV_MUSEOS = config('URL_MUSEOS')
    URL_CSV_SALAS_DE_CINE = config('URL_SALAS_DE_CINE')
    URL_CSV_BIBLIOTECAS_POPULARES = config('URL_BIBLIOTECAS_POPULARES')

    #se descargan los archivos csv
    try:
        comtemt_csv_museos = requests.get(URL_CSV_MUSEOS).content
        content_csv_salas_de_cine = requests.get(URL_CSV_SALAS_DE_CINE).content
        content_csv_bibliotecas_populares = requests.get(URL_CSV_BIBLIOTECAS_POPULARES).content
    except requests.ConnectionError:
        print('Error en la conexion a internet')
    except requests.exceptions.HTTPError:
        print('Error al descargar archivo CSV')
        logging.error(current_time +'Error al descargar archivo CSV')

    #se define una funcion para crear los directorios
    def create_folder(folder):
        try:
            os.mkdir(folder)
        except OSError:
            print("El directorio {} ya existe".format(folder) )
            logging.warning(current_time + 'El directorio {} ya existe'.format(folder))
        else:
            print("Se ha creado el directorio: {} ".format(folder))
            logging.info(current_time + 'Se a creado el directorio : {}'.format(folder))


    create_folder('./museos/')
    create_folder('./salas de cine/')
    create_folder('./bibliotecas populares/')
   
   
    current_month = datetime.date.today().strftime('%Y-%B')
    
    folder_museos = "./museos/" + current_month + "/"
    folder_salas_de_cine = "./salas de cine/" + current_month + "/"
    folder_bibliotecas_populares ="./bibliotecas populares/" + current_month + "/"

    create_folder(folder_museos)
    create_folder(folder_salas_de_cine)
    create_folder(folder_bibliotecas_populares)

    curren_time = datetime.date.today().strftime("%Y-%m-%d")
    file_museos = "museos-" + curren_time + '.csv'
    file_salas_de_cine = "salas-de-cine-" + curren_time + '.csv'
    file_bibliotecas_populares = "bibliotecas-populares-" + curren_time + '.csv'

    #se crea una variavle con la ruta de de cada archivo
    route_file_museos = folder_museos + file_museos
    route_file_salas_de_cine = folder_salas_de_cine + file_salas_de_cine
    route_bibliotecas_populares = folder_bibliotecas_populares + file_bibliotecas_populares

    #se crean los archivos csv
    csv_file_museos =  open(route_file_museos, 'wb')
    csv_file_salas_de_cine =  open(route_file_salas_de_cine, 'wb')
    csv_file_bibliotecas_populares =  open(route_bibliotecas_populares, 'wb')
    
    #se escriben los datos en los archivos csv
    csv_file_museos.write(comtemt_csv_museos)
    csv_file_salas_de_cine.write(content_csv_salas_de_cine)
    csv_file_bibliotecas_populares.write(content_csv_bibliotecas_populares)

    #se cierran los archivos csv
    csv_file_museos.close()
    csv_file_salas_de_cine.close()
    csv_file_bibliotecas_populares.close()

    return route_file_museos, route_file_salas_de_cine, route_bibliotecas_populares