import cx_Oracle

connection = None
cursor = None

def connect():
    global connection
    global cursor
    if connection:
        return 1
    try:
        connection = cx_Oracle.connect("system/123456@222.20.73.170/orcl")
    except cx_Oracle.Error as e:
        connection = None
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
    cursor.execute(sql)
    return cursor.fetchall()