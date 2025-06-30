import { defineStore } from 'pinia'
import { ref } from 'vue'
import ArticuloService from '../services/ArticuloService'
import type { Articulo, ArticuloPayload } from '../types/Articulo'
import { AxiosError } from 'axios'

export const useArticuloStore = defineStore('articulo', () => {
  const articulos = ref<Articulo[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const deleteError = ref<string | null>(null)

  async function fetchArticulos() {
    loading.value = true
    error.value = null
    try {
        const response = await ArticuloService.getAll()
        articulos.value = response.data
    } catch (err) {
      error.value = 'Error al cargar los artículos'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  async function createArticulo(payload: ArticuloPayload): Promise<boolean> {
    try {
      await ArticuloService.create(payload)
      return true
    } catch (err) {
      console.error('Error al crear el artículo:', err)
      return false
    }
  }

  async function updateArticulo(id: number, payload: ArticuloPayload): Promise<boolean> {
    try {
      const updated = await ArticuloService.update(id, payload)
      const index = articulos.value.findIndex(a => a.id === id)
      if (index !== -1) {
        articulos.value[index] = updated
      }
      return true
    } catch (err) {
      console.error('Error al actualizar el artículo:', err)
      return false
    }
  }

  async function deleteArticulo(id: number): Promise<boolean> {
    deleteError.value = null
    try {
      await ArticuloService.destroy(id)
      articulos.value = articulos.value.filter(a => a.id !== id)
      return true
    } catch (err) {
      if (err instanceof AxiosError && err.response) {
        deleteError.value = err.response.data?.message || 'Error al eliminar el artículo.'
      } else {
        deleteError.value = 'Error desconocido al eliminar.'
      }
      console.error('Error al eliminar el artículo:', err)
      return false
    }
  }

  return {
    articulos,
    loading,
    error,
    deleteError,
    fetchArticulos,
    createArticulo,
    updateArticulo,
    deleteArticulo
  }
})
