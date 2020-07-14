<template>
  <div class="q-pa-md">
    <q-table
      grid
      title="Opciones disponibles"
      :data="data"
      row-key="name"
      :filter="filter"
      hide-header
    >
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

      <template v-slot:item="props">
        <div class="q-pa-xs col-xs-12 col-sm-6 col-md-4">
          <q-card>

            <q-card-section class="text-center">
              <strong>{{ props.row.titulo }}</strong>
            </q-card-section>
            <q-separator />
            <q-card-section class="flex flex-center" style="10px">
              <div>{{ props.row.menu }}</div>
            </q-card-section>
            <q-card-actions>
              <q-btn >Seleccionar</q-btn>
          </q-card-actions>
          </q-card>
        </div>
      </template>
    </q-table>
    <div>
      <q-btn label="Volver" @click="volver" color="secondary"/>
    </div>
  </div>
</template>
<script>
export default {
  name: 'OpcionesPage',
    data () {
      return {
        filter: '',
        pagination: {
        page: 1,
        rowsPerPage: 3
      },
      options: '',
      data,
    }
  },
  methods: {
    volver: function (){
      this.$router.push('/dietasapp')
    },
  }
}

const opciones = [
  "Desayuno: Té + 3 tostadas con mermelada \nAlmuerzo: Pechuga de pollo con ensalada \nCena: 2 Milanesas de soja con ensalada",
  "Desayuno: Té + 3 tostadas con mermelada \nAlmuerzo: Lata de atún con ensalada mixta \nCena: 1 Milanesa de peceto con ensalada",
  "Desayuno: Cafe + 3 tostadas con mermelada \nAlmuerzo: Bife + 1 pan chico con ensalada \nCena: 2 Milanesas de soja con ensalada"
]
const titulo = "Menu "
const data = []

let j= 0;
opciones.forEach(opcion => {
    data.push({ menu: opcion, titulo:titulo + (j+1)})
  j++;
})

</script>
