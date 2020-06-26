<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
        <q-toolbar-title style="padding-left: 25px" color="secondary">
          DietasApp
        </q-toolbar-title>

    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'LoginLayout'
}
</script>
