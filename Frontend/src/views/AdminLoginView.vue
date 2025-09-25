<template>
  <div class="login-container">
    <h2 class="title">🔑 Login Admin</h2>

    <form class="login-form" @submit.prevent="submit">
      <input 
        v-model="username" 
        type="text" 
        placeholder="Usuario" 
        class="input"
      />

      <input 
        v-model="password" 
        type="password" 
        placeholder="Contraseña" 
        class="input"
      />

      <button type="submit" class="btn login-btn">
        Ingresar
      </button>
    </form>

    <div v-if="message" class="success">{{ message }}</div>
    <div v-if="error" class="error">{{ error }}</div>
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
      this.message = ''
      this.error = ''

      if (!this.username || !this.password) {
        this.error = 'Todos los campos son obligatorios.'
        return
      }

      try {
        const res = await API.post('admin/login/', {
          username: this.username,
          password: this.password
        })

        this.message = res.data.message || 'Login exitoso'
        this.$router.push('/admin/participantes')
      } catch (e) {
        this.error = e.response?.data?.error || e.message || 'Error'
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 60px auto;
  padding: 35px;
  background: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.title {
  margin-bottom: 25px;
  font-size: 26px;
  color: #333;
}

.login-form {
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
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.2s ease-in-out;
}

.login-btn {
  background: #4caf50;
  color: white;
  font-weight: bold;
}

.login-btn:hover {
  background: #45a049;
}

.success {
  margin-top: 15px;
  color: #2e7d32;
  font-weight: bold;
}

.error {
  margin-top: 15px;
  color: red;
  font-weight: bold;
}
</style>
