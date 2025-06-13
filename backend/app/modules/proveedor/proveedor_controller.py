from .proveedor_model import ProveedorModel

class ProveedorController:
    
    @staticmethod
    def get_all():
        return ProveedorModel.get_all()
    
    @staticmethod
    def get_one(id: int)-> dict:
        proveedor = ProveedorModel().get_one(id)
        return proveedor
    
    @staticmethod
    def create(data: dict) -> dict:
        proveedor = ProveedorModel(nombre=data['nombre'], telefono=data['telefono'], 
                                   direccion=data['direccion'], email=data['email'])
        result = proveedor.create()
        return result
    
    @staticmethod  
    def update(data: dict) -> dict:
        proveedor = ProveedorModel(id=data["id"],nombre=data['nombre'], telefono=data['telefono'], 
                                   direccion=data['direccion'], email=data['email'])        
        result = proveedor.update()
        return result
    
    @staticmethod
    def delete(id: int):
        result = ProveedorModel.delete(id)
        return result
