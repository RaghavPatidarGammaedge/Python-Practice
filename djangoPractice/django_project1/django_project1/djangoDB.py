import psycopg2

class ConnectionProvider:
    def __init__(self):
        self.__conn=psycopg2.connect("host=localhost dbname=djangoDatabase user=rghv password=rghv")
        self.__cursor=self.__conn.cursor()
        self.__cursor.execute("create table if not exists users (name text primary key, password text)")
        self.__conn.commit()

    def getConnection(self):
        return self.__conn

    def __del__(self):
        self.__conn.close()