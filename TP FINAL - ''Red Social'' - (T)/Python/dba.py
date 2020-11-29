# import
import mysql.connector

# db config
dbconf={
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'redsocialbd'
}

# class
class DataBase():
    # cnstr
    def __init__(self):
        self.__mydb = mysql.connector.connect(**dbconf)
        self.__cursor = self.__mydb.cursor()
    # mthds
    # gtt
    def get_lastrowid(self):
        return self.__cursor.lastrowid
    def get_mydb(self):
        return self.__mydb
    def get_cursor(self):
        return self.__cursor
    def get_commit(self):
        return self.__mydb.commit()
    # especificos
    def ejecutar(self, qry, val):
        self.__cursor.execute(qry, val)
    def actualizar_auto_increment(self, tab=str, col=str):
        qry = 'SELECT MAX('+col+')+%s FROM '+tab+';'
        val = (1, )
        self.__cursor.execute(qry, val)
        r = self.__cursor.fetchone()[0]
        if r != None:
            qry = 'ALTER TABLE '+tab+' AUTO_INCREMENT = %s;'
            val = (r, )
        else:
            qry = 'ALTER TABLE '+tab+' AUTO_INCREMENT = %s;'
            val = (1, )
        self.__cursor.execute(qry, val)
        self.get_commit()