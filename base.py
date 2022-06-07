import sqlite3
from datetime import datetime, timedelta
from config import BASE_NAME


def work():
    sqlite_connection = sqlite3.connect(BASE_NAME)
    cursor = sqlite_connection.cursor()
    return cursor, sqlite_connection


def all_classes():
    cursor, con = work()
    try:
        sql = "SELECT * FROM classes"
        cursor.execute(sql)

        res = cursor.fetchall()
        cursor.close()
        return res
    except Exception as e:
        print(e)
        return None


def isReg(user_id):
    cursor, con = work()
    try:
        sql = f"SELECT * FROM telegram WHERE telegram_id = {user_id}"
        cursor.execute(sql)

        res = cursor.fetchall()
        if res:
            return True
        else:
            return False
        cursor.close()
    except Exception as e:
        print(e)
        return None

def isUserExists(full_name):
    cursor, con = work()
    try:
        print(full_name)
        sql = f'SELECT * FROM students WHERE full_name = "{full_name}"'
        cursor.execute(sql)

        res = cursor.fetchall()

        if res:
            return True
        else:
            return False
        cursor.close()
    except Exception as e:
        print(e)
        return None


def isKeyExists(key):
    cursor, con = work()
    try:
        sql = f'SELECT * FROM codes WHERE key_code = {key}'
        cursor.execute(sql)

        res = cursor.fetchall()

        if res:
            return True
        else:
            return False
        cursor.close()
    except Exception as e:
        print(e)
        return None



def add_user(full_name, telegram_id):
    cursor, con = work()
    try:
        sql = f'SELECT id FROM students WHERE full_name = "{full_name}"'
        cursor.execute(sql)
        student_id = cursor.fetchall()[0][0]
        print(student_id)
        if not student_id:
            return None
        sql = f"INSERT INTO telegram VALUES ({student_id}, {telegram_id})"
        cursor.execute(sql)
        con.commit()
        return True

        cursor.close()

    except Exception as e:
        print(e)
        return None


def add_key(key, full_name):
    cursor, con = work()
    try:
        sql = f'SELECT id FROM classes WHERE id = (SELECT class_id FROM students WHERE full_name = "{full_name}")'
        cursor.execute(sql)
        class_id = cursor.fetchall()[0][0]
        print(class_id)
        if not class_id:
            return None
        sql = f"INSERT INTO codes VALUES ({key}, {class_id})"
        cursor.execute(sql)
        con.commit()
        return True

        cursor.close()

    except Exception as e:
        print(e)
        return None


def get_link_from_name(full_name):
    cursor, con = work()
    try:
        sql = f'SELECT link FROM classes WHERE id = (SELECT class_id FROM students WHERE full_name = "{full_name}")'
        cursor.execute(sql)
        res = cursor.fetchall()[0][0]
        cursor.close()
        return res

        cursor.close()

    except Exception as e:
        print(e)
        return None