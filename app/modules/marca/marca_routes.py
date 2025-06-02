from flask import Blueprint, request, jsonify
from .marca_controller import MarcaController

marca_bp=Blueprint("marcas", __name__)

@marca_bp.route("/marcas/")
def get_all():
    try:
        marcas = MarcaController.get_all()
        if marcas:
            return jsonify(marcas), 200
        else:
            return jsonify({'mensaje': 'no se encontraron marcas'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500

@marca_bp.route("/marcas/<int:id>")
def get_by_id(id):
    try:
        marca = MarcaController.get_by_id(id)
        if marca:
            return jsonify(marca), 200
        else:
            return jsonify({'mensaje': 'no se encontro la marca'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f" error : {str(exc)}"}), 500

@marca_bp.route("/marcas/", methods=["POST"])
def create():
    try:
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({'mensaje': 'La descripción es requerida'}), 400

        result = MarcaController.create(name)
        
        if result:
            return jsonify({'mensaje': 'Marca creada con éxito', 'id': result}), 201
        else:
            return jsonify({'mensaje': 'Error al crear la marca'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500
        
@marca_bp.route("/marcas/<int:id>", methods=["PUT"])
def update(id):
    try:
        # Obtener los datos del cuerpo de la solicitud
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({'mensaje': 'La descripción es requerida'}), 400

        result = MarcaController.update(id, name)
        
        if result:
            return jsonify({'mensaje': 'Marca actualizada con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar la marca'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500
    
@marca_bp.route("/marcas/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        result = MarcaController.delete(id)
        
        if result:
            return jsonify({'mensaje': 'Marca eliminada con éxito'}), 200
        else:
            return jsonify({'mensaje': 'Error al eliminar la marca'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500