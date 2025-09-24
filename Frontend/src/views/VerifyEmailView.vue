<template>
  <div>
    <h2>Verificación de correo</h2>
    <div v-if="loading">Verificando...</div>
    <div v-else-if="message">{{ message }}</div>
    <div v-else-if="error" style="color:red">{{ error }}</div>
  </div>
</template>

<script>
import API from '../services/api.js'
export default {
  data() {
    return {
      loading: true,
      message: '',
      error: ''
    }
  },
  async mounted() {
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token');
    if (!token) {
      this.error = 'Token de verificación no encontrado.';
      this.loading = false;
      return;
    }
    try {
      const res = await API.get(`verificar/?token=${token}`);
      this.message = res.data.message;
      
      if (res.data.message && res.data.message.includes('Correo verificado')) {
        setTimeout(() => {
          window.location.href = `/set-password?token=${token}`;
        }, 1500);
      }
    } catch (e) {
      this.error = e.response?.data?.error || e.message || 'Error al verificar.';
    }
    this.loading = false;
  }
}
</script>
