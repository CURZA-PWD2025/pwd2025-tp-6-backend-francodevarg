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

  async function createMarca(marca: Marca): Promise<boolean> {
    try {
      await MarcaService.create(marca)
      await fetchMarcas() // Refrescar la lista después de crear
      return true
    } catch (err) {
      console.error('Error al crear la marca:', err)
      return false
    }
  }
  
  async function updateMarca(marca: Marca): Promise<boolean> {
    try {
      await MarcaService.update(marca.id, marca)
      const index = marcas.value.findIndex(m => m.id === marca.id)
      if (index !== -1) marcas.value[index] = { ...marca }
      return true
    } catch (err) {
      console.error('Error al actualizar la marca:', err)
      return false
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
    createMarca,
    updateMarca,
    deleteMarca,
  }
})

