from flask import Flask, jsonify, request

app = Flask(__name__)

productos = {
    201:{"id": 201, "nombre": "Teclado Mecánico RGB", "precio": 45.00, "stock": 12},
    202:{"id": 202, "nombre": "Mouse inalámbrico", "precio": 18.50, "stock": 25},
    203:{"id": 203, "nombre": "Monitor LED 24\"", "precio": 165.00, "stock": 8}
}

@app.route("/")
def inicio():
    pass

@app.get("/productos")
def consultar_catalogo():
    return jsonify(list(productos.values()))

@app.get("/productos/<int:id>")
def consultar_un_producto():
    producto = productos.get(id)
    if producto:
        return jsonify(producto)
    return jsonify({"Error":"Producto no encontrado"}), 400

@app.post("/productos")
def añadir_producto():
    nuevo_producto = request.get_json()
    campos_requeridos = ("nombre", "precio", "stock")
    # if not all(campo in producto for campo in campos_requeridos):
    #     return jsonify({"Error": "Faltan campos requeridos"}), 400
    if not nuevo_producto or not all(campo in nuevo_producto for campo in campos_requeridos):
        return jsonify({"Error": "Faltan campos requeridos"}), 400
    
    id_producto = max(productos.keys(), default=200) + 1
    if id_producto in productos:
        return jsonify({"Error": "El producto ya existe"}), 400
    
    nuevo_producto["id"] = id_producto
    productos[id_producto] = nuevo_producto
    return jsonify(nuevo_producto), 201

if __name__ == "__main__":
    app.run(debug=True)