<script setup>
import { ref } from 'vue'
import YAML from 'yaml'
import { VContainer, VRow, VCol, VCard, VCardTitle, VCardText, VCardActions, VImg, VSpacer, 
  VBtn } from 'vuetify/components';
import TheFooter from '~/components/TheFooter.vue';

const { $backend } = useNuxtApp()
const html = ref("")
const calendaritems = ref([])
const cutoffsec = (new Date()).valueOf() / 1000


async function getCalendar(){
  let reply
  calendaritems.value = []
  try {
    reply = await $backend('filestore', 'anon_get_filelist', {
      group: 'youthcalendar',
    })
  }
  catch(error) {
    console.log('failed')
  }
  let promises = []
  reply.data.forEach(f => promises.push(getCalendarFile(f)))
  await Promise.all(promises)
  sortCalendar()
}

async function getCalendarFile(f){
  const fname = f.split('/')[1]
  try {
    const reply = await $backend('filestore', 'anon_get_file', {
      group: 'youthcalendar',
      name: fname,
    })
    const calYaml = YAML.parse(reply.data)
    processCalenderYaml(calYaml)
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


function sortCalendar(){
  calendaritems.value = calendaritems.value.sort((a,b) => a.datesec - b.datesec)
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


onMounted(()=>{
  getCalendar()
})



</script>

<template>
<div>
  <VContainer>
    <h1>Jeugdalender</h1>
    <ul>
      <li v-for="c, ix in calendaritems" :key="ix" class="mt-2">
        {{ renderCalenderItem(c) }}
        <div v-if="!!c.link">
          URL: <a :href="c.link">{{ c.link }}</a>
        </div>
      </li>
    </ul>  
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