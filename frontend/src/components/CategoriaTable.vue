<template>
    <v-data-table :items="categorias" :headers="headers" class="elevation-1">
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
  import type { Categoria } from '../types/Categoria'
  import { computed } from 'vue'
  
  defineProps<{ categorias: Categoria[] }>()
  
  const headers = computed(() => [
    { title: 'ID', key: 'id' },
    { title: 'Nombre', key: 'nombre' },
    { title: 'Acciones', key: 'actions', sortable: false }
  ])
  </script>
  