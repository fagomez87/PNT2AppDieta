<template>
  <div class="q-pa-md q-gutter-sm">
    <q-form
      v-on:submit="send"
    >
      <q-input 
        color="teal" 
        v-model="subject" 
        label="Asunto"
        :rules="[ val => val && val.length > 0 || 'El asunto no puede estar vacío']"
      />
      <q-input 
        color="teal" 
        type="textarea" 
        v-model="description" 
        label="Descripcion"
        :rules="[ val => val && val.length > 0 || 'Pon una descripción de tu problema']"
      />
      <br/>
      <q-btn label="Enviar" type="submit" color="accent"/>
      <q-btn label="Cancelar" @click="reset" color="negative" flat/>
    </q-form>
  </div>
</template>

<script>
//import emailjs from 'emailjs-com';
export default {
    name:'ChatPage',
    data () {
      return {
        subject:'',
        description:''
      }
    },
    methods: {
      send: function() {
        // ESTO SE USA PARA EL ENVÍO DE MAIL
        const formData = new FormData()
        formData.set('subject', this.subject)
        formData.set('description', this.description)
        // ENVÍO DE MAIL A NUESTRA CASILLA DE CORREO DE SOPORTE
        // emailjs.sendForm('YOUR_SERVICE_ID','YOUR_TEMPLATE_ID',formData, 'YOUR_USER_ID')
        // .then((result) => {
        // })
        this.$router.push('/dietasapp')
          this.$q.notify({
            color: 'green-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Tu mensaje ha sido enviado exitosamente'
          })
      }, 
      reset: function(){
          this.$router.push('/dietasapp')
      }
    }
}
</script>