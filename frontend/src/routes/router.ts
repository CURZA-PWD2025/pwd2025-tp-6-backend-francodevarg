import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import HomeView from '../views/Home.vue'
import MarcasView from '../views/Marcas.vue'
import ProveedoresView from '../views/Proveedores.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', component: HomeView },
  { path: '/marcas', component: MarcasView },
  { path: '/proveedores', component: ProveedoresView },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router