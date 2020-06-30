# Project_flask
Proyecto creado en Python usando el microframework flask.

En vez de un maquetado en html se uso bootstrap 4 para facilitar la creacion del proyecto. De igual manera solo lo use de forma sencilla sin muchas modificaciones.

Se creo usando Python 3.8.2 y flask en su versión 1.1.2. Todo este proyecto se empleo unicamente este framework.

Para la utilizacion de la base de datos mysql se hizo mediante flask_sqlalchemy, de manera que toda la información sea guardada allí.

Para el password se empleo werkzeug para que se cifrara el mismo y solo se pueda visualizar el hash.

El login se cada usuario se hizo empleando flask_login.

Para poder realizar el envio del email a cada usuario que se registe se utilizo flask_mail.

De igual manera se empleo la libreria Shell de flask_script, para facilitar las consultas de la base de datos.

Se utilizo flask_migrate para llevar de una forma mas organizada los cambios y que no fuera necesario borrar la base de datos si se desea agregar una nueva casilla ya sea a user o a task.

Para proteger contra los ataques csrf honeypots se empleo flask_wtf.csrf.

Solo se hicieron unas pocas validaciones usando unittest, probablemete mas adelante haga un update sobre ello. 

Por ultimo se uso decouple para realizar la validación del correo mediante una variable de entorno.
