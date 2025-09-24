<template>
    <div>
        <h2>Realizar Sorteo</h2>
        <button @click="draw">Generar Ganador</button>
        <div v-if="winner">Ganador: {{ winner.name }} ({{ winner.email }})</div>
    </div>
</template>

<script>
import API from '../services/api'
export default {
    data() { return { winner: null } },
    methods: {
        async draw() {
            try {
                const res = await API.post('admin/draw/')
                this.winner = res.data.winner
            } catch (e) { alert(e.response?.data?.detail || 'Error') }
        }
    }
}
</script>
