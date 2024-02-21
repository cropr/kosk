<script setup>
import { ref } from 'vue'
import { VApp, VAppBar, VAppBarTitle, VNavigationDrawer, VSpacer, VFooter, VContainer,
  VAppBarNavIcon, VMain, VList, VListItem, VListGroup, VCol, VRow, VCard, VCardText
 } from 'vuetify/components'

const drawer = ref(false)
</script>


<template>
  <v-app> 
    <v-navigation-drawer v-model="drawer" 
        class="bg-lime-darken-1">
      <v-list nav dense >
        <v-list-group>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props">KOSK</v-list-item>
          </template>
          <v-list-item to="/"> Home </v-list-item>
          <v-list-item to="/bestuur"> Bestuur </v-list-item>
          <v-list-item to="/kalender"> Kalender </v-list-item>
          <v-list-item to="/page/historiek">Historiek</v-list-item>
          <v-list-item to="/page/archief">Archief</v-list-item>
        </v-list-group>
        <v-list-group no-action>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props">Interne competities</v-list-item>
          </template>          
          <v-list-item to="/clubkampioenschap"> Clubkampioenschap </v-list-item>
          <v-list-item to="/page/blitz"> Blitz </v-list-item>
          <v-list-item to="/page/rapid"> Rapid </v-list-item>
        </v-list-group>
        <v-list-group no-action>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" >Externe competities</v-list-item>
          </template> 
          <v-list-item to="/page/interclub"> Nationale Interclubs </v-list-item>
          <v-list-item to="/page/vsf"> VSF </v-list-item>
          <v-list-item to="/page/liga"> Liga </v-list-item>
        </v-list-group>
        <v-list-group no-action>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props">Jeugd</v-list-item>
          </template> 
          <v-list-item to="/page/jeugd"> Captain Evans </v-list-item>
          <v-list-item to="/jeugdkalender"> Jeugdalender </v-list-item>
          <v-list-item to="/page/wvjk"> W-Vl kampioenschap </v-list-item>
          <v-list-item to="/page/vjk"> Vl. kampioenschap </v-list-item>
          <v-list-item to="/page/bjk"> B. kampioenschap </v-list-item>
        </v-list-group>                    
      </v-list>
    </v-navigation-drawer> 
    <v-app-bar color="lime-darken-1">
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-app-bar-title class="hidden-sm-and-down">
        <NuxtLink to="/">KOSK</NuxtLink>
      </v-app-bar-title>
      <v-spacer />
      <v-app-bar-title class="hidden-sm-and-down">
        Koninklijke Oostendse Schaakkring
      </v-app-bar-title>   
    </v-app-bar>    

    <v-main>
      <slot />    
    </v-main> 
    <v-footer class="bg-lime-darken-3" app>
      <div class="text-center text-white px-1 py-1">
        Website by
        <a target="_blank" href="https://www.chessdevil.net" class="copyright">
        Chessdevil Consulting</a
        >. &copy; 2021 - 2023. All rights reserved
      </div>
    </v-footer>    
  </v-app>
</template>
  
<style scoped>
a {
  text-decoration: none;
  color: black;
}
a.copyright { 
  color: white;
}
a:link,
a:hover {
  text-decoration: none;
}
a:hover {
  font-weight: 700;
}
footer div {
  margin: auto;
}
.footer2 {
  margin-bottom: 50px;
}
</style>