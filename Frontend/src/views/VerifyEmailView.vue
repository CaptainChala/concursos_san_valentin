<template>
  <div class="verification-container">
    <h2 class="title">✉️ Verificación de correo</h2>

    <div v-if="loading" class="status loading">Verificando...</div>
    <div v-else-if="message" class="status success">{{ message }}</div>
    <div v-else-if="error" class="status error">{{ error }}</div>
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
    const urlParams = new URLSearchParams(window.location.search)
    const token = urlParams.get('token')

    if (!token) {
      this.error = 'Token de verificación no encontrado.'
      this.loading = false
      return
    }

    try {
      const res = await API.get(`verificar/?token=${token}`)
      this.message = res.data.message

      if (res.data.message && res.data.message.includes('Correo verificado')) {
        setTimeout(() => {
          window.location.href = `/set-password?token=${token}`
        }, 1500)
      }
    } catch (e) {
      this.error = e.response?.data?.error || e.message || 'Error al verificar.'
    }

    this.loading = false
  }
}
</script>

<style scoped>
.verification-container {
  max-width: 500px;
  margin: 80px auto;
  padding: 30px;
  background: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.title {
  font-size: 24px;
  margin-bottom: 25px;
  color: #333;
}

.status {
  font-size: 16px;
  font-weight: bold;
  padding: 15px 20px;
  border-radius: 8px;
  margin-top: 20px;
}

.loading {
  background: #fff3e0;
  color: #ff9800;
}

.success {
  background: #e8f5e9;
  color: #2e7d32;
}

.error {
  background: #ffebee;
  color: #c62828;
}
</style>
