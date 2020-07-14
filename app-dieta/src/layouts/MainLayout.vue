<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          DietasApp
        </q-toolbar-title>
        <div>Hola {{username}} </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Essential Links
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

export default {
  name: 'MainLayout',

  components: {
    EssentialLink
  },
  computed: {
    username: function () {
      return this.$store.state.username
    }
  },

  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: [
        {
          title: 'Mis Datos',
          icon: 'account_circle',
          link: '/#/datos'
        },
        {
          title: 'Menu',
          caption: '',
          icon: 'restaurant',
          link: '/#/menu'
        },
        {
          title: 'Reportes',
          caption: '',
          icon: 'bar_chart',
          link: '/#/reportes'
        },
        {
          title: 'Quienes somos',
          caption: 'Nuestras redes sociales',
          icon: 'public',
          link: 'https://facebook.DietasApp.com'
        },
        {
          title: 'Contacto',
          caption: 'Soporte tecnico',
          icon: 'chat',
          link: '/#/chat'
        },
        {
          title: 'Logout',
          caption: 'Salir',
          icon: 'cancel',
          link: '/'
        }
      ]
    }
  }
}
</script>
