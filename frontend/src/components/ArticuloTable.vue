<template>
    <v-data-table :items="articulos" :headers="headers" class="elevation-1" item-value="id">
      <template #item.categorias="{ item }">
        <v-chip
          v-for="categoria in item.categorias"
          :key="categoria.id"
          class="ma-1"
          small
          color="primary"
          label
        >
          {{ categoria.nombre }}
        </v-chip>
      </template>
  
      <template #item.marca="{ item }">
        {{ item.marca?.nombre || '-' }}
      </template>
  
      <template #item.proveedor="{ item }">
        {{ item.proveedor?.nombre || '-' }}
      </template>
  
      <template #item.actions="{ item }">
        <v-btn icon @click="$emit('show', item)">
          <v-icon>mdi-eye</v-icon>
        </v-btn>
        <v-btn icon @click="$emit('edit', item)">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn icon @click="$emit('delete', item)">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </template>
  
  <script setup lang="ts">
  import type { Articulo } from '../types/Articulo'
  import { computed } from 'vue'
  
  defineProps<{ articulos: Articulo[] }>()
  
  const headers = computed(() => [
    { title: 'ID', key: 'id' },
    { title: 'Descripción', key: 'descripcion' },
    { title: 'Precio', key: 'precio' },
    { title: 'Stock', key: 'stock' },
    { title: 'Marca', key: 'marca' },
    { title: 'Proveedor', key: 'proveedor' },
    { title: 'Categorías', key: 'categorias' },
    { title: 'Acciones', key: 'actions', sortable: false }
  ])
  </script>
  