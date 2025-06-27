<template>
    <v-dialog :model-value="modelValue" @update:modelValue="(val) => { if (!val) $emit('close') }" max-width="500">
      <v-card>
        <v-card-title>Detalle de la Categoría</v-card-title>
        <v-card-text>
          <v-list dense>
            <v-list-item><v-list-item-title><strong>ID:</strong> {{ categoria?.id }}</v-list-item-title></v-list-item>
            <v-list-item><v-list-item-title><strong>Nombre:</strong> {{ categoria?.nombre }}</v-list-item-title></v-list-item>
          </v-list>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="$emit('close')">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import type { Categoria } from '../types/Categoria'
  
  defineProps<{ modelValue: boolean; categoria: Categoria | null }>()
  defineEmits(['close'])
  </script>