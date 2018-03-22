import cx_Oracle

connection = None
cursor = None

def connect():
    global connection
    global cursor
    if connection:
        return 1
    try:
        connection = cx_Oracle.connect("system/123456@222.20.72.194/orcl")
    except cx_Oracle.Error as e:
        connection = None
        print(e)
        return -1
    else:
        cursor = connection.cursor()
        return 0

def disconnect():
    global connection
    global cursor
    if connection:
        cursor.close()
        connection.close()
        connection = None
        return 0
    else:
        return 1
    
def executeSQL(sql):
    if connection:
        cursor.execute(sql)
        return cursor.fetchall()
    else:
        raise cx_Oracle.Error("Hey!Hava you connected to DB?")

def executeSQL2(sql):
    if connection:
        cursor.execute(sql)
        return
    else:
        raise cx_Oracle.Error("Hey!Hava you connected to DB?")