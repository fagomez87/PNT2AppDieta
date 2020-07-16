<template>
  <div class="q-pa-md q-gutter-sm">
    <q-input 
        filled 
        v-model="text" 
        label="Descripción del proyecto" 
        readonly>
    </q-input>
    <br/>
    <q-input 
        filled 
        type="textarea"
        v-model="integrantes" 
        label="Integrantes" 
        readonly>
    </q-input>
    <br/>

    <q-btn label="Volver" @click="volver" color="secondary"/>
  </div>
</template>

<script>
export default {
    name:'ContactoPage',
    data () {
        return {
            text: 'App de seguimiento y control de comidas',
            integrantes: 'Bidart, Mónica\nBrizuela, Nadia\nGomez, Fernando' 
        }
    },
    methods: {
        volver: function(){
            this.$router.push('/dietasapp')
        }
    }
}
</script>