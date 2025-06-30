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

    </v-card>
  </template>
  
  <script setup lang="ts">
  import {ref,onMounted } from 'vue'
  import { useArticuloStore } from '../stores/articuloStore'
  import type { Articulo } from '../types/Articulo'
  import ArticuloTable from '../components/ArticuloTable.vue'
  import ArticuloShowDialog from '../components/ArticuloShowDialog.vue'

  const articuloSeleccionado = ref<Articulo | null>(null)
  const showDialog = ref(false)

  const store = useArticuloStore()
  
  onMounted(() => {
    store.fetchArticulos()
  })
  
  function nuevoArticulo() {
    console.log('nuevo artículo') 
  }
  function verArticulo(articulo: Articulo) {
  articuloSeleccionado.value = articulo
  showDialog.value = true
}

  
  function editarArticulo(articulo: Articulo) {
    console.log('editar artículo', articulo) 
  }
  
  function abrirDialogEliminar(articulo: Articulo) {
    console.log('eliminar artículo', articulo)   }
  </script>
  