<template>
    <v-dialog v-model="model" max-width="700px" @update:modelValue="(val) => { if (!val) emit('cancel') }">
      <v-card>
        <v-card-title>{{ isEdit ? 'Editar Artículo' : 'Nuevo Artículo' }}</v-card-title>
        <v-card-text>
          <v-text-field label="Descripción" v-model="form.descripcion" />
          <v-text-field label="Precio" v-model="form.precio" type="number" />
          <v-text-field label="Stock" v-model="form.stock" type="number" />
  
          <v-select
            label="Marca"
            :items="marcas"
            item-title="nombre"
            item-value="id"
            v-model="form.marca_id"
          />
  
          <v-select
            label="Proveedor"
            :items="proveedores"
            item-title="nombre"
            item-value="id"
            v-model="form.proveedor_id"
          />
  
          <v-select
            label="Categorías"
            :items="categorias"
            item-title="nombre"
            item-value="id"
            v-model="form.categoria_ids"
            multiple
            chips
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="emit('cancel')">Cancelar</v-btn>
          <v-btn color="primary" text @click="guardar">Guardar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import { ref, watch, computed } from 'vue'
  import type { Articulo } from '../types/Articulo'
  import { useMarcaStore } from '../stores/marcaStore'
  import { useProveedorStore } from '../stores/proveedorStore'
  import { useCategoriaStore } from '../stores/categoriaStore'
  
  const props = defineProps<{
    modelValue: boolean
    articulo: Articulo | null
  }>()
  
  const emit = defineEmits(['update:modelValue', 'cancel', 'confirm'])
  
  const model = ref(props.modelValue)
  watch(() => props.modelValue, val => model.value = val)
  watch(model, val => emit('update:modelValue', val))
  
  // Stores para los dropdowns
  const marcaStore = useMarcaStore()
  const proveedorStore = useProveedorStore()
  const categoriaStore = useCategoriaStore()
  
  const marcas = computed(() => marcaStore.marcas)
  const proveedores = computed(() => proveedorStore.proveedores)
  const categorias = computed(() => categoriaStore.categorias)
  
  const form = ref({
    descripcion: '',
    precio: 0,
    stock: 0,
    marca_id: null as number | null,
    proveedor_id: null as number | null,
    categoria_ids: [] as number[]
  })
  
  const isEdit = computed(() => !!props.articulo)
  
  watch(() => props.articulo, (nuevo) => {
    if (nuevo) {
      form.value = {
        descripcion: nuevo.descripcion,
        precio: parseFloat(nuevo.precio),
        stock: nuevo.stock,
        marca_id: nuevo.marca?.id ?? null,
        proveedor_id: nuevo.proveedor?.id ?? null,
        categoria_ids: nuevo.categorias?.map(c => c.id) ?? []
      }
    } else {
      form.value = {
        descripcion: '',
        precio: 0,
        stock: 0,
        marca_id: null,
        proveedor_id: null,
        categoria_ids: []
      }
    }
  }, { immediate: true })
  
  function guardar() {
    emit('confirm', { ...form.value })
  }
  
  // Cargar data de los selects al montar
  marcaStore.fetchMarcas()
  proveedorStore.fetchProveedores()
  categoriaStore.fetchCategorias()
  </script>
  