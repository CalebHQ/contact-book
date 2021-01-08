import mysql.connector

# mycursor.execute('CREATE DATABASE ContactBook')
# mycursor.execute("CREATE TABLE Contact (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, fname varchar(50) NOT NULL, lname varchar(50), phone int NOT NULL, email varchar(50), address varchar(50), suburb varchar(50), postcode int, state varchar(50), country varchar(50), relationship varchar(50))")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="contactbook"
)

mycursor = db.cursor()


def create_contact(fname, lname, phone, email, address, suburb, postcode, state, country, relationship):
    try:
        mycursor.execute("INSERT INTO Contact (fname, lname, phone, email, address, suburb, postcode, state, country, relationship) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (fname, lname, phone, email, address, suburb, postcode, state, country, relationship))
        db.commit()
    except (Exception, mysql.connector.Error) as error:
        print(error)


def update_contact(column, value, id):
    try:
        mycursor.execute(
            f"UPDATE Contact SET {column} = '" + value + "' WHERE id = '" + id + "'")
        db.commit()
    except (Exception, mysql.connector.Error) as error:
        print(error)


def delete_contact(column, value):
    try:
        mycursor.execute(
            f"DELETE FROM Contact WHERE {column} = '" + value + "'")
        db.commit()
        print(mycursor.rowcount, "record(s) affected")
    except (Exception, mysql.connector.Error) as error:
        print(error)


def select_all():
    data = []
    try:
        mycursor.execute("SELECT * FROM Contact")
        for x in mycursor:
            data.append(x)
        return data
    except (Exception, mysql.connector.Error) as error:
        print(error)


def select_name(name):
    data = []
    try:
        mycursor.execute(f"SELECT * FROM Contact WHERE fname = '{name}'")
        for x in mycursor:
            data.append(x)
        return data
    except (Exception, mysql.connector.Error) as error:
        print(error)


# mycursor.execute('SELECT * FROM Contact')
# for x in mycursor:
#     print(x)
