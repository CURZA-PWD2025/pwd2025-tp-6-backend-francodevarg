<template>
  <v-app>
    <v-layout>

      <Sidebar />
      
      <v-app-bar app color="primary" dark>
        <v-toolbar-title>Inventario de Tienda</v-toolbar-title>
      </v-app-bar>
      
      <v-main>
        <div class="mx-4 my-4">
          <router-view />
        </div>
      </v-main>
    </v-layout>
  </v-app>
</template>

<script setup lang="ts">
import Sidebar from './components/Sidebar.vue'
</script>

