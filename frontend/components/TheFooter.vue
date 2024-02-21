<script setup>
import { VContainer, VCard, VCardText, VRow, VCol } from 'vuetify/components';
</script>
<template>
  <v-container fluid>
    <v-card class="bg-lime-lighten-1">
      <v-card-text>
        <v-row>
          <v-col>
            <h4 class="mb-2">Lokaal + Adres</h4>
            <div>Koninklijke Oostendse Schaakkring vzw.</div>
            <div>
              Koninginnelaan 76<br />
              8400 Oostende.<br />
            </div>
          </v-col>
          <v-col>
            <h4 class="mb-2">Contactgegevens</h4>
            <div>
              e-mail: <a href="mailto:bestuur@kosk.be">bestuur@kosk.be</a>
            </div>
            <div>IBAN : BE51 3800 0795 3162</div>
            <div>KBO: BE 0410.432.437</div>
          </v-col>
          <v-col>
            <h4 class="mb-2">Sociale media</h4>
            <div>
              Facebook:
              <a href="https://www.facebook.com/groups/210569320243">
                <img
                  style="vertical-align: middle"
                  src="~/assets/facebook.png"
                />
              </a>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>