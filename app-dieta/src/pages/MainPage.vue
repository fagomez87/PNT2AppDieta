<template>
    <q-page class="flex flex-center">
        <div>
            <q-card>
                <q-card-section 
                    class="text-center text-white" 
                    style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
                     @click="realizadas"
                >
                    <strong>Que comiste</strong>
                    <br>
                </q-card-section>
            </q-card>
            <br>
            <br>
            <q-card>
                <q-card-section 
                    class="text-center text-white" 
                    style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
                    @click="opciones"
                >
                    <strong>Opciones de comidas</strong>
                </q-card-section>
            </q-card>
        </div>
    </q-page>
</template>

<script>
export default {
    name: 'MainPage',
    beforeCreate: function () {
        if (!this.$store.getters['isLogged']) {
            this.$router.push('/')
        }
    },
    methods: {
        realizadas: function () {
            this.$router.push('realizadas')
        },
        opciones: function () {
            this.$router.push('opcionesComidas')
        }
    }
}
</script>
