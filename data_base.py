import psycopg2
from environs import Env

class Database():
    
    def connectionDB(self):
        env = Env()
        env.read_env()
        try:
            self.connection = psycopg2.connect(
                dbname=env('POSTGRES_DATABASE'),
                user=env('POSTGRES_USER'),
                password=('POSTGRES_PASSWORD'),
                host=env('POSTGRES_HOST')
            )
        except:
            print ('ERROR AL CONECTAR')

    def list_of_elements(self):

        cursor= self.connection.cursor()
        cursor.execute ("""SELECT * FROM products;""")
        fet=cursor.fetchall()
        return fet

    def list_by_name(self,name_product):

        cursor= self.connection.cursor()
        cursor.execute (f"""SELECT * FROM products WHERE name = {name_product} ;""")
        fet=cursor.fetchall()
        return fet
    
db = Database()
db.connectionDB()
db.list_of_elements('hola')