import psycopg2
from psycopg2 import Error


class Dbconnect:
    def dbConnection(self):
        try:
            # Conectar a la base de datos
            # print("Intentando conectar a la base de datos...")
            connection = psycopg2.connect(
                user="postgres",
                password="postgres",
                host="127.0.0.1",
                port="5432",
                database="training"
            )

            cursor = connection.cursor()

            return connection, cursor

        except psycopg2.Error as error:
            print("Error while connecting to PostgreSQL:", error)
            return None, None
