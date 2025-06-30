<template>
    <v-card class="rounded-lg elevation-1">
      <v-toolbar color="primary" dark flat>
        <v-toolbar-title>Listado de Artículos</v-toolbar-title>
        <v-spacer />
        <v-btn icon @click="nuevoArticulo">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </v-toolbar>
  
      <ArticuloTable
        :articulos="store.articulos"
        @show="verArticulo"
        @edit="editarArticulo"
        @delete="abrirDialogEliminar"
      />
  
      <ArticuloShowDialog
        :model-value="showDialog"
        :articulo="articuloSeleccionado"
        @close="showDialog = false"
      />
  
      <ArticuloEditDialog
        v-model="editDialog"
        :articulo="modoEdicion === 'edit' ? articuloSeleccionado : null"
        @cancel="cerrarDialogEditar"
        @confirm="confirmarEdicion"
      />
    </v-card>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useArticuloStore } from '../stores/articuloStore'
  import type { Articulo, ArticuloPayload } from '../types/Articulo'
  
  import ArticuloTable from '../components/ArticuloTable.vue'
  import ArticuloShowDialog from '../components/ArticuloShowDialog.vue'
  import ArticuloEditDialog from '../components/ArticuloEditDialog.vue'
  
  const store = useArticuloStore()
  
  const articuloSeleccionado = ref<Articulo | null>(null)
  const showDialog = ref(false)
  const editDialog = ref(false)
  const modoEdicion = ref<'create' | 'edit'>('create')
  
  onMounted(() => {
    store.fetchArticulos()
  })
  
  function nuevoArticulo() {
    articuloSeleccionado.value = null
    modoEdicion.value = 'create'
    editDialog.value = true
  }
  
  function verArticulo(articulo: Articulo) {
    articuloSeleccionado.value = articulo
    showDialog.value = true
  }
  
  function editarArticulo(articulo: Articulo) {
    articuloSeleccionado.value = articulo
    modoEdicion.value = 'edit'
    editDialog.value = true
  }
  
  function abrirDialogEliminar(articulo: Articulo) {
    console.log('eliminar artículo', articulo)
  }
  
  function cerrarDialogEditar() {
    editDialog.value = false
    articuloSeleccionado.value = null
  }
  
  async function confirmarEdicion(payload: ArticuloPayload) {
    const ok = modoEdicion.value === 'edit' && articuloSeleccionado.value
      ? await store.updateArticulo(articuloSeleccionado.value.id, payload)
      : await store.createArticulo(payload)
  
    if (ok) {
      cerrarDialogEditar()
      await store.fetchArticulos()
    }
  }
  </script>
  
  