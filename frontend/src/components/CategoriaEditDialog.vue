<template>
    <v-dialog v-model="model" max-width="600px" @update:modelValue="(val) => { if (!val) emit('cancel') }">
      <v-card>
        <v-card-title>{{ categoria?.id ? 'Editar Categoría' : 'Nueva Categoría' }}</v-card-title>
        <v-card-text>
          <v-text-field label="Nombre" v-model="localCategoria.nombre" />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="emit('cancel')">Cancelar</v-btn>
          <v-btn color="primary" text @click="emit('confirm', localCategoria)">Guardar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import { ref, watch } from 'vue'
  import type { Categoria } from '../types/Categoria'
  
  const props = defineProps<{ modelValue: boolean; categoria: Categoria | null }>()
  const emit = defineEmits(['update:modelValue', 'cancel', 'confirm'])
  
  const model = ref(props.modelValue)
  watch(() => props.modelValue, val => (model.value = val))
  watch(model, val => emit('update:modelValue', val))
  
  const localCategoria = ref<Categoria>({ id: 0, nombre: '' })
  
  watch(() => props.categoria, nuevo => {
    localCategoria.value = nuevo ? { ...nuevo } : { id: 0, nombre: '' }
  }, { immediate: true })
  </script>
  