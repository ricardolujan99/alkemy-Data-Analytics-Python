import requests
import os 
import datetime
import locale
import logging
locale.setlocale(locale.LC_ALL, 'esp_esp')

def downloads_csv():
    #se establecen los parametros para el logging de eventos
    logging.basicConfig(filename='info.log', filemode='a', format='%(levelname)s - %(message)s' , level=logging.INFO)
    
    # se crea una variavle que contiene la fecha y hora actual
    current_time =  datetime.datetime.now().strftime('[%d-%m-%Y %H:%M] ')
    
    #se establecen la url de cada fuente de datos
    URL_CSV_MUSEOS = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
    URL_CSV_SALAS_DE_CINE = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
    URL_CSV_BIBLIOTECAS_POPULARES = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'

    #se descargan los archivos csv
    try:
        CONTENT_CSV_MUSEOS = requests.get(URL_CSV_MUSEOS).content
        CONTENT_CSV_SALAS_DE_CINE = requests.get(URL_CSV_SALAS_DE_CINE).content
        CONTENT_CSV_BIBLIOTECAS_POPULARES = requests.get(URL_CSV_BIBLIOTECAS_POPULARES).content
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
            print("Error al crear el directorio {} ".format(folder) )
            logging.warning(current_time + 'Error al crear el directorio : {}'.format(folder))
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
    CSV_FILE_MUSEOS =  open(route_file_museos, 'wb')
    CSV_FILE_SALAS_DE_CINE =  open(route_file_salas_de_cine, 'wb')
    CSV_FILE_BIBLIOTECAS_POPULARES =  open(route_bibliotecas_populares, 'wb')
    
    #se escriben los datos en los archivos csv
    CSV_FILE_MUSEOS.write(CONTENT_CSV_MUSEOS)
    CSV_FILE_SALAS_DE_CINE.write(CONTENT_CSV_SALAS_DE_CINE)
    CSV_FILE_BIBLIOTECAS_POPULARES.write(CONTENT_CSV_BIBLIOTECAS_POPULARES)

    #se cierran los archivos csv
    CSV_FILE_MUSEOS.close()
    CSV_FILE_SALAS_DE_CINE.close()
    CSV_FILE_BIBLIOTECAS_POPULARES.close()

    return route_file_museos, route_file_salas_de_cine, route_bibliotecas_populares