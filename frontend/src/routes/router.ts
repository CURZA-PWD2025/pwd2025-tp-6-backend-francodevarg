import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import HomeView from '../views/Home.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', component: HomeView },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router