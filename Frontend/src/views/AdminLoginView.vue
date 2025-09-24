<template>
  <div>
    <h2>Login Admin</h2>
    <form @submit.prevent="submit">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Contraseña" />
      <button type="submit">Ingresar</button>
    </form>

    <div v-if="message">{{ message }}</div>
    <div v-if="error" style="color:red">{{ error }}</div>
  </div>
</template>

<script>
import API from '../services/api.js'

export default {
  data() {
    return {
      username: '',
      password: '',
      message: '',
      error: ''
    }
  },
  methods: {
    async submit() {
      this.message = '';
      this.error = '';

      if (!this.username || !this.password) {
        this.error = 'Todos los campos son obligatorios.';
        return;
      }

      try {
        const res = await API.post('admin/login/', {
          username: this.username,
          password: this.password
        });

        this.message = res.data.message || 'Login exitoso';

        // ✅ Redirigir a AdminParticipantsView después del login exitoso
        this.$router.push('/admin/participantes');

      } catch (e) {
        this.error = e.response?.data?.error || e.message || 'Error';
      }
    }
  }
}
</script>
