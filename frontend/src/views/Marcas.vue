<template>
  <v-card class="rounded-lg elevation-1">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>Listado de Marcas</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-data-table-virtual
      class="pa-2"
      :headers="headers"
      :items="marcas"
      item-value="nombre"
      fixed-header
      fixed-footer
      height="400"
      width="100%"
      density="comfortable"
    >
      <template #item.acciones="{ item }">
        <div class="d-flex align-center justify-center">
          <v-icon size="20" class="me-2" color="primary" @click="editarMarca(item)">mdi-pencil</v-icon>
          <v-icon size="20" color="error" @click="openDeleteDialog(item)">mdi-delete</v-icon>
        </div>
      </template>

      <template #bottom>
        <div class="d-flex justify-end align-center px-4 py-2 text-medium-emphasis text-caption">
          Total de marcas: <strong class="ml-1">{{ marcas.length }}</strong>
        </div>
      </template>
    </v-data-table-virtual>

    <!-- Modal de confirmación -->
    <v-dialog v-model="deleteDialog" max-width="400">
      <v-card>
        <v-card-title class="text-h6">¿Eliminar marca?</v-card-title>
        <v-card-text>
          ¿Estás seguro de que querés eliminar <strong>{{ marcaSeleccionada?.nombre }}</strong>?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="deleteDialog = false">Cancelar</v-btn>
          <v-btn color="error" @click="confirmarEliminacion">Eliminar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import MarcaService from '../services/MarcaService'
import type { Marca } from '../types/Marca'

//ReadOnly
const headers = [
  { title: 'ID', key: 'id', align: 'start', sortable: true },
  { title: 'Nombre', key: 'nombre', align: 'start', sortable: true },
  { title: 'Acciones', key: 'acciones', align: 'center', sortable: false },
] as const

const marcas = ref<Marca[]>([])
const deleteDialog = ref(false)
const marcaSeleccionada = ref<Marca | null>(null)

onMounted(async () => {
  await cargarMarcas()
})

async function cargarMarcas() {
  try {
    const response = await MarcaService.getAll()
    marcas.value = response.data
  } catch (error) {
    console.error('Error al cargar las marcas:', error)
  }
}

function editarMarca(item: Marca) {
  console.log('Editar:', item)
}

function openDeleteDialog(item: Marca) {
  marcaSeleccionada.value = item
  deleteDialog.value = true
}

async function confirmarEliminacion() {
  if (!marcaSeleccionada.value) return

  try {
    await MarcaService.destroy(marcaSeleccionada.value.id)
    marcas.value = marcas.value.filter(m => m.id !== marcaSeleccionada.value?.id)
  } catch (error) {
    console.error('Error al eliminar la marca:', error)
  } finally {
    deleteDialog.value = false
    marcaSeleccionada.value = null
  }
}
</script>
