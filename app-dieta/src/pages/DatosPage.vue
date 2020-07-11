<template> 
  <q-page class="flex flex-center">
    <div color="primary">
        <h4>Mi información</h4>
    </div>
    <div>
      <q-form
        v-on:submit="update"
      >
      <q-input
        filled
        v-model="nombre"
        label="nombre"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor ingrese su nombre']"
      />
      <q-input
        filled
        v-model="apellido"
        label="apellido"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor ingrese su apellido']"
      />
      <q-input
        filled
        v-model="usuario"
        label="usuario"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor ingrese su nombre de usuario']"
      />
      <q-input
        filled
        type="password"
        v-model="password"
        label="Contraseña"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor ingrese su contraseña']"
      />
      <q-input
        filled
        v-model="mail"
        label="Email"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor ingrese su correo']"
      />
      <q-input
        filled
        v-model="peso"
        label="peso"
        type="number"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor ingrese su peso']"
      />
      <q-input
        filled
        v-model="altura"
        label="altura"
        type="number"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Por favor ingrese su altura']"
      />
      <q-select
        filled
        clearable
        v-model="options[menu-1]"
        label="menu"
        :options="options"
        :rules="['Seleccione una por favor']" 
      />
      <br/>
      <div>
          <q-btn label="Actualizar" type="submit" color="secondary" />
          <q-btn label="Cancelar" @click="volver" color="secondary" flat class="q-ml-sm" />
      </div>
    </q-form>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'DatosPage',
  data () {
    return {
      nombre: '',
      apellido: '',
      usuario: '',
      password: '',
      mail: '',
      peso: '',
      altura: '',
      menu: '',
      model: null,
      options: ["Carnes y vegetales", "Vegetariano", "Vegano"]
    }
  },
  beforeMount() {
      let id = this.$store.getters["logData"]
      this.$axios.get('http://127.0.0.1:9001/getUser', {params:{idUsuario:id}})
        .then((response) => {
            this.nombre = response.data.nombre
            this.apellido = response.data.apellido
            this.usuario = response.data.user
            this.password = response.data.password
            this.mail = response.data.mail
            this.peso = response.data.peso
            this.altura = response.data.altura
            this.menu = response.data.menu
        })
        .catch((error) => {
            this.$router.push('/dietasapp')
        })
  },
  methods: {
    update: function () {
      const formData = new FormData()
      formData.set('nombre', this.nombre)
      formData.set('apellido', this.apellido)
      formData.set('usuario', this.usuario)
      formData.set('password', this.password)
      formData.set('mail', this.mail)
      formData.set('peso', this.peso)
      formData.set('altura', this.altura)
      formData.set('menu', this.menu)

      this.$axios.post('http://127.0.0.1:9001/update', formData)
        .then((response) => {
          this.$router.push('/dietasapp')
        })
        .catch((error) => {
          this.$q.dialog({
            title: 'Oopss...',
            message: 'Experimentamos un error al actualizar tus datos. Intenta nuevamente más tarde',
            cancel: true,
            persistent: true,
          })
        })
    },
    volver: function () {
      this.$router.push('/dietasapp')
    }
  }
}
</script>