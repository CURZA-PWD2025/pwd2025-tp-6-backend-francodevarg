import { defineStore } from 'pinia'
import { ref } from 'vue'
import ProveedorService from '../services/ProveedorService'
import type { Proveedor } from '../types/Proveedor'
import { AxiosError } from 'axios'

export const useProveedorStore = defineStore('proveedor', () => {
  const proveedores = ref<Proveedor[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const deleteError = ref<string | null>(null)

  async function fetchProveedores() {
    loading.value = true
    error.value = null
    try {
      const response = await ProveedorService.getAll()
      proveedores.value = response.data
    } catch (err) {
      error.value = 'Error al cargar los proveedores'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  async function createProveedor(proveedor: Proveedor): Promise<boolean> {
    try {
      await ProveedorService.create(proveedor)
      return true
    } catch (err) {
      console.error('Error al crear el proveedor:', err)
      return false
    }
  }

  async function updateProveedor(proveedor: Proveedor): Promise<boolean> {
    try {
      await ProveedorService.update(proveedor.id, proveedor)
      const index = proveedores.value.findIndex(m => m.id === proveedor.id)
      if (index !== -1) proveedores.value[index] = { ...proveedor }
      return true
    } catch (err) {
      console.error('Error al actualizar el proveedor:', err)
      return false
    }
  }

  async function deleteProveedor(id: number): Promise<boolean> {
    deleteError.value = null
    try {
      await ProveedorService.destroy(id)
      proveedores.value = proveedores.value.filter(p => p.id !== id)
      return true
    } catch (err) {
      if (err instanceof AxiosError && err.response) {
        deleteError.value = err.response.data?.message || 'Error al eliminar el proveedor.'
      } else {
        deleteError.value = 'Error desconocido al eliminar.'
      }
      console.error(err)
      return false
    }
  }

  return {
    proveedores,
    loading,
    error,
    deleteError,
    fetchProveedores,
    createProveedor,
    updateProveedor,
    deleteProveedor
  }
})
