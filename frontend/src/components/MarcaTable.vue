<template>
    <v-data-table-virtual
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
          <v-icon size="20" class="me-2" color="primary" @click="$emit('edit', item)">mdi-pencil</v-icon>
          <v-icon size="20" color="error" @click="$emit('delete', item)">mdi-delete</v-icon>
        </div>
      </template>
  
      <template #bottom>
        <div class="d-flex justify-end align-center px-4 py-2 text-medium-emphasis text-caption">
          Total de marcas: <strong class="ml-1">{{ marcas.length }}</strong>
        </div>
      </template>
    </v-data-table-virtual>
  </template>
  
  <script setup lang="ts">
  import type { Marca } from '../types/Marca'
  
defineProps<{
    marcas: Marca[]
  }>()
  
defineEmits<{
    (e: 'edit', item: Marca): void
    (e: 'delete', item: Marca): void
  }>()
  
  const headers = [
    { title: 'ID', key: 'id', align: 'start', sortable: true },
    { title: 'Nombre', key: 'nombre', align: 'start', sortable: true },
    { title: 'Acciones', key: 'acciones', align: 'center', sortable: false },
  ] as const
  </script>
  