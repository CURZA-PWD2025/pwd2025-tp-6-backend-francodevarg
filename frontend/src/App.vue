<template>
  <v-app>
    <Sidebar />

    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Administracion de Tienda</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import Sidebar from './components/Sidebar.vue'
</script>

