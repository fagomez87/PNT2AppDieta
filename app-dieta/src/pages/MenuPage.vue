<template>
    <q-page class="flex flex-center">
        
        <div>
            <q-card class="my-card bg-purple text-white">
                <q-card-section>
                    <div class="text-h6">Elige tu opcion de menú</div>
                </q-card-section>

                <q-card-actions vertical>
                    <q-btn @click="updateMenu(1)">Carnes y vegetales</q-btn>
                    <q-btn @click="updateMenu(2)">Vegetariano</q-btn>
                    <q-btn @click="updateMenu(3)">Vegano</q-btn>
                </q-card-actions>
            </q-card>
        </div>
    </q-page>
</template>

<script>
export default {
    name: 'Menu',
    beforeCreate: function () {
        if (!this.$store.getters['isLogged']) {
            this.$router.push('/')
        }
    },
    methods: {
        updateMenu: function (id) {
            // traigo el id usuario
            let idUsuario = this.$store.getters['logData']
            
            const formData = new FormData()
            formData.set('idUsuario', idUsuario)
            formData.set('menu',id)
            this.$axios.put("http://127.0.0.1:9001/actualizarMenu", formData)
            .then((response) => {
                this.$router.push('/dietasapp')
                this.$q.notify({
                    color: 'green-4',
                    textColor: 'white',
                    icon: 'cloud_done',
                    message: 'Datos actualizados'
                })
            })
            .catch((error) => {
                this.$q.dialog({
                    title: 'Ooopss..',
                    message: 'No pudimos actualizar tus datos. Intenta nuevamente más tarde',
                    cancel: true,
                    persistent: true,
                })
            }) 
        }
    }
}
</script>
