<template>
  <q-page class="flex flex-center">
    <q-form
      v-on:submit="login"
      v-on:reset="onReset"
    >
    <q-img :src="require('../assets/sombrero1.png')" />
      <q-input
        filled
        v-model="username"
        label="Usuario"
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
      <div>
        <q-btn label="Ingresar" type="submit" color="secondary"/>
        <q-btn label="Cancelar" type="reset" color="secondary" flat class="q-ml-sm" />
        <p><br>¿No estas registrado?</p><q-btn @click="register" flat class="q-ml-sm" color="primary">¡Registrate!</q-btn>
      </div>
    </q-form>
  </q-page>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login: function () {
      const formData = new FormData()
      formData.set('username', this.username)
      formData.set('password', this.password)
      this.$axios.post('http://127.0.0.1:9001/login', formData)
        .then((response) => {
          console.log(response.data)
            this.$store.commit('login', {
            id: this.id,
            username: this.username,
            token: response.data.token
          })
          this.$router.push('/dietasapp')
          this.$q.notify({
            color: 'green-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Bienvenido'
          })
        })
        .catch((error) => {
            this.$q.dialog({
            title: 'Datos erroneos',
            message: 'Usuario o contraseña incorrectos',
            cancel: true,
            persistent: true,
          })
        })
    },
    onReset () {
      this.username = null
      this.password = null
    },
    register: function () {
      this.$router.push('registrar')
    }
  }
}
</script>
