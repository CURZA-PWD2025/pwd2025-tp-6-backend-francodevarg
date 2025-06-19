<template>
    <v-navigation-drawer app permanent>
      <v-list nav dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          router
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </template>
  
  <script setup lang="ts">
  const items = [
    { title: 'Home', icon: 'mdi-home', to: '/' },
    { title: 'Profile', icon: 'mdi-account', to: '/profile' },
    { title: 'Settings', icon: 'mdi-cog', to: '/settings' },
  ]
  </script>
  