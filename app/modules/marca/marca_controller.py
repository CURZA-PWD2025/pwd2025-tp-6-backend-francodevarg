from .marca_model import MarcaModel

class MarcaController:
      @staticmethod
      def get_all() -> list[dict]:
         marcas = MarcaModel.get_all()
         return marcas
     
      @staticmethod
      def get_one(id: int)-> dict:
         marca = MarcaModel().get_one(id)
         return marca
         
      @staticmethod
      def create(data: dict) -> dict:
            marca = MarcaModel(nombre=data['nombre'])
            result = marca.create()
            return result
     
      @staticmethod  
      def update(data: dict)-> dict:
            marca = MarcaModel(id=data.get('id'), nombre=data.get('nombre'))
            result = marca.update()

            if result:
                  return {"message": "Marca actualizada correctamente"}, 200
            else:
                  return {"message": "Error al actualizar la marca"}, 500
      
      @staticmethod
      def delete(id: int)-> dict:
            result = MarcaModel.delete(id)
            if result:
                return {"message": "Marca eliminada correctamente"}
            else:
                return {"message": "Error al eliminar la marca o la marca tiene artículos asociados"}, 400