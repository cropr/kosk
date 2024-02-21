<script setup>
import { ref }  from 'vue'
import YAML from 'yaml'
import { VContainer, VRow, VCol, VBtn, VIcon } from 'vuetify/lib/components/index.mjs';

const { $backend } = useNuxtApp()
const board = ref([])

async function getBoard(){
  console.log('running getBoard')
  let reply
  try {
    reply = await $backend("filestore","anon_get_file", {
      group: "info",
      name: "bestuur.yaml"
    })
  } catch (error) {
    console.log('error', error)
    return
  }
  finally {

  }
  board.value = YAML.parse(reply.data)
  console.log('board', board.value)
}

onMounted(()=>{
  getBoard()
})


</script>


<template>
  <v-container class="mt-1">
    <h1>Dagelijks Bestuur KOSK</h1>
    <v-row>
      <v-col v-for="bm in board" :key="bm.email" cols="12" md="6" xl="4">
        <div class="ma-1 elevation-3 d-flex pa-1">
          <div class="flex-shrink-0 flex-grow-0">
            <img :src="'/img/' + bm.slug + '.jpg'" class="person-photo d-none d-lg-flex">
            <img :src="'/img/' + bm.slug + '.jpg'" class="person-photo-sm d-lg-none ">
          </div>
          <div class="d-flex flex-column flex-grow-1 ml-1">
            <div class="bg-lime-lighten-3 pa-3">
              {{ bm.voornaam }} {{ bm.naam }}
            </div>
            <div class="pa-3">
              <div v-for="r in bm.functies" :key="r">
                {{ r }}
              </div>
              <div v-show="bm.mobile">
                tel: {{ bm.mobile }}
              </div>
              <div>e-mail: {{ bm.slug }}@kosk.be</div>
            </div>
            <div class="pa-3 d-flex">
              <v-btn v-show="bm.mobile" icon color="lime-darken-2" class="mx-2" :href="'tel:' + bm.mobile">
                <v-icon color="white">
                  mdi-phone
                </v-icon>
              </v-btn>
              <v-btn v-show="bm.mobile" icon color="lime-darken-2" class="mx-2" :href="'sms:' + bm.mobile">
                <v-icon color="white">
                  mdi-message-processing
                </v-icon>
              </v-btn>
              <v-btn icon color="lime-darken-2" class="mx-2" :href="'mailto:' + bm.slug + '@kosk.be'">
                <v-icon color="white">
                  mdi-email
                </v-icon>
              </v-btn>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>



<style scoped>

.person-photo {
  width: 160px;
}

.person-photo-sm {
  width: 120px;
}

</style>
