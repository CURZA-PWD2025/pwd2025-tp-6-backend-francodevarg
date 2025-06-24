<template>
  <v-navigation-drawer app permanent>
    <v-list nav dense>
      <v-list-item 
        v-for="item in items" 
        :key="item.title" 
        :to="item.to" 
        router link 
        :prepend-icon="item.icon">
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>

    </v-list>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
const items = [
  { title: 'Marcas', icon: 'mdi-tag-multiple', to: '/marcas' },
  { title: 'Categorías', icon: 'mdi-shape', to: '/categorias' },
  { title: 'Proveedores', icon: 'mdi-truck-delivery', to: '/proveedores' },
  { title: 'Artículos', icon: 'mdi-cube-outline', to: '/articulos' },
]
</script>