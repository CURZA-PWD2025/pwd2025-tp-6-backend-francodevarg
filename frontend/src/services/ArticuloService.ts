import ApiService from './ApiService'
import type { Articulo, ArticuloPayload } from '../types/Articulo'

const baseUrl = 'articulos/'

export default {
  getAll() {
    return ApiService.getAll<Articulo>(baseUrl)
  },
  getOne(id: number) {
    return ApiService.getOne<Articulo>(baseUrl, id)
  },
  create(data: ArticuloPayload) {
    return ApiService.create<ArticuloPayload>(baseUrl, data)
  },
  update(id: number, data: ArticuloPayload) {
    return ApiService.update<ArticuloPayload>(baseUrl, id, data)
  },
  destroy(id: number) {
    return ApiService.destroy(baseUrl, id)
  }
}
