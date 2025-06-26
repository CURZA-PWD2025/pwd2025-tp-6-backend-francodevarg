<template>
  <v-dialog v-model="model" max-width="600px">
    <v-card>
      <v-card-title>{{ proveedor?.id ? 'Editar Proveedor' : 'Nuevo Proveedor' }}</v-card-title>
      <v-card-text>
        <v-text-field label="Nombre" v-model="localProveedor.nombre" />
        <v-text-field label="Teléfono" v-model="localProveedor.telefono" />
        <v-text-field label="Direccion" v-model="localProveedor.direccion" />
        <v-text-field label="Email" v-model="localProveedor.email" />
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn text @click="$emit('cancel')">Cancelar</v-btn>
        <v-btn color="primary" text @click="guardar">Guardar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { watch, ref } from 'vue'
import type { Proveedor } from '../types/Proveedor'

const props = defineProps<{
  modelValue: boolean
  proveedor: Proveedor | null
}>()

const emit = defineEmits(['update:modelValue', 'cancel', 'confirm'])

const model = ref(props.modelValue)
watch(() => props.modelValue, val => (model.value = val))
watch(model, val => emit('update:modelValue', val))

const localProveedor = ref<Proveedor>({
  id: 0,
  nombre: '',
  telefono: '',
  direccion: '',
  email: ''
})

watch(
  () => props.proveedor,
  (nuevo) => {
    localProveedor.value = nuevo
      ? { ...nuevo }
      : { id: 0, nombre: '', telefono: '',  direccion: '',email: '' }
  },
  { immediate: true }
)

function guardar() {
  emit('confirm', localProveedor.value)
}
</script>
