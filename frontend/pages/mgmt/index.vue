<script setup>
import { ref, onMounted } from 'vue'
import * as jose from 'jose'
import { usePersonStore } from "@/store/person"
import { storeToRefs } from 'pinia'


// stores
const personstore = usePersonStore();
const { person } = storeToRefs(personstore)

// datamodel
const wrong_domain = ref(false)

async function checkPerson() {
  console.log('checking if person is present so we can go to overview')
  if (person.value.credentials.length > 0) {
    if (person.value.email.endsWith('@ksok.be')) {
      navigateTo('/mgmt/overview')
    }
    else {
      wrong_domain.value = true
    }
  }
}


function handleGoogle(resp) {
  console.log('handling google')
  wrong_domain.value = false
  const payload = jose.decodeJwt(resp.credential)
  console.log('decoded', payload)
  personstore.updatePerson({
    credentials: resp.credential,
    user: payload.given_name,
    email: payload.email
  })
  checkPerson()
}

function setupGoogle() {
  console.log('Setup google sign in')
  const reply = google.accounts.id.initialize({
    client_id: '154971061769-faafor0rppa5kko69sk9ls0jifomu8up.apps.googleusercontent.com',
    callback: handleGoogle,
    prompt_parent_id: 'parent_id'
  })
  console.log("initialize:", reply)
  const prompt = google.accounts.id.prompt((notif) => {
    console.log('notif', notif)
    if (notif.isNotDisplayed() || notif.isSkippedMoment()) {
      document.cookie = `g_state=;path=/;expires=Thu, 01 Jan 1970 00:00:01 GMT`;
      google.accounts.id.prompt()
    }
  })
  console.log("prompt", prompt)
  console.log('Setup google sign in completed')
}

useHead({
  script: [
    { src: 'https://accounts.google.com/gsi/client', defer: true }
  ],
  title: 'Management Login',
})

definePageMeta({
  layout: 'mgmt',
})

onMounted(() => {
  checkPerson()
  setupGoogle()
})

</script>

<template>
  <VContainer>
    <p>Beheer KOSK</p>
    <p>
      Dit gedeelte is enkel toegankelijk voor mensen met een geldig @kosk.be
      account
    </p>
    <div id="parent_id" />
    <v-alert error v-show="wrong_domain">Ongeldig domein</v-alert>
  </VContainer>
</template>


