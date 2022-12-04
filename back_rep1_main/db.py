import psycopg2
from back_rep1_main.configDB import host, user, password, db_name

def db_init():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    try:
        # connection.autocommit = True
        print("succesfull entry")
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM users;"""
            )
            users = cursor.fetchall()

            cursor.execute(
                """SELECT * FROM category;"""
            )
            category = cursor.fetchall()

            cursor.execute(
                """SELECT * FROM currency;"""
            )
            currency = cursor.fetchall()

            cursor.execute(
                """SELECT * FROM record;"""
            )
            record = cursor.fetchall()

            cursor.execute(
                """INSERT INTO users(first_name, last_name)
                    VALUES ('Masha', 'Petrovjjjj'); """
            )
            #connection.commit()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
    return users, category, currency, record

