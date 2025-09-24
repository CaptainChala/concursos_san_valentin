<template>
  <div>
    <h2>Sorteo de Ganador</h2>

    <!-- Botón de regresar -->
    <button @click="$router.push('/admin/participantes')" style="margin-bottom: 20px;">
      ← Volver a Participantes
    </button>

    <button @click="generarGanador" :disabled="loading">
      {{ loading ? "Generando..." : "Generar Ganador" }}
    </button>

    <div v-if="ganador" style="margin-top: 20px;">
      <h3>¡Ganador!</h3>
      <p><strong>Nombre:</strong> {{ ganador.nombre }}</p>
      <p><strong>Email:</strong> {{ ganador.email }}</p>
    </div>

    <div v-if="error" style="color:red; margin-top: 10px;">{{ error }}</div>
  </div>
</template>

<script>
import API from '../services/api.js'

export default {
  data() {
    return {
      ganador: null,
      loading: false,
      error: ''
    }
  },
  methods: {
    async generarGanador() {
      this.loading = true
      this.error = ''
      this.ganador = null
      try {
        const res = await API.post('admin/sorteo/', {}, {
          headers: { Authorization: `Token ${localStorage.getItem('token')}` }
        })
        this.ganador = res.data
      } catch (e) {
        this.error = e.response?.data?.error || e.message || 'Error al generar ganador'
      }
      this.loading = false
    }
  }
}
</script>
