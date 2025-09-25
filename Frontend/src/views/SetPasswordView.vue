<template>
  <div class="set-password-container">
    <h2 class="title">🔒 Crear contraseña</h2>

    <form class="password-form" @submit.prevent="submit">
      <input 
        v-model="password" 
        type="password" 
        placeholder="Nueva contraseña" 
        class="input"
        required
      />
      <button type="submit" class="btn submit-btn">
        Guardar contraseña
      </button>
    </form>

    <div v-if="loading" class="status loading">Procesando...</div>
    <div v-if="message" class="status success">{{ message }}</div>
    <div v-if="error" class="status error">{{ error }}</div>
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
      this.loading = true
      this.message = ''
      this.error = ''

      const urlParams = new URLSearchParams(window.location.search)
      const token = urlParams.get('token')

      if (!token) {
        this.error = 'Token de verificación no encontrado.'
        this.loading = false
        return
      }

      try {
        const res = await API.post('set-password/', {
          token,
          password: this.password
        })
        this.message = res.data.message
      } catch (e) {
        this.error = e.response?.data?.error || e.message || 'Error al guardar la contraseña.'
      }

      this.loading = false
    }
  }
}
</script>

<style scoped>
.set-password-container {
  max-width: 450px;
  margin: 60px auto;
  padding: 35px;
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

.password-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.input {
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 15px;
  outline: none;
  transition: border 0.2s ease-in-out;
}

.input:focus {
  border-color: #4caf50;
  box-shadow: 0 0 5px rgba(76, 175, 80, 0.4);
}

.btn {
  padding: 12px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  transition: all 0.2s ease-in-out;
}

.submit-btn {
  background: #4caf50;
  color: white;
}

.submit-btn:hover {
  background: #45a049;
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
