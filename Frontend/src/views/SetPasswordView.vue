<template>
  <div>
    <h2>Crear contraseña</h2>
    <form @submit.prevent="submit">
      <input v-model="password" type="password" placeholder="Nueva contraseña" required />
      <button type="submit">Guardar contraseña</button>
    </form>
    <div v-if="loading">Procesando...</div>
    <div v-if="message">{{ message }}</div>
    <div v-if="error" style="color:red">{{ error }}</div>
  </div>
</template>

<script>
import API from '../services/api.js'
export default {
  data() {
    return {
      password: '',
      loading: false,
      message: '',
      error: ''
    }
  },
  methods: {
    async submit() {
      this.loading = true;
      this.message = '';
      this.error = '';
      const urlParams = new URLSearchParams(window.location.search);
      const token = urlParams.get('token');
      if (!token) {
        this.error = 'Token de verificación no encontrado.';
        this.loading = false;
        return;
      }
      try {
        const res = await API.post('set-password/', {
          token,
          password: this.password
        });
        this.message = res.data.message;
      } catch (e) {
        this.error = e.response?.data?.error || e.message || 'Error al guardar la contraseña.';
      }
      this.loading = false;
    }
  }
}
</script>
