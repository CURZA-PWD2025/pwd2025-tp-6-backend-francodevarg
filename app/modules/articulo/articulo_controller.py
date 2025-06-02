from .articulo_model import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        articulos = ArticuloModel.get_all()
        return articulos

    @staticmethod
    def get_by_id(id: int):
        articulo = ArticuloModel(id=id).get_by_id()
        return articulo

    @staticmethod
    def create(descripcion: str, precio: float, stock: int, marca_id: int, proveedor_id: int):
        articulo = ArticuloModel(
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            marca_id=marca_id,
            proveedor_id=proveedor_id
        )
        result = articulo.create()
        return result

    @staticmethod
    def update(id: int, descripcion: str, precio: float, stock: int, marca_id: int, proveedor_id: int):
        articulo = ArticuloModel(
            id=id,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            marca_id=marca_id,
            proveedor_id=proveedor_id
        )
        result = articulo.update()
        return result

    @staticmethod
    def delete(id: int):
        result = ArticuloModel.delete(id)
        return (result is not None) and (result > 0)
