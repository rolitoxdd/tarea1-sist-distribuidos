import psycopg2
from environs import Env


class Database:
    def __init__(self) -> None:
        self.conn = False
        pass

    def connectionDB(self):
        env = Env()
        env.read_env()
        #
        if self.conn:
            return self.conn
        else:
            self.conn = psycopg2.connect(
                dbname=env('POSTGRES_DATABASE'),
                user=env('POSTGRES_USER'),
                password=env('POSTGRES_PASSWORD'),
                host=env('POSTGRES_HOST')
            )
            return self.conn

    def list_of_elements(self):
        cursor = self.connectionDB().cursor()
        cursor.execute("""SELECT * FROM products;""")
        fet = cursor.fetchall()
        return fet

    def list_by_name(self, name_product):

        cursor = self.connectionDB().cursor()
        cursor.execute(
            f"""SELECT * FROM products WHERE name = {name_product} ;""")
        fet = cursor.fetchall()
        return fet
