<script setup>
import { ref } from 'vue'
import { VContainer } from 'vuetify/components';
const route = useRoute()
const { $backend } = useNuxtApp()
const html = ref("")
const metadata = ref({})

async function getContent(){
  try {
    const reply = await $backend('filestore', 'anon_get_file', {
      group: 'articles',
      name: `${route.params.slug}.md`
    })
    let content = useMarkdown(reply.data)
    html.value = content.html
    metadata.value = content.metadata
  }
  catch(error) {
    console.log('failed')
  }
}

onMounted(()=>{
  getContent()
})

</script>

<template>
  <VContainer>
      <h1>{{ metadata.title }}</h1>
      <div v-html="html" class="markdowncontent"></div>
    </VContainer>
</template>

<style>
h1:after
{
    content:' ';
    display: block;
    border:1px solid #aaa;
    margin-bottom: 1em;
}
ul { padding-left: 1rem; }
</style>