<template>
    <q-page class="flex flex-center">
        
        <div>
            <p>Elige tu menu</p>
            <q-card>
                <q-card-section 
                    class="text-center text-white" 
                    style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
                     @click="goToMain"
                >
                    <strong>Carnes y vegetales </strong>
                    <br>
                </q-card-section>
            </q-card>
            <br>
            <br>
            <q-card>
                <q-card-section 
                    class="text-center text-white" 
                    style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
                    @click="goToMain"
                >
                    <strong>Vegetariano</strong>
                </q-card-section>
            </q-card>
            <br>
            <br>
            <q-card>
                <q-card-section 
                    class="text-center text-white" 
                    style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
                    @click="goToMain"
                >
                    <strong>Vegano</strong>
                </q-card-section>
            </q-card>
        </div>
    </q-page>
</template>

<script>
export default {
    name: 'Menu',
    methods: {
        goToMain: function () {
            this.$router.push('/dietasapp')
        }
    }
}
</script>
