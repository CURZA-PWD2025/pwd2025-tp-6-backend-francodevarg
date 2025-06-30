export interface Articulo {
    id: number
    descripcion: string
    precio: string
    stock: number
    marca: { id: number; nombre: string }
    proveedor: { id: number; nombre: string }
    categorias: { id: number; nombre: string }[]
  }
  