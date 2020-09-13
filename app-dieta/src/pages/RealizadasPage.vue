<template>
  <div class="q-pa-md">
    <q-table
      grid
      title="Que comiste"
      :data="data"
      :columns="columns"
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
              <strong>{{ props.row.dia }}</strong>
              <br>
              {{ props.row.dieta }}
            </q-card-section>
            <q-separator />
            <q-card-section class="flex flex-center" style="10px">
              <div>{{ props.row.tipo }}</div>
            </q-card-section>
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
  name: 'MainPage',
  beforeCreate: function () {
      if (!this.$store.getters['isLogged']) {
          this.$router.push('/')
      }
  },
  data () {
    return {
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: 3
      },
      columns: [
        { name: 'dieta', label: 'Tipo de dieta', field: 'dieta' },
        { name: 'tipo', label: 'Opcion', field: 'tipo' }
      ],
      data
    }
  },
  methods: {
    volver: function(){
      this.$router.push('/dietasapp')
    }
  }
}

const tipos = [
  'Desayuno: Té + 3 tostadas con mermelada \nAlmuerzo: Pechuga de pollo con ensalada Cena: 2 Milanesas de soja con ensalada',
  'Desayuno: Té + 3 tostadas con mermelada \nAlmuerzo: Lata de atún con ensalada Cena: 1 Milanesa de peceto con ensalada',
  'Desayuno: Cafe + 3 tostadas con mermelada \nAlmuerzo: Bife + 1 pan chico con ensalada Cena: 2 Milanesas de soja con ensalada'
]
const dias = ["Lunes", "Martes", "Miercoles"]
const data = []
let j= 0;
tipos.forEach(name => {
  for (let i = 0; i < 1; i++) {
    data.push({ dieta: 'Mi comida fue', tipo: name, dia:dias[j] })
  }
  j++;
})

</script>
