<template>
    <v-dialog :model-value="modelValue" @update:modelValue="(val) => { if (!val) $emit('cancel') }" max-width="500">
      <v-card>
        <v-card-title class="text-h5">Eliminar Categoría</v-card-title>
        <v-card-text>
          ¿Estás seguro que deseas eliminar la categoría "{{ categoria?.nombre }}"?
          <div v-if="error" class="text-error mt-2">{{ error }}</div>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="$emit('cancel')">Cancelar</v-btn>
          <v-btn color="red" text @click="$emit('confirm')">Eliminar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import type { Categoria } from '../types/Categoria'
  
  defineProps<{ modelValue: boolean; categoria: Categoria | null; error: string | null }>()
  defineEmits(['cancel', 'confirm'])
  </script>