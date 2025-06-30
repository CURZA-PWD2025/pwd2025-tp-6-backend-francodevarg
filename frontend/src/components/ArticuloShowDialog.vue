<template>
    <v-dialog :model-value="modelValue" @update:modelValue="(val) => { if (!val) $emit('close') }" max-width="600">
      <v-card>
        <v-card-title>Detalle del Artículo</v-card-title>
        <v-card-text>
          <v-list density="compact">
            <v-list-item><v-list-item-title><strong>ID:</strong> {{ articulo?.id }}</v-list-item-title></v-list-item>
            <v-list-item><v-list-item-title><strong>Descripción:</strong> {{ articulo?.descripcion }}</v-list-item-title></v-list-item>
            <v-list-item><v-list-item-title><strong>Precio:</strong> ${{ articulo?.precio }}</v-list-item-title></v-list-item>
            <v-list-item><v-list-item-title><strong>Stock:</strong> {{ articulo?.stock }}</v-list-item-title></v-list-item>
            <v-list-item><v-list-item-title><strong>Marca:</strong> {{ articulo?.marca?.nombre }}</v-list-item-title></v-list-item>
            <v-list-item><v-list-item-title><strong>Proveedor:</strong> {{ articulo?.proveedor?.nombre }}</v-list-item-title></v-list-item>
            <v-list-item>
              <v-list-item-title><strong>Categorías:</strong></v-list-item-title>
              <v-chip
                v-for="categoria in articulo?.categorias || []"
                :key="categoria.id"
                class="ma-1"
                color="primary"
                small
                label
              >
                {{ categoria.nombre }}
              </v-chip>
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
  import type { Articulo } from '../types/Articulo'
  
  defineProps<{
    modelValue: boolean
    articulo: Articulo | null
  }>()
  
  defineEmits(['close'])
  </script>
  