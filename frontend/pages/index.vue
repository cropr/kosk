<script setup>
import { ref } from 'vue'
import YAML from 'yaml'
import { VContainer, VRow, VCol, VCard, VCardTitle, VCardText, VCardActions, VImg, VSpacer, 
  VBtn } from 'vuetify/components';
import TheFooter from '~/components/TheFooter.vue';

const { $backend } = useNuxtApp()
const html = ref("")
const metadata = ref({})
const articles = ref([])
const articles3 = ref([])
const articlesrest = ref([])
const calendaritems = ref([])
const cutoffsec = (new Date()).valueOf() / 1000

async function getArticleFile(f){
  const fname = f.split('/')[1]
  try {
    const reply = await $backend('filestore', 'anon_get_file', {
      group: 'articles',
      name: fname,
    })
    const artMarkdown = useMarkdown(reply.data)
    processArticleMarkdown(artMarkdown, fname)
  }
  catch(error) {
    console.log('failed')
  }
}

async function getCalendar(){
  let reply
  calendaritems.value = []
  try {
    reply = await $backend('filestore', 'anon_get_filelist', {
      group: 'calendar',
    })
  }
  catch(error) {
    console.log('failed')
  }
  let promises = []
  reply.data.forEach(f => promises.push(getCalendarFile(f)))
  await Promise.all(promises)
  sortCalendar5()
}

async function getCalendarFile(f){
  const fname = f.split('/')[1]
  try {
    const reply = await $backend('filestore', 'anon_get_file', {
      group: 'calendar',
      name: fname,
    })
    const calYaml = YAML.parse(reply.data)
    processCalenderYaml(calYaml)
  }
  catch(error) {
    console.log('failed')
  }
}

async function getContent(){
  try {
    const reply = await $backend('filestore', 'anon_get_file', {
      group: 'pages',
      name: 'index.md'
    })
    let content = useMarkdown(reply.data)
    html.value = content.html
    metadata.value = content.metadata

  }
  catch(error) {
    console.log('failed')
  }
}

async function getNews(){
  let reply
  try {
    reply = await $backend('filestore', 'anon_get_filelist', {
      group: 'articles',
    })
  }
  catch(error) {
    console.log('failed')
  }
  let promises = []
  reply.data.forEach(f => promises.push(getArticleFile(f)))
  await Promise.all(promises)
  console.log('article count', articles.value.length)
  sortNews()
}

function processArticleMarkdown(artMarkdown, fname){
  const date = new Date(artMarkdown.metadata.publication_date)
  const pubdatesec = date.valueOf() / 1000
  const expdatesec = pubdatesec + parseInt(artMarkdown.metadata.active_days) * 86400
  const todaysec = (new Date()).valueOf() / 1000
  if (expdatesec + 86400 >= todaysec) {
    articles.value.push({
      html: artMarkdown.html,
      metadata: artMarkdown.metadata,
      slug: fname.split('.').slice(0,-1).join('.'),
      date,
      pubdatesec,
      expdatesec,
    })
  }
  else {
    console.log(fname, artMarkdown.metadata.publication_date)
  }
}

function processCalenderYaml(calYaml){
  if (calYaml.multiple) {
    calYaml.multiple.forEach((s) => {processCalenderYaml(s)})
  }
  const datesec = (new Date(calYaml.date)).valueOf() / 1000
  if (datesec + 86400 >= cutoffsec) {
    calendaritems.value.push({
      date: calYaml.date,
      title: calYaml.title,
      datesec: datesec
    })
  }
}

function renderCalenderItem(c) {
  const date = new Date(c.date)
  const output = []
  output.push(date.toLocaleDateString('nl', { dateStyle: 'medium' }) + ':')
  output.push(c.title)
  if (c.round) {
    output.push('Ronde')
    output.push(c.round)
  }
  return output.join(' ')
}


function sortNews(){
  const as = articles.value.sort((a,b) => b.pubdatesec - a.pubdatesec)
  articles3.value = as.slice(0,3)
  articlesrest.value = as.slice(3)
}

function sortCalendar5(){
  calendaritems.value = calendaritems.value.sort((a,b) => a.datesec - b.datesec).slice(0, 5)
}

onMounted(()=>{
  getContent()
  getCalendar()
  getNews()
})



</script>

<template>
  <div>
  <VContainer>
    <VRow>
      <VCol cols="4" md="2">
        <VImg contain src="~/assets/kosk.png" />
      </VCol>
      <VCol cols="8" md="7">
        <h1>{{ metadata.title }}</h1>
        <div v-html="html" class="markdowncontent"></div>
      </VCol>
      <VCol cols="12" md="3">
        <VCard>
          <VCardTitle class="bg-lime-darken-2 text-white">Kalender</VCardTitle>
          <VCardText class="mt-2">
            <ul>
              <li v-for="c, ix in calendaritems" :key="ix" 
                v-html="renderCalenderItem(c)" />
            </ul>            
          </VCardText>
          <VCardActions>
            <VSpacer />
            <VBtn to="/kalender" variant="tonal">
              Meer ...
            </VBtn>
          </VCardActions>
        </VCard>
      </VCol>
    </VRow>
  </VContainer>
  <VContainer fluid>
    <VImg contain src="~/assets/wandkosk.jpeg" />
  </VContainer>
  <VContainer>
      <VRow>
        <VCol v-for="art in articles3" :key="art.slug" cols="12" sm="6" md="4" xl="3">
          <VCard>
            <VCardTitle class="bg-lime-lighten-2 pa-3 hyphen">
              {{ art.metadata.title }}
            </VCardTitle>
            <VCardText class="mt-2">
              <p>
                <em>{{ art.date.toLocaleDateString("nl") }}</em>
              </p>
              <div v-html="art.metadata.intro" />
            </VCardText>
            <VCardActions>
              <VSpacer />
              <VBtn :to="'/article/' + art.slug" variant="tonal">
                Meer ...
              </VBtn>
            </VCardActions>
          </VCard>
        </VCol>
      </VRow>
    </VContainer>
    <VContainer fluid>
      <VImg contain src="~/assets/tombe.jpeg" />
    </VContainer>
    <VContainer>
      <VRow>
        <VCol v-for="art in articlesrest" :key="art.slug" cols="12" sm="6" md="4" xl="3">
          <VCard>
            <VCardTitle class="bg-lime-lighten-2 pa-3 hyphen">
              {{ art.metadata.title }}
            </VCardTitle>
            <VCardText class="mt-2">
              <p>
                <em>{{ art.date.toLocaleDateString("nl") }}</em>
              </p>
              <div v-html="art.metadata.intro" />
            </VCardText>
            <VCardActions>
              <VSpacer />
              <VBtn :to="'/article/' + art.slug" variant="tonal">
                Meer ...
              </VBtn>
            </VCardActions>
          </VCard>
        </VCol>
      </VRow>
    </VContainer>
    <the-footer />
  </div>
  </template>

<style scoped>
h1:after
{
    content:' ';
    display: block;
    border:1px solid #aaa;
    margin-bottom: 1em;
}
ul { padding-left: 1rem; }
.v-card-title { white-space: normal;}

</style>