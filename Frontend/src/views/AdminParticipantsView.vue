<template>
    <div>
        <h2>Participantes</h2>
        <ul>
            <li v-for="p in participants" :key="p.id">{{ p.full_name }} - {{
                p.email }} - {{ p.is_verified ? 'Verificado' : 'No' }}</li>
        </ul>
    </div>
</template>

<script>
import API from '../services/api'
export default {
    data() { return { participants: [] } },
    async mounted() {
        try {
            const res = await API.get('admin/participantes/')
            this.participants = res.data
        } catch (e) { console.error(e) }
    }
}
</script>
