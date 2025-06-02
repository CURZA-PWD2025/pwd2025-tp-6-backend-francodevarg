from flask import Blueprint, request, jsonify
from .articulo_controller import ArticuloController

articulo_bp = Blueprint("articulos", __name__)

# Obtener todos los artículos
@articulo_bp.route("/articulos", methods=["GET"])
def get_all_articulos():
    try:
        articulos = ArticuloController.get_all()
        if articulos:
            return jsonify(articulos), 200
        else:
            return jsonify({'mensaje': 'No se encontraron artículos'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500


# Obtener un artículo por ID
@articulo_bp.route("/articulos/<int:id>", methods=["GET"])
def get_articulo_by_id(id):
    try:
        articulo = ArticuloController.get_by_id(id)
        if articulo:
            return jsonify(articulo), 200
        else:
            return jsonify({'mensaje': 'No se encontró el artículo'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500


# Crear un nuevo artículo
@articulo_bp.route("/articulos", methods=["POST"])
def create_articulo():
    try:
        data = request.get_json()
        descripcion = data.get('descripcion')
        precio = data.get('precio')
        stock = data.get('stock')
        marca_id = data.get('marca_id')
        proveedor_id = data.get('proveedor_id')

        # Validaciones mínimas
        if not descripcion or precio is None or stock is None or not marca_id or not proveedor_id:
            return jsonify({'mensaje': 'Todos los campos son requeridos'}), 400

        result = ArticuloController.create(descripcion, precio, stock, marca_id, proveedor_id)

        if result:
            return jsonify({'mensaje': 'Artículo creado con éxito', 'id': result}), 201
        else:
            return jsonify({'mensaje': 'Error al crear el artículo'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500


# Actualizar un artículo existente
@articulo_bp.route("/articulos/<int:id>", methods=["PUT"])
def update_articulo(id):
    try:
        data = request.get_json()
        descripcion = data.get('descripcion')
        precio = data.get('precio')
        stock = data.get('stock')
        marca_id = data.get('marca_id')
        proveedor_id = data.get('proveedor_id')

        if not descripcion or precio is None or stock is None or not marca_id or not proveedor_id:
            return jsonify({'mensaje': 'Todos los campos son requeridos'}), 400

        result = ArticuloController.update(id, descripcion, precio, stock, marca_id, proveedor_id)

        if result:
            return jsonify({'mensaje': 'Artículo actualizado con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar el artículo'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500


# Eliminar un artículo
@articulo_bp.route("/articulos/<int:id>", methods=["DELETE"])
def delete_articulo(id):
    try:
        result = ArticuloController.delete(id)

        if result:
            return jsonify({'mensaje': 'Artículo eliminado con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al eliminar el artículo'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500
