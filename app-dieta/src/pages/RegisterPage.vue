<template> <!-- TO DO ORDENAR LA IDENTACIÓN -->
  <q-page class="flex flex-center">
    <div color="primary">
        <h3>Bienvenido</h3>
    </div>
    <div>
      <q-form
        v-on:submit="register"
        v-on:reset="reset"
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
        v-model="contrasena"
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
        v-model="menu"
        label="menu"
        :options="options"
        :rules="['Seleccione una por favor']" 
      />
      <br/>
      <div>
          <q-btn label="Registrar" type="submit" color="secondary" />
          <q-btn label="Cancelar" type="reset" color="secondary" flat class="q-ml-sm" />
      </div>
    </q-form>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'RegisterPage',
  data () {
    return {
      nombre: '',
      apellido: '',
      usuario: '',
      contrasena: '',
      mail: '',
      peso: '',
      altura: '',
      menu: '',
      model: null,
      options: ["Carnes y vegetales", "Vegetariano", "Vegano"]
    }
  },
  methods: {
    register: function () {
      // Voy al servidor, consulto, y si no existe lo crea y vuelve al login. 
          //si existe no lo crea y da aviso de que el usuario ya existe
    //   this.$store.commit('dietasapp/login', {
    //     username: this.username,
    //     token: 'abcdefghijk'
    //   })

      const formData = new FormData()
      formData.set('nombre', this.nombre)
      formData.set('apellido', this.apellido)
      formData.set('usuario', this.usuario)
      formData.set('contrasena', this.contrasena)
      formData.set('mail', this.mail)
      formData.set('peso', this.peso)
      formData.set('altura', this.altura)
      formData.set('menu', this.menu)

      this.$axios.post('http://127.0.0.1:9001/register', formData)
        .then((response) => {
            this.$store.commit('register', {
            username: this.username,
            token: response.data.token
          })
          this.$router.push('/')
        })
        .catch((error) => {
          console.log(error)
        })
      this.$router.push('/')
      // Esta OK
    },
    reset: function () {
      this.$router.push('/')
    }
  }
}
</script>