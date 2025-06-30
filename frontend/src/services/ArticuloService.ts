// services/ArticuloService.ts
import ApiService from './ApiService'
import type { Articulo } from '../types/Articulo'

const baseUrl = 'articulos/'

export default {
  getAll() {
    return ApiService.getAll<Articulo>(baseUrl)
  },
  getOne(id: number) {
    return ApiService.getOne<Articulo>(baseUrl, id)
  },
  create(data: Partial<Articulo>) {
    return ApiService.create<Articulo>(baseUrl, data)
  },
  update(id: number, data: Partial<Articulo>) {
    return ApiService.update<Articulo>(baseUrl, id, data)
  },
  destroy(id: number) {
    return ApiService.destroy(baseUrl, id)
  }
}
