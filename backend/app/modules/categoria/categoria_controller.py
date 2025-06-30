from flask import jsonify
from .categoria_model import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        categorias = CategoriaModel.get_all()
        return categorias

    @staticmethod
    def get_one(id: int):
        categoria = CategoriaModel().get_one(id=id)
        return categoria

    @staticmethod
    def create(name: str):
        categoria = CategoriaModel(nombre=name)
        result = categoria.create()
        return result

    @staticmethod
    def update(id: int, name: str):
        categoria = CategoriaModel(id,nombre=name)
        result = categoria.update()
        return result

    @staticmethod
    def delete(id: int):
        result = CategoriaModel.delete(id)
        return result