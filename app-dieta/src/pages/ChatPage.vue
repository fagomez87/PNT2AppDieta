<template>
  <div class="q-pa-md q-gutter-sm">

    <q-img
      :src="url"
      spinner-color="white"
      style="position:'center center-flex'"
    />
    <q-btn label="Volver" @click="volver" color="secondary"/>
  </div>
</template>

<script>
export default {
    name:'chatPage',
    data () {
        return {
            url: 'https://patagonianqueengf.com/wp-content/uploads/2013/11/website-construction-graphic-4.jpg'
        }
    },
    methods: {
        volver: function(){
            this.$router.push('/dietasapp')
        }
    }
}
</script>