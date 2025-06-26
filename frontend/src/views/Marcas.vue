<template>
  <v-card class="rounded-lg elevation-1">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>Listado de Marcas</v-toolbar-title>
      <v-spacer />
      <v-btn icon @click="nuevaMarca">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-toolbar>

    <MarcaTable
      :marcas="store.marcas"
      @edit="editarMarca"
      @delete="openDeleteDialog"
    />

    <MarcaDeleteDialog
      :model-value="deleteDialog"
      :marca="marcaSeleccionada"
      :error="store.deleteError"
      @cancel="cerrarDeleteDialog"
      @confirm="confirmarEliminacion"
    />

    <MarcaEditDialog
      v-model="editDialog"
      :marca="marcaSeleccionada"
      @cancel="cerrarEditDialog"
      @confirm="confirmarEdicion"
    />
  </v-card>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useMarcaStore } from '../stores/marcaStore'
import type { Marca } from '../types/Marca'
import MarcaTable from '../components/MarcaTable.vue'
import MarcaDeleteDialog from '../components/MarcaDeleteDialog.vue'
import MarcaEditDialog from '../components/MarcaEditDialog.vue'

const store = useMarcaStore()

const deleteDialog = ref(false)
const editDialog = ref(false)
const marcaSeleccionada = ref<Marca | null>(null)
const modoEdicion = ref<'create' | 'edit'>('create')

onMounted(() => {
  store.fetchMarcas()
})

function nuevaMarca() {
  marcaSeleccionada.value = null
  modoEdicion.value = 'create'
  editDialog.value = true
}


function editarMarca(marca: Marca) {
  marcaSeleccionada.value = marca
  modoEdicion.value = 'edit'
  editDialog.value = true
}


function cerrarDeleteDialog() {
  deleteDialog.value = false
  marcaSeleccionada.value = null
}

function cerrarEditDialog() {
  editDialog.value = false
  marcaSeleccionada.value = null
}

function openDeleteDialog(marca: Marca) {
  marcaSeleccionada.value = marca
  deleteDialog.value = true
}

async function confirmarEliminacion() {
  if (marcaSeleccionada.value) {
    const ok = await store.deleteMarca(marcaSeleccionada.value.id)
    if (ok) cerrarDeleteDialog()
  }
}

async function confirmarEdicion(marca: Marca) {
  const ok =
    modoEdicion.value === 'create'
      ? await store.createMarca(marca)
      : await store.updateMarca(marca)

  await store.fetchMarcas()

  if (ok) cerrarEditDialog()
}

</script>
