from .proveedor_model import ProveedorModel

class ProveedorController:
    
    @staticmethod
    def get_all():
        return ProveedorModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        return ProveedorModel(id=id).get_by_id()
    
    @staticmethod  
    def update(id: int, nombre: str, telefono: str, direccion: str, email: str):
        proveedor = ProveedorModel(id, nombre, telefono, direccion, email)
        result = proveedor.update()
        return result
    
    @staticmethod
    def create(nombre: str, telefono: str, direccion: str, email: str):
        proveedor = ProveedorModel(nombre=nombre, telefono=telefono, direccion=direccion, email=email)
        result = proveedor.create()
        return proveedor if result else None
    
    @staticmethod
    def delete(id: int):
        result = ProveedorModel.delete(id)
        return result
