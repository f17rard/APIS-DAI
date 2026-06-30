from flask import Flask, jsonify, request

app = Flask(__name__)

productos = {
    "201":{"id": 201, "producto": "Teclado Mecánico RGB", "precio": 45.00, "stock": 12},
    "202":{"id": 202, "producto": "Mouse inalámbrico", "precio": 18.50, "stock": 25},
    "203":{"id": 203, "producto": "Monitor LED 24\"", "precio": 165.00, "stock": 8}
}

@app.route("/")
def inicio():
    pass

@app.get("/productos")
def consultar_catalogo():
    pass

@app.get("/productos/<int:id>")
def consultar_un_producto():
    pass

@app.post("/productos")
def añadir_producto():
    pass