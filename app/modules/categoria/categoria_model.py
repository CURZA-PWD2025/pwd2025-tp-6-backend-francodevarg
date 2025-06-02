from app.database.connect_db import ConnectDB

class CategoriaModel:
    SQL_SELECT_ALL = "SELECT * FROM CATEGORIAS"
    SQL_SELECT_BY_ID = "SELECT * FROM CATEGORIAS WHERE id = %s"
    SQL_INSERT = "INSERT INTO CATEGORIAS (nombre) VALUES (%s)"
    SQL_UPDATE = "UPDATE CATEGORIAS SET nombre = %s WHERE id = %s"
    SQL_DELETE = "DELETE FROM CATEGORIAS WHERE id = %s"

    def __init__(self, id: int = 0, nombre: str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre
        }

    @staticmethod
    def deserializar(data: dict):
        return CategoriaModel(
            id=data['id'],
            nombre=data['nombre'],
        )

    @staticmethod
    def get_all():
        rows = ConnectDB.read(CategoriaModel.SQL_SELECT_ALL)
        return rows if rows else []
        
    def get_by_id(self):
        result = ConnectDB.read(CategoriaModel.SQL_SELECT_BY_ID, (self.id,))
        return result[0] if result else None

    def create(self):
        result = ConnectDB.write(CategoriaModel.SQL_INSERT, (self.nombre,))
        return result if result else False

    def update(self):
        result = ConnectDB.write(CategoriaModel.SQL_UPDATE, (self.nombre, self.id))
        return result > 0

    @staticmethod
    def delete(id: int):
        result = ConnectDB.write(CategoriaModel.SQL_DELETE, (id,))
        return result > 0
