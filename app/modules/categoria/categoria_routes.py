from flask import Blueprint, request, jsonify
from .categoria_controller import CategoriaController

categoria_bp = Blueprint('categoria_bp', __name__)
@categoria_bp.route("/categorias", methods=["GET"])
def get_all_categorias():
    try:
        categorias = CategoriaController.get_all()
        if categorias:
            return jsonify(categorias), 200
        else:
            return jsonify({'mensaje': 'No se encontraron categorías'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@categoria_bp.route("/categorias/<int:id>", methods=["GET"])
def get_categoria_by_id(id):
    try:
        categoria = CategoriaController.get_by_id(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({'mensaje': 'Categoría no encontrada'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@categoria_bp.route("/categorias", methods=["POST"])
def create_categoria():
    try:
        data = request.get_json()
        name = data.get('nombre')

        if not name:
            return jsonify({'mensaje': 'El nombre es requerido'}), 400

        result = CategoriaController.create(name)
        if result:
            return jsonify({'mensaje': 'Categoría creada con éxito'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear la categoría'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@categoria_bp.route("/categorias/<int:id>", methods=["PUT"])
def update_categoria(id):
    try:
        data = request.get_json()
        name = data.get('nombre')

        if not name:
            return jsonify({'mensaje': 'El nombre es requerido'}), 400

        result = CategoriaController.update(id, name)
        if result:
            return jsonify({'mensaje': 'Categoría actualizada con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar la categoría'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@categoria_bp.route("/categorias/<int:id>", methods=["DELETE"])
def delete_categoria(id):
    try:
        result = CategoriaController.delete(id)
        if result:
            return jsonify({'mensaje': 'Categoría eliminada con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al eliminar la categoría'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500
