import psycopg2
from environs import Env



def connectionDB():
    env = Env()
    env.read_env()
    try:
        return psycopg2.connect(
            dbname=env('POSTGRES_DATABASE'),
            user=env('POSTGRES_USER'),
            password=('POSTGRES_PASSWORD'),
            host=env('POSTGRES_HOST')
        )
    except:
        print ('ERROR AL CONECTAR')

def list_of_elements():

    connection=connectionDB
    cursor= connection.cursor()
    cursor.execute ("""SELECT * FROM products;""")
    fet=cursor.fetchall()
    return fet

def list_by_name(name_product):
    connection=connectionDB
    cursor= connection.cursor()
    cursor.execute (f"""SELECT * FROM products WHERE name = {name_product} ;""")
    fet=cursor.fetchall()
    return fet
