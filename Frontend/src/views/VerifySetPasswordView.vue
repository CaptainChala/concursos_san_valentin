<template>
    <div>
        <h2>Verificar y crear contraseña</h2>
        <div v-if="statusMsg">{{ statusMsg }}</div>
        <div v-if="showForm">
            <input v-model="password" type="password" placeholder="Contraseña" />
            <button @click="setPassword">Crear contraseña</button>
        </div>
        <div v-if="error">{{ error }}</div>
    </div>
</template>

<script>
import API from '../services/api'
export default {
    data() {
        return {
            password: '', token: '', showForm: false, statusMsg: '',
            error: ''
        }
    },
    async mounted() {
        this.token = new URLSearchParams(window.location.search).get('token')
        if (!this.token) { this.error = 'Token faltante'; return }
        try {
            const res = await API.get('verify/', { params: { token: this.token } })
            this.statusMsg = 'Verificado. Por favor crea tu contraseña.'
            this.showForm = true
        } catch (e) { this.error = e.response?.data?.detail || 'Token inválido' }
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
            } catch (e) { this.error = e.response?.data?.detail || 'Error' }
        }
    }
}
</script>