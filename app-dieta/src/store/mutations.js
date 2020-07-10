export default {
    login: function (state, data) {
      state.id = data.id
      state.username = data.username
      state.token = data.token
    },
    logout: function (state) {
      state.username = null
      state.token = null
    },
    opciones: function (state, data) {
      console.log("En la mutation " + data)
     
    }
  }
  