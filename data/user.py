# solo por aburrimiento lo separe
from data.db import Database
# se creo la entidad usuario para ser un poco mas ordenado
from entities.user import User

# instancie la conexion a la base de datos por que no me acuerdo de la herencia como es que se usa
db = Database()

class UserDB:
    def __init__(self):
        self.connection:any = db.connection
        self.cursor:any = db.cursor

    # obtener el ultimo id para cuando se crea el primero que no sabemos el id, y tambien los demas ya que no es necesario manda el id ya que este es
    # autoincrementable
    def select_last_id(self):
        sql = 'SELECT id FROM user ORDER BY id DESC LIMIT 1;'
        try: # tratar si no hay error
            self.cursor.execute(sql) # el cursor ejecuta la consulta
            id = self.cursor.fetchone() # ya que es solo una fila se procesa con fecthone
            return id[0] # ya que nos devuelve una tupla, solo le ponemos la posicion para retornar el valor
        except Exception as e: # si hay error
            print('An error has occurred: ',e) # manda la alerta


    def select_users(self):
        sql = f'SELECT id, name, firstname, lastname, phonenumber, email, password FROM user;'
        try: # tratar si no hay error
            self.cursor.execute(sql) # el cursor ejecuta la consulta
            users = self.cursor.fetchall() # ya que mandamos a llamar mas de un registro, se debe procesar con fetchall
            for user in users:
                print('Id: ',user[0])
                print('Name: ',user[1])
                print('Firstname: ',user[2])
                print('lastname: ',user[3])
                print('Phonenumber: ',user[4])
                print('Email: ',user[5])
                print('Password: ',user[6])
                print('______________________________\n')
        except Exception as e: # si hay error
            print('An error has occurred: ',e) # manda la alerta


    def select_user(self, id:int):
        sql = f'SELECT id, name, firstname, lastname, phonenumber, email, password FROM user WHERE id={id};'
        try: # tratar si no hay error
            self.cursor.execute(sql) # el cursor ejecuta la consulta
            user = self.cursor.fetchone() # ya que es solo una fila se procesa con fecthone
            print('Id: ',user[0])
            print('Name: ',user[1])
            print('Firstname: ',user[2])
            print('lastname: ',user[3])
            print('Phonenumber: ',user[4])
            print('Email: ',user[5])
            print('Password: ',user[6])
            print('______________________________\n')
        except Exception as e: # si hay error
            print('An error has occurred: ',e) # manda la alerta


    def insert_user(self, user:User):
        sql = f'INSERT INTO user(id, name, firstname, lastname, phonenumber, email, password) VALUES ({user.id}, "{user.name}", "{user.firstname}", "{user.lastname}", "{user.phonenumber}", "{user.email}", "{user.password}")'
        try: # tratar si no hay error
            self.cursor.execute(sql) # el cursor ejecuta la consulta
            self.connection.commit() # el commit es para hacer que los cambios en la base de datos se haga permanentes
            print('registration was successful!\n') # manda la alerta de todo salio bien
        except Exception as e: # si hay error
            print('An error has occurred: ',e) # manda la alerta


    def update_user(self, id:int, user:User):
        sql=f'UPDATE user SET name="{user.name}", firstname="{user.firstname}", lastname="{user.lastname}", phonenumber="{user.phonenumber}", email="{user.email}", password="{user.password}" WHERE id={id};'
        try: # tratar si no hay error
            self.cursor.execute(sql) # el cursor ejecuta la consulta
            self.connection.commit() # el commit es para hacer que los cambios en la base de datos se haga permanentes
            print('The change was successful!\n') # manda la alerta de todo salio bien
        except Exception as e: # si hay error
            print('An error has occurred: ',e) # manda la alerta


    def delete_user(self, id:int):
        sql = f'DELETE FROM user WHERE id={id};'
        try: # tratar si no hay error
            self.cursor.execute(sql) # el cursor ejecuta la consulta
            self.connection.commit() # el commit es para hacer que los cambios en la base de datos se haga permanentes
            print('The user was successful removed!\n') # manda la alerta de todo salio bien
        except Exception as e: # si hay error
            print('An error has occurred: ',e) # manda la alerta


    def close_connection(self) -> None:
        self.connection.close()