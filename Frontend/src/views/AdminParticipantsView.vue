<template>
  <div>
    <h2>Listado de Participantes</h2>

    <!-- Input de búsqueda -->
    <input
      v-model="search"
      placeholder="Buscar por nombre o correo"
      @input="filterList"
    />

    <table border="1" cellpadding="5">
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
          <td>{{ p.verificado ? 'Sí' : 'No' }}</td>
        </tr>
      </tbody>
    </table>

    <div v-if="loading">Cargando participantes...</div>
    <div v-if="error" style="color:red">{{ error }}</div>
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
        const res = await API.get('admin/participantes/')
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
