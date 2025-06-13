// services/MarcaService.ts
import ApiService from './ApiService';
import type { Marca } from '../types/Marca';

const baseUrl = 'marcas/';

export default {
  getAll() {
    return ApiService.getAll<Marca>(baseUrl);
  },
  getOne(id: number) {
    return ApiService.getOne<Marca>(baseUrl, id);
  },
  create(data: Partial<Marca>) {
    return ApiService.create<Marca>(baseUrl, data);
  },
  update(id: number, data: Partial<Marca>) {
    return ApiService.update<Marca>(baseUrl, id, data);
  },
  destroy(id: number) {
    return ApiService.destroy(baseUrl, id);
  }
};
