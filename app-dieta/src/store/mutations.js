export default {
    login: function (state, data) {
      state.username = data.username
      state.token = data.token
    },
    logout: function (state) {
      state.username = null
      state.token = null
    }
  }
  