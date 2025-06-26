<template>
  <v-dialog :model-value="modelValue" max-width="500" @update:modelValue="(val) => { if (!val) $emit('close') }">
    <v-card>
      <v-card-title>Detalle del Proveedor: {{ proveedor?.id }}</v-card-title>
      <v-card-text>
        <v-list dense>
          <v-list-item>
            <v-list-item-title><strong>Nombre:</strong> {{ proveedor?.nombre }}</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title><strong>Teléfono:</strong> {{ proveedor?.telefono }}</v-list-item-title>
          </v-list-item>
            <v-list-item>
            <v-list-item-title><strong>Direccion:</strong> {{ proveedor?.direccion }}</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title><strong>Email:</strong> {{ proveedor?.email }}</v-list-item-title>
          </v-list-item>
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
import type { Proveedor } from '../types/Proveedor'

defineProps<{
  modelValue: boolean
  proveedor: Proveedor | null
}>()

defineEmits(['close'])
</script>
