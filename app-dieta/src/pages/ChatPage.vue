<template>
  <div class="q-pa-md q-gutter-sm">

    <q-img
      :src="require('../assets/website-construction-graphic-4.jpg')"
      spinner-color="white"
      style="position:'center center-flex'"
    />
    <q-btn label="Volver" @click="volver" color="secondary"/>
  </div>
</template>

<script>
export default {
    name:'chatPage',
    methods: {
        volver: function(){
            this.$router.push('/dietasapp')
        }
    }
}
</script>