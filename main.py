from fastapi import FastAPI
from fastapi import HTTPException
from database import get_suppliers, get_supplier, create_supplier, update_supplier, delete_supplier


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/suppliers")
async def read_suppliers():
    suppliers = get_suppliers()
    if suppliers is None:
        raise HTTPException(status_code=404, detail="Suppliers not found")
    return suppliers


@app.get("/supplier/{supId}")
async def read_supplier(supId: int):
    supplier = get_supplier(supId)
    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


@app.post("/supplier")
async def create_new_supplier(supplier: dict):
    create_supplier(supplier)
    return {"detail": "Supplier created successfully"}


@app.put("/supplier/{supId}")
async def update_existing_supplier(supId: int, supplier: dict):
    existing_supplier = get_supplier(supId)
    if existing_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    update_supplier(supId, supplier)
   


""" 
from fastapi import FastAPI
from typing import List
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# Conexión a la base de datos
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="api_shop"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
        
# Obtener todos los registros de la tabla shop
@app.get("/shop", response_model=List[Shop])
def read_shop():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM shop")
    result = cursor.fetchall()
    return result

# Obtener un registro de la tabla shop por su ID
@app.get("/shop/{shop_id}", response_model=Shop)
def read_shop_by_id(shop_id: int):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM shop WHERE supId = %s", (shop_id,))
    result = cursor.fetchone()
    return result

# Crear un nuevo registro en la tabla shop
@app.post("/shop", response_model=Shop)
def create_shop(shop: Shop):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    query = "INSERT INTO shop (supName, supLastName, address, phoneNumber, shopId) VALUES (%s, %s, %s, %s, %s)"
    values = (shop.supName, shop.supLastName, shop.address, shop.phoneNumber, shop.shopId)
    cursor.execute(query, values)
    connection.commit()
    shop.supId = cursor.lastrowid
    return shop

# Actualizar un registro existente en la tabla shop por su ID
@app.put("/shop/{shop_id}", response_model=Shop)
def update_shop(shop_id: int, shop: Shop):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    query = "UPDATE shop SET supName=%s, supLastName=%s, address=%s, phoneNumber=%s, shopId=%s WHERE supId=%s"
    values = (shop.supName, shop.supLastName, shop.address, shop.phoneNumber, shop.shopId, shop_id)
    cursor.execute(query, values)
    connection.commit()
    shop.supId = shop_id
    return shop

# Eliminar un registro de la tabla shop por su ID
@app.delete("/shop/{shop_id}")
def delete_shop(shop_id: int):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM shop WHERE supId = %s", (shop_id,))
    connection.commit()
    return {"message": "Registro eliminado exitosamente"}
 """