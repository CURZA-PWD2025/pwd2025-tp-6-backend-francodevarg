<template>
  <v-dialog :model-value="modelValue" max-width="500"
    @update:modelValue="$emit('update:modelValue', $event)"
  >
    <v-card>
      <v-card-title class="text-h5">Eliminar proveedor</v-card-title>
      <v-card-text>
        ¿Estás seguro que deseas eliminar al proveedor "{{ proveedor?.nombre }}"?
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
import type { Proveedor } from '../types/Proveedor'

defineProps<{
  modelValue: boolean
  proveedor: Proveedor | null
  error: string | null
}>()

defineEmits(['cancel', 'confirm'])
</script>
