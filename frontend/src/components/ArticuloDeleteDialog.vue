<template>
    <v-dialog :model-value="modelValue" @update:modelValue="(val) => { if (!val) $emit('cancel') }" max-width="500">
      <v-card>
        <v-card-title class="text-h5">Eliminar artículo</v-card-title>
        <v-card-text>
          ¿Estás seguro que deseas eliminar el artículo "{{ articulo?.descripcion }}"?
          <v-alert v-if="error" type="error" dense class="mt-3">
            {{ error }}
          </v-alert>
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
  import type { Articulo } from '../types/Articulo'
  
  defineProps<{
    modelValue: boolean
    articulo: Articulo | null
    error: string | null
  }>()
  
  defineEmits(['cancel', 'confirm'])
  </script>
  