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
        try:
            cursor.close()
            connection.close()
            cursor = None
            connection = None
            return 0
        except cx_Oracle.Error as e:
            print(e)
            return -1
    else:
        return 1
    
def executeSQL(sql):
    if connection:
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except cx_Oracle.Error as e:
            print(e)
            return None
    else:
        return None

def executeSQL2(sql):
    if connection:
        try:
            cursor.execute(sql)
            connection.commit()
            return 0
        except cx_Oracle.Error as e:
            print(e)
            return -1
    else:
        return -1