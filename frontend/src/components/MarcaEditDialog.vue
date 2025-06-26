<template>
    <v-dialog
      :model-value="modelValue"
      @update:modelValue="$emit('update:modelValue', $event)"
      max-width="500"
    >
      <v-card>
        <v-card-title class="text-h6">{{ form.id ? 'Editar' : 'Crear' }} Marca</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="form.nombre"
            label="Nombre de la marca"
            required
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="$emit('cancel')">Cancelar</v-btn>
          <v-btn color="primary" @click="emitConfirm">Guardar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import type { Marca } from '../types/Marca'
  import { ref, watch } from 'vue'
  
  const props = defineProps<{
    modelValue: boolean
    marca: Marca | null
  }>()
  
  const emit = defineEmits<{
    (e: 'update:modelValue', value: boolean): void
    (e: 'cancel'): void
    (e: 'confirm', data: Marca): void
  }>()
  
  const form = ref<Marca>({ id: 0, nombre: '' })
  
  watch(() => props.marca, (val) => {
    if (val) form.value = { ...val }
    else form.value = { id: 0, nombre: '' }
  })
  
  function emitConfirm() {
    emit('confirm', { ...form.value })
  }
  </script>
  