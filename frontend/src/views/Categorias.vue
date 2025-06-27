<template>
    <v-card class="rounded-lg elevation-1">
      <v-toolbar color="primary" dark flat>
        <v-toolbar-title>Listado de Categorías</v-toolbar-title>
        <v-spacer />
        <v-btn icon @click="nuevaCategoria"><v-icon>mdi-plus</v-icon></v-btn>
      </v-toolbar>
  
      <CategoriaTable :categorias="store.categorias" @show="verCategoria" @edit="editarCategoria" @delete="abrirDialogEliminar" />
  
      <CategoriaDeleteDialog :model-value="deleteDialog" :categoria="categoriaSeleccionada" :error="store.deleteError" @cancel="cerrarDialogEliminar" @confirm="confirmarEliminacion" />
  
      <CategoriaEditDialog v-model="editDialog" :categoria="categoriaSeleccionada" @cancel="cerrarDialogEditar" @confirm="confirmarEdicion" />
  
      <CategoriaShowDialog :model-value="showDialog" :categoria="categoriaSeleccionadaParaVer" @close="showDialog = false" />
    </v-card>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useCategoriaStore } from '../stores/categoriaStore'
  import type { Categoria } from '../types/Categoria'
  import CategoriaTable from '../components/CategoriaTable.vue'
  import CategoriaEditDialog from '../components/CategoriaEditDialog.vue'
  import CategoriaDeleteDialog from '../components/CategoriaDeleteDialog.vue'
  import CategoriaShowDialog from '../components/CategoriaShowDialog.vue'
  
  const store = useCategoriaStore()
  
  const editDialog = ref(false)
  const deleteDialog = ref(false)
  const showDialog = ref(false)
  const categoriaSeleccionada = ref<Categoria | null>(null)
  const categoriaSeleccionadaParaVer = ref<Categoria | null>(null)
  const modoEdicion = ref<'create' | 'edit'>('create')
  
  onMounted(() => {
    store.fetchCategorias()
  })
  
  function nuevaCategoria() {
    categoriaSeleccionada.value = null
    modoEdicion.value = 'create'
    editDialog.value = true
  }
  
  function editarCategoria(categoria: Categoria) {
    categoriaSeleccionada.value = categoria
    modoEdicion.value = 'edit'
    editDialog.value = true
  }
  
  function cerrarDialogEditar() {
    editDialog.value = false
    categoriaSeleccionada.value = null
  }
  
  function abrirDialogEliminar(categoria: Categoria) {
    categoriaSeleccionada.value = categoria
    deleteDialog.value = true
  }
  
  function cerrarDialogEliminar() {
    deleteDialog.value = false
    categoriaSeleccionada.value = null
    store.deleteError = null
  }
  
  function verCategoria(categoria: Categoria) {
    categoriaSeleccionadaParaVer.value = categoria
    showDialog.value = true
  }
  
  async function confirmarEliminacion() {
    if (categoriaSeleccionada.value) {
      const ok = await store.deleteCategoria(categoriaSeleccionada.value.id)
      if (ok) cerrarDialogEliminar()
    }
  }
  
  async function confirmarEdicion(categoria: Categoria) {
    const ok =
      modoEdicion.value === 'create'
        ? await store.createCategoria(categoria)
        : await store.updateCategoria(categoria)
  
    if (ok) {
      cerrarDialogEditar()
      store.fetchCategorias()
    }
  }
  </script>
  