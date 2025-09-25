<template>
  <div class="participantes-container">
    <h2 class="title">👥 Listado de Participantes</h2>

    <div class="actions">
      <button
        class="btn sorte-btn"
        @click="$router.push('/admin/sorteo')"
        :disabled="!participants.some(p => p.verificado)"
      >
        Ingresar al Sorteo
      </button>

      <input
        v-model="search"
        placeholder="🔍 Buscar por nombre o correo"
        @input="filterList"
        class="input search-input"
      />
    </div>

    <div v-if="loading" class="loading">Cargando participantes...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <table v-if="filteredParticipants.length > 0" class="participants-table">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Correo</th>
          <th>Verificado</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in filteredParticipants" :key="p.id">
          <td>{{ p.nombre_completo }}</td>
          <td>{{ p.email }}</td>
          <td>
            <span :class="['badge', p.verificado ? 'badge-success' : 'badge-fail']">
              {{ p.verificado ? 'Sí' : 'No' }}
            </span>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-else-if="!loading && !error" class="no-data">
      No se encontraron participantes.
    </div>
  </div>
</template>

<script>
import API from '../services/api.js'

export default {
  data() {
    return {
      participants: [],
      filteredParticipants: [],
      search: '',
      loading: false,
      error: ''
    }
  },
  methods: {
    async fetchParticipants() {
      this.loading = true
      this.error = ''
      try {
        const res = await API.get('admin/participantes/', {
          headers: { Authorization: `Token ${localStorage.getItem('token')}` }
        })
        this.participants = res.data
        this.filteredParticipants = this.participants
      } catch (e) {
        this.error = e.response?.data?.error || e.message || 'Error al cargar participantes'
      }
      this.loading = false
    },
    filterList() {
      const term = this.search.toLowerCase()
      this.filteredParticipants = this.participants.filter(
        p =>
          p.nombre_completo.toLowerCase().includes(term) ||
          p.email.toLowerCase().includes(term)
      )
    }
  },
  mounted() {
    this.fetchParticipants()
  }
}
</script>

<style scoped>
.participantes-container {
  max-width: 800px;
  margin: 50px auto;
  padding: 30px;
  background: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.title {
  text-align: center;
  margin-bottom: 25px;
  font-size: 26px;
  color: #333;
}

.actions {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  gap: 10px;
}

.input {
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ccc;
  flex: 1;
  font-size: 15px;
  outline: none;
  transition: border 0.2s ease-in-out;
}

.input:focus {
  border-color: #4caf50;
  box-shadow: 0 0 5px rgba(76, 175, 80, 0.4);
}

.btn {
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 15px;
  transition: all 0.2s ease-in-out;
}

.sorte-btn {
  background: #4caf50;
  color: white;
  font-weight: bold;
}

.sorte-btn:disabled {
  background: #a5d6a7;
  cursor: not-allowed;
}

.sorte-btn:hover:not(:disabled) {
  background: #45a049;
}

.participants-table {
  width: 100%;
  border-collapse: collapse;
  border-radius: 12px;
  overflow: hidden;
  background: white;
}

.participants-table th, 
.participants-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.participants-table th {
  background: #f0f0f0;
  font-weight: bold;
}

.participants-table tr:hover {
  background: #f9f9f9;
}

.badge {
  padding: 5px 12px;
  border-radius: 12px;
  font-size: 13px;
  font-weight: bold;
}

.badge-success {
  background: #c8e6c9;
  color: #2e7d32;
}

.badge-fail {
  background: #ffcdd2;
  color: #c62828;
}

.loading {
  text-align: center;
  margin-top: 15px;
  font-style: italic;
  color: #666;
}

.error {
  color: red;
  margin-top: 15px;
  font-weight: bold;
  text-align: center;
}

.no-data {
  text-align: center;
  margin-top: 20px;
  font-style: italic;
  color: #777;
}
</style>
