import { defineStore } from 'pinia'
import { ref } from 'vue'
import CategoriaService from '../services/CategoriaService'
import type { Categoria } from '../types/Categoria'
import { AxiosError } from 'axios'

export const useCategoriaStore = defineStore('categoria', () => {
  const categorias = ref<Categoria[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const deleteError = ref<string | null>(null)

  async function fetchCategorias() {
    loading.value = true
    error.value = null
    try {
      const response = await CategoriaService.getAll()
      categorias.value = response.data
    } catch (err) {
      error.value = 'Error al cargar las categorías'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  async function createCategoria(categoria: Categoria): Promise<boolean> {
    try {
      await CategoriaService.create(categoria)
      return true
    } catch (err) {
      console.error('Error al crear la categoría:', err)
      return false
    }
  }

  async function updateCategoria(categoria: Categoria): Promise<boolean> {
    try {
      await CategoriaService.update(categoria.id, categoria)
      const index = categorias.value.findIndex(c => c.id === categoria.id)
      if (index !== -1) categorias.value[index] = { ...categoria }
      return true
    } catch (err) {
      console.error('Error al actualizar la categoría:', err)
      return false
    }
  }

  async function deleteCategoria(id: number): Promise<boolean> {
    deleteError.value = null
    try {
      await CategoriaService.destroy(id)
      categorias.value = categorias.value.filter(c => c.id !== id)
      return true
    } catch (err) {
      if (err instanceof AxiosError && err.response) {
        deleteError.value = err.response.data?.mensaje || 'Error al eliminar la categoría.'
      } else {
        deleteError.value = 'Error desconocido al eliminar.'
      }
      console.error(err)
      return false
    }
  }

  return {
    categorias,
    loading,
    error,
    deleteError,
    fetchCategorias,
    createCategoria,
    updateCategoria,
    deleteCategoria
  }
})
