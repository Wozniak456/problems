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
        connection.autocommit = True  # connection.commit()
        with connection.cursor() as cursor:

            ## ------------------------CREATION AND DATA INSERTION TO [USERS] TABLE------------------------

            # cursor.execute(
            #     """CREATE TABLE users(id serial PRIMARY KEY, first_name VARCHAR(50) NOT NULL, last_name VARCHAR (50)
            #     NOT NULL, email VARCHAR(100));"""
            # )
            # cursor.execute(
            #     """INSERT INTO users(first_name, last_name)
            #     VALUES ('Sofiia', 'Vozniak');"""
            # )
            # cursor.execute(
            #     """INSERT INTO users(first_name, last_name, email)
            #     VALUES ('Karina', 'Dudukchian', 'krasotka@gmail.com'),
            #     ('Anna', 'Mikhnenko', 'simpotiashka@outlook.com'),
            #     ('Anna', 'Sperkach','chertovka2000@gmail.com'),
            #     ('Eduardo','Giga','gmail@gmail.com'),
            #     ('Vasyl','Doroshko', NULL),
            #     ('Markus', 'Strathmann','nemetz@outlook.com'),
            #     ('Oleg','Boiko','boikoboiko@gmail.com') ;"""
            # )

            ## ------------------------CREATION AND DATA INSERTION TO [CATEGORY] TABLE------------------------

            # cursor.execute(
            #     """CREATE TABLE category(id serial PRIMARY KEY, name VARCHAR(50) NOT NULL);"""
            # )
            # cursor.execute(
            #     """INSERT INTO category(name) VALUES ('Food'), ('Clothes'), ('Vacation'), ('Presents'), ('Alcohol'),
            #     ('Utilities'), ('Petrol'); """
            # )

            ## ------------------------CREATION AND DATA INSERTION TO [CURRENCY] TABLE------------------------

            # cursor.execute(
            #     """CREATE TABLE currency(id serial PRIMARY KEY, name VARCHAR(50) NOT NULL);"""
            # )
            # cursor.execute(
            #     """INSERT INTO currency(name) VALUES ('UAH'), ('USD'), ('EUR'), ('PLN'), ('CZK');"""
            # )

            ## ---------------------CREATION AND DATA INSERTION TO [RECORD] TABLE------------------------

            # cursor.execute(
            #     """CREATE TABLE record(id serial PRIMARY KEY, user_id integer REFERENCES users(id),
            #      category_id integer REFERENCES category(id), currency_id integer REFERENCES currency(id),
            #      date DATE NOT NULL, cost money  NOT NULL);"""
            # )
            # cursor.execute(
            #     """INSERT INTO record(user_id, category_id, currency_id, date, cost)
            #     VALUES
            #     (4,1,DEFAULT,'2022-11-10',1000),
            #     (4,2,DEFAULT,'2022-12-15',900),
            #     (4,5,DEFAULT,'2022-12-25',620),
            #     (5,1,3,'2022-08-10',1060),
            #     (5,4,3,'2022-08-10',1300),
            #     (5,6,3,'2022-08-10',3400),
            #     (6,1,4,'2022-10-10',1120),
            #     (6,6,4,'2022-10-10',4500),
            #     (6,7,4,'2022-10-10',2800);"""
            # )
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


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
    return users, category, currency, record
