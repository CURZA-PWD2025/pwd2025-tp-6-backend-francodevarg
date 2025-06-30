import { defineStore } from 'pinia'
import { ref } from 'vue'
import ArticuloService from '../services/ArticuloService'
import type { Articulo } from '../types/Articulo'


export const useArticuloStore = defineStore('articulo', () => {
  const articulos = ref<Articulo[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  async function fetchArticulos() {
    loading.value = true
    error.value = null
    try {
      const response = await ArticuloService.getAll()
      articulos.value = response.data
    } catch (err) {
      error.value = 'Error al cargar los artículos'
      console.error('fetchArticulos →', err)
    } finally {
      loading.value = false
    }
  }

  return {
    articulos,
    loading,
    error,
    fetchArticulos,
  }
})
