# importar la conexion a la base de datos, que viene en el modulo de PyMySQL
from pymysql import connect

class Database:
    def __init__(self):
        self.connection:any = connect(
            host= 'localhost', # host localhost es cuando esta en la misma computadora, se puede poner una ip si es que se va a conectar a un servidor
            user= 'python_user', # el nombre del usuario de la base de dato
            passwd= 'python_123', # la contrasenia del usuario de la base de dato
            database= 'python_mysql' # el nombre de la base de dato a la cual no vamos a conectar
        )
        self.cursor:any = self.connection.cursor() # el cursor no ayuda a ejecutar las consultas(queries) a la base de datos


"""
Para crear base de datos
    > create database python_mysql;
Para usar la base de datos
    > use python_mysql;
Para crear la tabla
    > create table user (
        id int auto_increment not null primary key,
        name varchar(60) not null,
        firstname varchar(60) not null,
        lastname varchar(60) not null,
        phonenumber varchar(10),
        email varchar(60) not null unique,
        password varchar(17) not null
    );

Para crear un usuario en mysql
    > create user 'python_user'@'localhost' identified by 'python_123';
Darle los privilegios para la base de datos
    > grant all privileges on python_mysql.* to 'python_user'@'localhost';
Para que los privilegios tenga efectos
    > flush privileges;
Para eliminar un usuario opcional
    > drop user 'python_user'@'localhost';
"""