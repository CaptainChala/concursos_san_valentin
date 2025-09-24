<template>
  <div>
    <h1>Inscríbete al Sorteo San Valentín</h1>
    <form @submit.prevent="submit">
      <input v-model="full_name" placeholder="Nombre completo" />
      <input v-model="email" placeholder="Email" />
      <input v-model="phone" placeholder="Teléfono" />
      <button type="submit">Registrarme</button>
    </form>

    <div v-if="message">{{ message }}</div>
    <div v-if="error" style="color:red">{{ error }}</div>

    
    <div style="margin-top: 20px;">
      <router-link to="/admin/login">
        <button>Login Admin</button>
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
      this.message = '';
      this.error = '';
      if (!this.full_name || !this.email || !this.phone) {
        this.error = 'Todos los campos son obligatorios.';
        return;
      }
      try {
        const res = await API.post('registro/', {
          nombre_completo: this.full_name,
          email: this.email,
          telefono: this.phone
        });
        this.message = res.data.detail;
      } catch (e) {
        this.error = JSON.stringify(e.response?.data) || e.message || 'Error';
      }
    }
  }
}
</script>
