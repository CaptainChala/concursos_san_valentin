import { createRouter, createWebHistory } from 'vue-router'
import RegisterView from '../views/RegisterView.vue'
import VerifySetPasswordView from '../views/VerifySetPasswordView.vue'
import VerifyEmailView from '../views/VerifyEmailView.vue'
import SetPasswordView from '../views/SetPasswordView.vue'
import AdminLoginView from '../views/AdminLoginView.vue'
import AdminParticipantsView from '../views/AdminParticipantsView.vue'
import AdminDrawView from '../views/AdminDrawView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: RegisterView },
    { path: '/verificar', component: VerifyEmailView },
  { path: '/verify', component: VerifySetPasswordView },
  { path: '/set-password', component: SetPasswordView },
  { path: '/admin/login', component: AdminLoginView },
  { path: '/admin/participantes', component: AdminParticipantsView },
  { path: '/admin/sorteo', component: AdminDrawView },],
})

export default router
