<template>
  <header class="navbar">
    <div class="container">
      <div class="logo">Dolce Passo</div>
      <nav class="nav">
        <RouterLink to="/">Inicio</RouterLink>
      </nav>
    </div>
  </header>
  <main class="container">
    <router-view />
  </main>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.navbar {
  background-color: #fff;
  border-bottom: 1px solid #eee;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  padding: 1.5rem 0;
}

.container {
  width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.8rem;
  font-weight: 700;
  color: #111;
}

.nav a {
  margin-left: 2rem;
  font-size: 1.05rem;
  font-weight: 500;
  color: #333;
  transition: color 0.3s ease;
}

.nav a:hover {
  color: #f39c12;
}
</style>