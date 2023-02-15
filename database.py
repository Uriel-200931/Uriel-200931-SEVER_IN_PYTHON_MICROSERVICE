import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
        host="localhost",
            port=3307,
            user="root",
            password="1234",
            database="api_shop"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def close_connection(connection):
    if connection:
        connection.close()
        print("MySQL connection is closed")


def get_suppliers():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    select_query = "SELECT * FROM shop"
    cursor.execute(select_query)
    suppliers = cursor.fetchall()

    close_connection(connection)
    return suppliers


def get_supplier(supId):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    select_query = "SELECT * FROM shop WHERE supId = %s"
    cursor.execute(select_query, (supId,))
    supplier = cursor.fetchone()

    close_connection(connection)
    return supplier


def create_supplier(supplier):
    connection = create_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO shop (supName, supLastName, adress, phoneNumber, shopId) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (supplier["supName"], supplier["supLastName"], supplier["adress"], supplier["phoneNumber"], supplier["shopId"]))
    connection.commit()

    close_connection(connection)


def update_supplier(supId, supplier):
    connection = create_connection()
    cursor = connection.cursor()

    update_query = "UPDATE shop SET supName=%s, supLastName=%s, adress=%s, phoneNumber=%s, shopId=%s WHERE supId = %s"
    cursor.execute(update_query, (supplier["supName"], supplier["supLastName"], supplier["adress"], supplier["phoneNumber"], supplier["shopId"], supId))
    connection.commit()

    close_connection(connection)


def delete_supplier(supId):
    connection = create_connection()
    cursor = connection.cursor()

    delete_query = "DELETE FROM shop WHERE supId = %s"
    cursor.execute(delete_query, (supId,))
    connection.commit()

    close_connection(connection)


""" import mysql.connector

mydb = mysql.connector.connect(
  host="3307",
  user="root",
  password="1234",
  database="api_shop"
)
 """