import ApiService from './ApiService'
import type { Categoria } from '../types/Categoria'

const baseUrl = 'categorias/'

export default {
  getAll() {
    return ApiService.getAll<Categoria>(baseUrl)
  },
  getOne(id: number) {
    return ApiService.getOne<Categoria>(baseUrl, id)
  },
  create(data: Partial<Categoria>) {
    return ApiService.create<Categoria>(baseUrl, data)
  },
  update(id: number, data: Partial<Categoria>) {
    return ApiService.update<Categoria>(baseUrl, id, data)
  },
  destroy(id: number) {
    return ApiService.destroy(baseUrl, id)
  }
}