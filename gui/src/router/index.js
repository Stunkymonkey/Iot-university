import Vue from 'vue'
import VueRouter from 'vue-router'
import Crows from '@/components/Crows.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/emulator/',
    name: 'Crows emulator',
    component: Crows,
  }, 
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
