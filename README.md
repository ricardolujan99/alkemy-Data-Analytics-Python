# alkemy-Data-Analytics-Python


# guia para hacer funcionar el proyecto:

1. para comenzar asumiendo de que ya tiene instalado en su sistema python y pip el primer paso sera ejecutar el siguiente comando:
 
    ```pip install virtualenv```

2. una vez se haya terminado la instalacion de virtualenv, ejecutar el siguiente comando: 
 
    ```virtualenv alkemy```

3. teniendo el entorno virtual ya creado tenemos que activarlo, para lograr hay que ejecutar los siguientes comandos:
 
 
    ```
    cd ./alkemy/scripts
    activate
    cd ../ 
    ```

    
4. con el entorno virtual ya activado es necesario instalar todas los paquetes necesarios para que el proyecto funcione, para poder instalarlos se debe ejectuar el siguiente comando:
  
   ```pip install -m requeriments.txt```
    
5. taniendo el entorno virtual activado y los paquetes necesarios ya instalados el siguiente paso antes de poder ejecutar el proyecto es el de instalar el servidor postgresql para la base de datos, esto lo podemos lograr de dos formas, una es instalando el servidor postgresql en nuestro sistema y la otra es utilizando docker, a continuacion en forma de guia se adjuntan dos videos tutoriales: 
    
 - instalar postgresql en su sistema:
 
   https://www.youtube.com/watch?time_continue=691&v=RgP1njsQO0g&feature=emb_logo

 - utilizar postgresql con docker :
 
   https://www.youtube.com/watch?v=0ACd1_mo-dI
  
6. taniendo ya postgresql funcionando ya podemos ejecutar el proyecto para lograrlo hay que ejecutar el siguiente comando:

   ```py procesar_datos.py```
   
7. En casi de ser necesario configurar el nombre de usuario o contraseña de postgresql lo podemos hacer desde el siguiente archivo:
  
  
  ```py settings.ini```
  
