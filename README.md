
# solo es una conexion a base de datos que es para ejemplo
se usaron una entidad, y tabla (conexion a la base de datos para usar dicha tabla)
luego le hare una interfaz para prueba, primero en consola.

pip es un modulo que nos permite instalar diferentes modulos que usamos o usaremos
-m viene de modulo, y luego va el nombre del modulo

Para usar entorno virtual, de mi parte uso lo que es virtualenv
>> py -m pip install virtualenv
o
>> python -m pip install virtualenv
o tambien
>> pip install virtualenv

para crear el entorno virtual, (modulo nombre_del_entorno)
>> py -m venv env
o
>> virtualenv env

para correr el entorno virtual en window
>> .\env\Scripts\activate

para desactivar el entorno virtual en window
>> .\env\Scripts\deactivate.bat

el archivo de requirements.txt es para ver los modulos que ocupamos en el entorno virtual
para generar este archivo
>> py -m pip freeze > requirements.txt
o
>> python -m pip freeze > requirements.txt
o
>> freeze > requirements.txt

para instalar los requerimientos del archivo de requirements.txt
>> pip install -r .\requeriments.txt
