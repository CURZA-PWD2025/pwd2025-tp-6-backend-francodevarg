from app.database.connect_db import ConnectDB


class MarcaModel:
    SQL_SELECT_ALL = "SELECT * FROM MARCAS"
    SQL_SELECT_BY_ID = "SELECT * FROM MARCAS WHERE id = %s"
    SQL_INSERT = "INSERT INTO MARCAS (nombre) VALUES (%s)"
    SQL_UPDATE = "UPDATE MARCAS SET nombre = %s WHERE id = %s"
    SQL_DELETE = "DELETE FROM MARCAS WHERE id = %s"
    
    def __init__(self, id: int = 0, name: str = ""):
        self.id = id
        self.name = name

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }

    @staticmethod
    def deserializar(data: dict):
        return MarcaModel(
            id=data['id'],
            name=data['name'],
        )

    @staticmethod
    def get_all():
        rows = ConnectDB.read(MarcaModel.SQL_SELECT_ALL)
        return rows if rows else []

    def get_by_id(self):
        result = ConnectDB.read(MarcaModel.SQL_SELECT_BY_ID, (self.id,))
        return result[0] if result else None

    def create(self):
        result = ConnectDB.write(MarcaModel.SQL_INSERT, (self.name,))
        return result if result else False

    def update(self):
        result = ConnectDB.write(MarcaModel.SQL_UPDATE, (self.name, self.id))
        return result > 0

    @staticmethod
    def delete(id: int):
        result = ConnectDB.write(MarcaModel.SQL_DELETE, (id,))
        return result > 0
