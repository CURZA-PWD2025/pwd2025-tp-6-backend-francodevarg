from app.database.connect_db import ConnectDB

class ProveedorModel:
    SQL_SELECT_ALL = "SELECT * FROM PROVEEDORES"
    SQL_SELECT_BY_ID = "SELECT * FROM PROVEEDORES WHERE id = %s"
    SQL_INSERT = "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)"
    SQL_UPDATE = "UPDATE PROVEEDORES SET nombre = %s, telefono = %s, direccion = %s, email = %s WHERE id = %s"
    SQL_DELETE = "DELETE FROM PROVEEDORES WHERE id = %s"
    
    def __init__(self, id: int = 0, nombre: str = "", telefono: str = "", direccion: str = "", email: str = ""):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'email': self.email
        }

    @staticmethod
    def deserializar(data: dict):
        return ProveedorModel(
            id=data['id'],
            nombre=data['nombre'],
            telefono=data['telefono'],
            direccion=data['direccion'],
            email=data['email']
        )

    @staticmethod
    def get_all() -> list[dict]:
        rows = ConnectDB.read(ProveedorModel.SQL_SELECT_ALL)
        return rows if rows else []

    @staticmethod
    def get_by_id(id:int) -> dict:
        result = ConnectDB.read(ProveedorModel.SQL_SELECT_BY_ID, (id,))
        return result[0] if result else None

    def create(self) -> bool | None:
        result = ConnectDB.write(ProveedorModel.SQL_INSERT, (self.nombre, self.telefono, self.direccion, self.email))
        return result > 0 or None
    
    def update(self) -> bool | None:
        result = ConnectDB.write(ProveedorModel.SQL_UPDATE, (self.nombre, self.telefono, self.direccion, self.email, self.id))
        return result > 0

    @staticmethod
    def delete(id: int) -> bool | None:
        try:
            getArticulosByProveedor = ProveedorModel.getArticulosByProveedor(id)
            
            if len(getArticulosByProveedor) > 0:
                return False            
            # Si no hay artículos asociados, procede a eliminar el proveedor
            result = ConnectDB.write(ProveedorModel.SQL_DELETE, (id,))
            return result > 0 if result is not None else None

        except Exception as e:
            return None
    
    @staticmethod
    def getArticulosByProveedor(id: int) -> list[dict]:
        SQL_SELECT_ARTICULOS_BY_PROVEEDOR = """
            SELECT * FROM ARTICULOS WHERE proveedor_id = %s
        """
        rows = ConnectDB.read(SQL_SELECT_ARTICULOS_BY_PROVEEDOR, (id,))
        return rows if rows else []
