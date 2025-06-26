<template>
<v-dialog
  :model-value="modelValue"
  @update:modelValue="$emit('update:modelValue', $event)"
  max-width="400"
>
      <v-card>
        <v-card-title class="text-h6">¿Eliminar marca {{ marca?.nombre }}?</v-card-title>
        <v-card-text>
          ¿Estás seguro de que querés eliminar <strong>{{ marca?.nombre }}</strong>?
        </v-card-text>
        <v-card-text class="text-caption text-error" v-if="error">
          {{ error }}
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="$emit('cancel')">Cancelar</v-btn>
          <v-btn color="error" @click="$emit('confirm')">Eliminar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import type { Marca } from '../types/Marca'
  
  defineProps<{
  modelValue: boolean
  marca: Marca | null
  error: string | null
}>()

defineEmits<{
  (e: 'update:modelValue', value: boolean): void
  (e: 'cancel'): void
  (e: 'confirm'): void
}>()
  </script>
  