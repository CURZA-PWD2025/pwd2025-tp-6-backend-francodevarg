from app.database.connect_db import ConnectDB
from app.modules.marca.marca_model import MarcaModel
from app.modules.proveedor.proveedor_model import ProveedorModel


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

    def __init__(self, id=0, descripcion="", precio=0.0, stock=0, marca_id=0, proveedor_id=0):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id
        }

    @staticmethod
    def deserializar(data: dict):
        return ArticuloModel(
            id=data.get("id", 0),
            descripcion=data.get("descripcion", ""),
            precio=data.get("precio", 0.0),
            stock=data.get("stock", 0),
            marca_id=data.get("marca_id", 0),
            proveedor_id=data.get("proveedor_id", 0)
        )

    @staticmethod
    def get_all():
        rows = ConnectDB.read(ArticuloModel.SQL_SELECT_ALL)
        if not rows:
            return []


        marcas = {m["id"]: m for m in MarcaModel.get_all()}
        proveedores = {p["id"]: p for p in ProveedorModel.get_all()}

        for row in rows:
            row["marca"] = marcas.get(row["marca_id"])
            row["proveedor"] = proveedores.get(row["proveedor_id"])

        return rows

    def get_by_id(self):
        result = ConnectDB.read(ArticuloModel.SQL_SELECT_BY_ID, (self.id,))
        return result[0] if result else None

    def create(self):
        params = (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
        result = ConnectDB.write(ArticuloModel.SQL_INSERT, params)
        return result if result else False

    def update(self):
        params = (
            self.descripcion, self.precio, self.stock,
            self.marca_id, self.proveedor_id, self.id
        )
        result = ConnectDB.write(ArticuloModel.SQL_UPDATE, params)
        return result > 0

    @staticmethod
    def delete(id: int):
        ConnectDB.write("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (id,))
        result = ConnectDB.write(ArticuloModel.SQL_DELETE, (id,))
        return result > 0
