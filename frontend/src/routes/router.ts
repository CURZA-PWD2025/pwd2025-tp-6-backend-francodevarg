import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import HomeView from '../views/Home.vue'
import MarcasView from '../views/Marcas.vue'
import ProveedoresView from '../views/Proveedores.vue'
import CategoriasView from '../views/Categorias.vue'
import ArticulosView from '../views/Articulos.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', component: HomeView },
  { path: '/marcas', component: MarcasView },
  { path: '/proveedores', component: ProveedoresView },
  { path: '/categorias', component: CategoriasView },
  { path: '/articulos', component: ArticulosView },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router