import cx_Oracle

class oracle(object):
    def __init__(self):
        self.__conn = cx_Oracle.connect("system/123456@192.168.1.31/orcl")
        self.__cursor = self.__conn.cursor()
    def __del__(self):
        self.__cursor.close()
        self.__conn.close()
    def select(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()
    def alter(self, sql):
        self.__cursor.execute(sql)
        self.__conn.commit()
