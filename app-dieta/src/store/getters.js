export default {
    isLogged: function (state) {
      return state.username != null && state.username.length > 0 && state.token != null && state.token.length > 0
    }
  }
  