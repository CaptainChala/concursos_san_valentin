<template>
  <div class="sorteo-container">
    <h2 class="title">🎉 Sorteo de Ganador 🎉</h2>

    <div class="buttons">
      <button class="btn back-btn" @click="$router.push('/admin/participantes')">
        ← Volver a Participantes
      </button>

      <button class="btn generate-btn" @click="generarGanador" :disabled="loading">
        {{ loading ? "Generando..." : "Generar Ganador" }}
      </button>
    </div>

    <div v-if="ganador" class="ganador-card">
      <h3>¡Ganador!</h3>
      <p><strong>Nombre:</strong> {{ ganador.nombre }}</p>
      <p><strong>Email:</strong> {{ ganador.email }}</p>
    </div>

    <div v-if="error" class="error">{{ error }}</div>
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

<style scoped>
.sorteo-container {
  max-width: 500px;
  margin: 40px auto;
  padding: 30px;
  background: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.title {
  margin-bottom: 25px;
  color: #333;
  font-size: 28px;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 30px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.2s ease-in-out;
}

.back-btn {
  background: #ddd;
  color: #333;
}

.back-btn:hover {
  background: #ccc;
}

.generate-btn {
  background: #4caf50;
  color: white;
}

.generate-btn:disabled {
  background: #a5d6a7;
  cursor: not-allowed;
}

.generate-btn:hover:not(:disabled) {
  background: #45a049;
}

.ganador-card {
  margin-top: 20px;
  padding: 20px;
  border-radius: 12px;
  background: #fffbe6;
  border: 1px solid #ffe58f;
}

.error {
  color: red;
  margin-top: 15px;
  font-weight: bold;
}
</style>
