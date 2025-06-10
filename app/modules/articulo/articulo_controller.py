from .articulo_model import ArticuloModel
from ..marca.marca_model import MarcaModel
from ..proveedor.proveedor_model import ProveedorModel

class ArticuloController:
    @staticmethod
    def get_all():
        articulos = ArticuloModel.get_all()
        return articulos

    @staticmethod
    def get_one(id: int):
        articulo = ArticuloModel().get_one(id=id)
        return articulo

    @staticmethod
    def create(data: dict):
        marca = MarcaModel(id=data['marca_id'])
        proveedor = ProveedorModel(id=data['proveedor_id'])
        articulo = ArticuloModel(
            descripcion=data['descripcion'],
            precio=data['precio'],
            stock=data['stock'],
            marca=marca,
            proveedor=proveedor
        )
        result = articulo.create()
        return result

    @staticmethod
    def update(id: int, data: dict):
        marca = MarcaModel(id=data['marca_id'])
        proveedor = ProveedorModel(id=data['proveedor_id'])
        articulo = ArticuloModel(
            id=id,
            descripcion=data['descripcion'],
            precio=data['precio'],
            stock=data['stock'],
            marca=marca,
            proveedor=proveedor
        )
        result = articulo.update()
        return result

    @staticmethod
    def delete(id: int):
        result = ArticuloModel.delete(id)
        return result