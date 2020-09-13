<template>
  <div class="q-pa-md q-gutter-sm">

    <q-img
      :src="require('../assets/grafico.png')"
      spinner-color="white"
      style="position:'center center-flex'"
    />
    <q-btn label="Volver" @click="volver" color="secondary"/>
  </div>
</template>

<script>
export default {
    name:'ReportesPage',
    beforeCreate: function () {
        if (!this.$store.getters['isLogged']) {
            this.$router.push('/')
        }
    },
    methods: {
        volver: function(){
            this.$router.push('/dietasapp')
        }
    }
}
</script>