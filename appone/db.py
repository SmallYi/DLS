import cx_Oracle

connection = None
cursor = None

def connect():
    global connection
    global cursor
    if connection:
        return "duplicate connect"
    try:
        connection = cx_Oracle.connect("system/123456@222.20.73.170/orcl")
    except cx_Oracle.Error as e:
        connection = None
        return "connect error"
    else:
        cursor = connection.cursor()
        return "connect success"

def disconnect():
    global connection
    global cursor
    if connection:
        cursor.close()
        connection.close()
        connection = None
        return "disconnect success"
    else:
        return "disconnect duplicate"
    
def executeSQL(sql):
    cursor.execute(sql)
    return cursor.fetchall()