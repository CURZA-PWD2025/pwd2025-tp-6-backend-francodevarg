from flask import Blueprint, request, jsonify
from .proveedor_controller import ProveedorController

proveedor_bp = Blueprint("proveedores", __name__)

@proveedor_bp.route("/proveedores/", methods=["GET"])
def get_all():
    try:
        proveedores = ProveedorController.get_all()
        if proveedores:
            return jsonify(proveedores), 200
        else:
            return jsonify({'mensaje': 'No se encontraron proveedores'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@proveedor_bp.route("/proveedores/<int:id>", methods=["GET"])
def get_one(id):
    try:
        proveedor = ProveedorController.get_by_id(id)
        if proveedor:
            return jsonify(proveedor), 200
        else:
            return jsonify({'mensaje': 'Proveedor no encontrado'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500


@proveedor_bp.route("/proveedores/", methods=["POST"])
def create():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        telefono = data.get('telefono')
        direccion = data.get('direccion')
        email = data.get('email')

        # Validación de campos requeridos
        if not nombre or not telefono or not direccion or not email:
            return jsonify({'mensaje': 'Todos los campos son requeridos (nombre,direccion,telefono,email)'}), 400

        proveedor = ProveedorController.create(data)
        if proveedor:
            return jsonify({'mensaje': 'Proveedor creado con éxito'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear el proveedor'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@proveedor_bp.route("/proveedores/<int:id>", methods=["PUT"])
def update(id):
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        telefono = data.get('telefono')
        direccion = data.get('direccion')
        email = data.get('email')

        id = data.get('id')
        if not ProveedorController.get_by_id(id):
            return jsonify({'mensaje': f'Proveedor con ID {id} no encontrado'}), 404

        # Validación de campos requeridos
        if not nombre or not telefono or not direccion or not email:
            return jsonify({'mensaje': 'Todos los campos son requeridos'}), 400

        result = ProveedorController.update(data)
        if result:
            return jsonify({'mensaje': 'Proveedor actualizado con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar el proveedor'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@proveedor_bp.route("/proveedores/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        result = ProveedorController.delete(id)
        if result:
            return jsonify({'mensaje': 'Proveedor eliminado con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al eliminar el proveedor'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500
