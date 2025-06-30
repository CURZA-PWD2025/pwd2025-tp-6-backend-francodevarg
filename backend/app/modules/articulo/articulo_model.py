from app.database.connect_db import ConnectDB
from app.modules.marca.marca_model import MarcaModel as Marca
from app.modules.proveedor.proveedor_model import ProveedorModel as Proveedor
from app.modules.categoria.categoria_model import CategoriaModel as Categoria


class ArticuloModel:
    SQL_SELECT_ALL = "SELECT * FROM ARTICULOS"
    SQL_SELECT_BY_ID = "SELECT * FROM ARTICULOS WHERE id = %s"
    SQL_INSERT = """
        INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id)
        VALUES (%s, %s, %s, %s, %s)
    """
    SQL_UPDATE = """
        UPDATE ARTICULOS
        SET descripcion = %s, precio = %s, stock = %s, marca_id = %s, proveedor_id = %s
        WHERE id = %s
    """
    SQL_DELETE = "DELETE FROM ARTICULOS WHERE id = %s"

    def __init__(self, id:int = 0, descripcion="", precio=0.0, stock=0, marca:Marca = None, proveedor:Proveedor = None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serializar(),
            "proveedor": self.proveedor.serializar()
    }
    @staticmethod
    def deserializar(data: dict):
        return ArticuloModel(
            id=data['id'], 
            descripcion=data['descripcion'],
            precio=data['precio'], 
            stock=data['stock'],
            marca=data['marca'],
            proveedor=data['proveedor']            
        )

    @staticmethod
    def get_all() -> list[dict]:
        rows = ConnectDB.read(ArticuloModel.SQL_SELECT_ALL)
        if not rows:
            return []

        articulos = []
        for row in rows:
            marca = Marca().get_one(row["marca_id"])
            proveedor = Proveedor().get_one(row["proveedor_id"])

            # Obtener todas las categorías asociadas (N:N)
            categoria_ids = ConnectDB.read(
                "SELECT categoria_id FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s",
                (row["id"],)
            )
            categorias = [
                Categoria().get_one(cat_row["categoria_id"]) for cat_row in categoria_ids
            ]

            # Inyectar datos
            row["marca"] = marca
            row["proveedor"] = proveedor
            row["categorias"] = categorias

            # Eliminar claves que ya no son necesarias
            del row["marca_id"]
            del row["proveedor_id"]

            articulos.append(row)

        return articulos

    @staticmethod
    def get_one(id: int) -> dict | None:
        result = ConnectDB.read(ArticuloModel.SQL_SELECT_BY_ID, (id,))
        if result:
            marca = Marca().get_one((result[0]["marca_id"]))
            proveedor = Proveedor().get_one((result[0]["proveedor_id"]))
            result[0]["marca"] = marca
            result[0]["proveedor"] = proveedor
            del result[0]["marca_id"]
            del result[0]["proveedor_id"]
        else:
            result = []
        return result[0] if result else None
    
        
    def create(self):
        params = (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id)
        result = ConnectDB.write(ArticuloModel.SQL_INSERT, params)
        return result if result else False


    def update(self):
        params = (
            self.descripcion, self.precio, self.stock,
            self.marca.id, self.proveedor.id, self.id
        )
        result = ConnectDB.write(ArticuloModel.SQL_UPDATE, params)
        return result > 0

    @staticmethod
    def delete(id: int):
        try:
            #Eliminar las relacions N a N con categorías
            ConnectDB.write(
                "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (id,)
            )

            result = ConnectDB.write(ArticuloModel.SQL_DELETE, (id,))
            return result > 0 if result is not None else None

        except Exception as e:
            print(f"Error eliminando artículo {id}: {e}")
            return None
        
    def asociar_categorias(self, articulo_id: int, categoria_ids: list[int]) -> None:
        for categoria_id in categoria_ids:
            ConnectDB.write(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                (articulo_id, categoria_id)
            )