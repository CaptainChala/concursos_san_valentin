<template>
  <div class="verify-password-container">
    <h2 class="title">🔑 Verificar y crear contraseña</h2>

    <div v-if="statusMsg" class="status success">{{ statusMsg }}</div>

    <div v-if="showForm" class="form-section">
      <input 
        v-model="password" 
        type="password" 
        placeholder="Contraseña" 
        class="input"
      />
      <button class="btn submit-btn" @click="setPassword">
        Crear contraseña
      </button>
    </div>

    <div v-if="error" class="status error">{{ error }}</div>
  </div>
</template>

<script>
import API from '../services/api'

export default {
  data() {
    return {
      password: '',
      token: '',
      showForm: false,
      statusMsg: '',
      error: ''
    }
  },
  async mounted() {
    this.token = new URLSearchParams(window.location.search).get('token')
    if (!this.token) { 
      this.error = 'Token faltante'; 
      return 
    }
    try {
      const res = await API.get('verify/', { params: { token: this.token } })
      this.statusMsg = 'Verificado. Por favor crea tu contraseña.'
      this.showForm = true
    } catch (e) { 
      this.error = e.response?.data?.detail || 'Token inválido' 
    }
  },
  methods: {
    async setPassword() {
      try {
        const res = await API.post('set-password/', {
          token: this.token,
          password: this.password
        })
        this.statusMsg = res.data.detail
        this.showForm = false
      } catch (e) { 
        this.error = e.response?.data?.detail || 'Error' 
      }
    }
  }
}
</script>

<style scoped>
.verify-password-container {
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

.form-section {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 20px;
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

.success {
  background: #e8f5e9;
  color: #2e7d32;
}

.error {
  background: #ffebee;
  color: #c62828;
}
</style>
