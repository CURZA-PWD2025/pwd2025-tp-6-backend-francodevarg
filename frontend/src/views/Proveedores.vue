<template>
  <v-card class="rounded-lg elevation-1">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>Listado de Proveedores</v-toolbar-title>
      <v-spacer />
      <v-btn icon @click="nuevoProveedor">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-toolbar>

    <ProveedorTable
    :proveedores="store.proveedores"
    @show="verProveedor"
    @edit="editarProveedor"
    @delete="abrirDialogEliminar"
    />
    
    <ProveedorShowDialog
        :model-value="showDialog"
        :proveedor="proveedorSeleccionadoParaVer"
        @close="showDialog = false"
        />


    <ProveedorDeleteDialog
      :model-value="deleteDialog"
      :proveedor="proveedorSeleccionado"
      :error="store.deleteError"
      @cancel="cerrarDialogEliminar"
      @confirm="confirmarEliminacion"
    />

    <ProveedorEditDialog
      v-model="editDialog"
      :proveedor="proveedorSeleccionado"
      @cancel="cerrarDialogEditar"
      @confirm="confirmarEdicion"
    />
  </v-card>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useProveedorStore } from '../stores/proveedorStore'
import type { Proveedor } from '../types/Proveedor'
import ProveedorTable from '../components/ProveedorTable.vue'
import ProveedorDeleteDialog from '../components/ProveedorDeleteDialog.vue'
import ProveedorEditDialog from '../components/ProveedorEditDialog.vue'
import ProveedorShowDialog from '../components/ProveedorShowDialog.vue'

const store = useProveedorStore()

const deleteDialog = ref(false)
const editDialog = ref(false)
const proveedorSeleccionado = ref<Proveedor | null>(null)
const modoEdicion = ref<'create' | 'edit'>('create')
const showDialog = ref(false)
const proveedorSeleccionadoParaVer = ref<Proveedor | null>(null)


onMounted(() => {
  store.fetchProveedores()
})

function verProveedor(proveedor: Proveedor) {
  proveedorSeleccionadoParaVer.value = proveedor
  showDialog.value = true
}

function nuevoProveedor() {
  proveedorSeleccionado.value = null
  modoEdicion.value = 'create'
  editDialog.value = true
}

function editarProveedor(proveedor: Proveedor) {
  proveedorSeleccionado.value = proveedor
  modoEdicion.value = 'edit'
  editDialog.value = true
}

function abrirDialogEliminar(proveedor: Proveedor) {
  proveedorSeleccionado.value = proveedor
  deleteDialog.value = true
}

function cerrarDialogEliminar() {
  deleteDialog.value = false
  proveedorSeleccionado.value = null
  store.deleteError = null
}

function cerrarDialogEditar() {
  editDialog.value = false
  proveedorSeleccionado.value = null
}

async function confirmarEliminacion() {
  if (proveedorSeleccionado.value) {
    const ok = await store.deleteProveedor(proveedorSeleccionado.value.id)
    if (ok) cerrarDialogEliminar()
  }
}

async function confirmarEdicion(proveedor: Proveedor) {
  const ok =
    modoEdicion.value === 'create'
      ? await store.createProveedor(proveedor)
      : await store.updateProveedor(proveedor)

  await store.fetchProveedores()

  if (ok) cerrarDialogEditar()
}
</script>
