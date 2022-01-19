from mysql.connector import connect, Error


class MysqlContext:

    DB_NAME = 'schema'
    DB_SENHA = 'senha'
    DB_USER = 'user'
    DB_HOST = 'db'
    DB_LOCAL = 'localhost'

    def mysql_connection(self):
        try:
            connection = connect(host=self.DB_HOST,
                                 database=self.DB_NAME,
                                 user=self.DB_USER,
                                 password=self.DB_SENHA)
        except Error as ex:
            try:
                connection = connect(host=self.DB_LOCAL,
                                     database=self.DB_NAME,
                                     user=self.DB_USER,
                                     password=self.DB_SENHA)
            except Exception as error:
                raise error
        return connection

    @staticmethod
    def mysql_close_connection(cursor, conn):
        if conn.is_connected():
            cursor.close()
            conn.close()

