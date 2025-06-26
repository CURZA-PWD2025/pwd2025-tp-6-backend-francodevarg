import { defineStore } from 'pinia'
import { ref } from 'vue'
import MarcaService from '../services/MarcaService'
import type { Marca } from '../types/Marca'
import { AxiosError } from 'axios'

export const useMarcaStore = defineStore('marca', () => {
  const marcas = ref<Marca[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const deleteError = ref<string | null>(null)

  async function fetchMarcas() {
    loading.value = true
    error.value = null
    try {
      const response = await MarcaService.getAll()
      marcas.value = response.data
    } catch (err) {
      error.value = 'Error al cargar las marcas'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  async function deleteMarca(id: number): Promise<boolean> {
    deleteError.value = null
    try {
      await MarcaService.destroy(id)
      marcas.value = marcas.value.filter(m => m.id !== id)
      return true
    } catch (err) {
      if (err instanceof AxiosError && err.response) {
        deleteError.value = err.response.data?.message || 'Error al eliminar la marca.'
      } else {
        deleteError.value = 'Error desconocido al eliminar.'
      }
      console.error(err)
      return false
    }
  }

  return {
    marcas,
    loading,
    error,
    deleteError,
    fetchMarcas,
    deleteMarca,
  }
})

