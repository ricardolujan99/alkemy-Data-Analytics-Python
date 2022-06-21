from sqlalchemy import create_engine, exc
from sqlalchemy_utils import database_exists, create_database
from decouple import config
import logging 
import datetime

#Funcion para crear la base de datos y tablas
def create_db():
    current_time =  datetime.datetime.now().strftime('[%d-%m-%Y %H:%M] ')
    logging.basicConfig(filename='info.log', filemode='a', format='%(levelname)s - %(message)s' , level=logging.INFO)
    
    engine = create_engine(config('DATABASE_URL'))
    
    if not database_exists(engine.url):
        try:
            create_database(engine.url)
            engine.connect()
            file = open('crear_tablas.sql','r')
            sql = file.read()
            engine.execute(sql)
            print('se a creado la base de datos con exito!')
            logging.info(current_time+"se a creado la base de datos")
        except exc.SQLAlchemyError:
            print("Error al crear la base de datos") 
            logging.error(current_time+'Error al crear la base de datos')
            