<template>
  <div class="registro-container">
    <h1 class="title">💌 Inscríbete al Sorteo San Valentín</h1>

    <form class="registro-form" @submit.prevent="submit">
      <input
        v-model="full_name"
        type="text"
        placeholder="Nombre completo"
        class="input"
      />
      <input
        v-model="email"
        type="email"
        placeholder="Email"
        class="input"
      />
      <input
        v-model="phone"
        type="tel"
        placeholder="Teléfono"
        class="input"
      />
      <button type="submit" class="btn submit-btn">
        Registrarme
      </button>
    </form>

    <div v-if="message" class="success">{{ message }}</div>
    <div v-if="error" class="error">{{ error }}</div>

    <div class="admin-link">
      <router-link to="/admin/login">
        <button class="btn admin-btn">Login Admin</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import API from '../services/api.js'

export default {
  data() {
    return {
      full_name: '',
      email: '',
      phone: '',
      message: '',
      error: ''
    }
  },
  methods: {
    async submit() {
      this.message = ''
      this.error = ''
      if (!this.full_name || !this.email || !this.phone) {
        this.error = 'Todos los campos son obligatorios.'
        return
      }
      try {
        const res = await API.post('registro/', {
          nombre_completo: this.full_name,
          email: this.email,
          telefono: this.phone
        })
        this.message = res.data.detail
      } catch (e) {
        this.error = JSON.stringify(e.response?.data) || e.message || 'Error'
      }
    }
  }
}
</script>

<style scoped>
.registro-container {
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
  margin-bottom: 25px;
  font-size: 24px;
  color: #333;
}

.registro-form {
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
  border-color: #e91e63;
  box-shadow: 0 0 5px rgba(233, 30, 99, 0.4);
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
  background: #e91e63;
  color: white;
}

.submit-btn:hover {
  background: #d81b60;
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

.admin-link {
  margin-top: 25px;
}

.admin-btn {
  background: #2196f3;
  color: white;
}

.admin-btn:hover {
  background: #1976d2;
}
</style>
