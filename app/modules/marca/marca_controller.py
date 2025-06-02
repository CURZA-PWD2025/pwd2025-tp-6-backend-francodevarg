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
      def update(id: int, name: str):
            marca = MarcaModel(id, name)
            result = marca.update()
            return result 
         
      @staticmethod
      def create(name: str):
            marca = MarcaModel(name=name)
            result = marca.create()
            return result
      
      @staticmethod
      def delete(id: int):
            result = MarcaModel.delete(id)
            return result