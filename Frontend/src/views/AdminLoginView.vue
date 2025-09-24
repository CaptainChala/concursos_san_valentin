<template>
  <div>
    <h2>Login Admin</h2>
    <form @submit.prevent="submit">
      <input v-model="email" placeholder="Email" />
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
      email: '',
      password: '',
      message: '',
      error: ''
    }
  },
  methods: {
    async submit() {
      this.message = '';
      this.error = '';
      if (!this.email || !this.password) {
        this.error = 'Todos los campos son obligatorios.';
        return;
      }
      try {
        const res = await API.post('admin/login/', {
          email: this.email,
          password: this.password
        });
        this.message = res.data.message || 'Login exitoso';
        // Aquí podrías guardar un token o redirigir a admin panel
      } catch (e) {
        this.error = JSON.stringify(e.response?.data) || e.message || 'Error';
      }
    }
  }
}
</script>
