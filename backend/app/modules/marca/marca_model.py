from app.database.connect_db import ConnectDB


class MarcaModel:
    SQL_SELECT_ALL = "SELECT * FROM MARCAS"
    SQL_SELECT_BY_ID = "SELECT * FROM MARCAS WHERE id = %s"
    SQL_INSERT = "INSERT INTO MARCAS (nombre) VALUES (%s)"
    SQL_UPDATE = "UPDATE MARCAS SET nombre = %s WHERE id = %s"
    SQL_DELETE = "DELETE FROM MARCAS WHERE id = %s"
    
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
        return MarcaModel(
            id=data['id'],
            nombre=data['nombre'],
        )

    @staticmethod
    def get_all() -> list[dict]:
        rows = ConnectDB.read(MarcaModel.SQL_SELECT_ALL)
        return rows if rows else []

    @staticmethod
    def get_one(id:int) -> dict:
        result = ConnectDB.read(MarcaModel.SQL_SELECT_BY_ID, (id,))
        return result[0] if result else None

    def create(self) -> bool | None:
        result = ConnectDB.write(MarcaModel.SQL_INSERT, (self.nombre,))
        return result > 0 or None


    def update(self) -> bool | None:
        result = ConnectDB.write(MarcaModel.SQL_UPDATE, (self.nombre,self.id))
        return result > 0 or None
    
    def delete(id: int) -> bool | None:
        try:
            getArticulosByMarca = MarcaModel.getArticulosByMarca(id)
            
            if len(getArticulosByMarca) > 0:
                return False            
            # Si no hay artículos asociados, procede a eliminar la marca
            result = ConnectDB.write(MarcaModel.SQL_DELETE, (id,))
            return result > 0 if result is not None else None

        except Exception as e:
            return None
    
    @staticmethod
    def getArticulosByMarca(id: int) -> list[dict]:
        SQL_SELECT_ARTICULOS_BY_MARCA = """
            SELECT * FROM ARTICULOS WHERE marca_id = %s
        """
        rows = ConnectDB.read(SQL_SELECT_ARTICULOS_BY_MARCA, (id,))
        return rows if rows else []