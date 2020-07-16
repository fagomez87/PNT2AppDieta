<template> <!-- TO DO ORDENAR LA IDENTACIÓN -->
  <q-page class="flex flex-center">
    <div color="primary">
        <h3>Bienvenido</h3>
    </div>
    <div>
      <q-form v-on:submit="register" >
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
        v-model="menu"
        label="menu"
        :options="options"
        :rules="['Seleccione una por favor']" 
      />
      <br/>
      <div>
          <q-btn label="Registrar" type="submit" color="secondary" />
          <q-btn label="Cancelar" @click="reset" color="secondary" flat class="q-ml-sm" />
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
      password: '',
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
      
      const formData = new FormData()
      formData.set('nombre', this.nombre)
      formData.set('apellido', this.apellido)
      formData.set('usuario', this.usuario)
      formData.set('password', this.password)
      formData.set('mail', this.mail)
      formData.set('peso', this.peso)
      formData.set('altura', this.altura)
      formData.set('menu', this.menu)

      this.$axios.post('http://127.0.0.1:9001/register', formData)
        .then((response) => {
          this.$router.push('/')
        })
        .catch((error) => {
          this.$q.dialog({
            title: 'Error al crear el usuario',
            message: 'Ya tenemos registrado un usuario con ese alias',
            cancel: true,
            persistent: true,
          })
        })

      // Esta OK
    },
    reset: function () {
      this.$router.push('/')
    }
  }
}
</script>