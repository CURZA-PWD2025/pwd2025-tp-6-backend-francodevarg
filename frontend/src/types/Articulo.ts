export interface Articulo {
  id: number
  descripcion: string
  precio: string
  stock: number
  marca: { id: number; nombre: string }
  proveedor: { id: number; nombre: string }
  categorias: { id: number; nombre: string }[]
}


export interface ArticuloPayload {
  descripcion: string
  precio: number
  stock: number
  marca_id: number
  proveedor_id: number
  categoria_ids: number[]
}
