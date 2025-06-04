from .marca_model import MarcaModel

class MarcaController:
      @staticmethod
      def get_all():
         marcas = MarcaModel.get_all()
         return marcas
     
      @staticmethod
      def get_by_id(id: int):
         marca = MarcaModel(id=id).get_by_id()
         return marca
     
      @staticmethod  
      def update(id: int, nombre: str):
            marca = MarcaModel(id, nombre)
            result = marca.update()
            return result 
         
      @staticmethod
      def create(nombre: str):
            marca = MarcaModel(nombre=nombre)
            result = marca.create()
            return result
      
      @staticmethod
      def delete(id: int):
            result = MarcaModel.delete(id)
            return result