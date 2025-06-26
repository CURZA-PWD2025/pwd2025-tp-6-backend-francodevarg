import ApiService from './ApiService'
import type { Proveedor } from '../types/Proveedor'

const baseUrl = 'proveedores/'

export default {
  getAll() {
    return ApiService.getAll<Proveedor>(baseUrl)
  },
  getOne(id: number) {
    return ApiService.getOne<Proveedor>(baseUrl, id)
  },
  create(data: Partial<Proveedor>) {
    return ApiService.create<Proveedor>(baseUrl, data)
  },
  update(id: number, data: Partial<Proveedor>) {
    return ApiService.update<Proveedor>(baseUrl, id, data)
  },
  destroy(id: number) {
    return ApiService.destroy(baseUrl, id)
  }
}
