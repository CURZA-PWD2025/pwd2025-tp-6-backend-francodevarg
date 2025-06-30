<template>
    <div>
        <h1>Bienvenido a la aplicación de gestión de artículos</h1>
        <p>Redirigiendo a la lista de artículos...</p>
        <v-progress-circular indeterminate color="primary" />
    </div>
</template>
  
<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
    console.log('Home component loaded')
    router.push('/articulos')
})

</script>