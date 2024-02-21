import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  app: {
    head: {
      link: [
        {
          rel: 'stylesheet',
          href: '/css/kosk.css',
        },
      ],
    },
  },
  build: {
    transpile: ['vuetify'],
  },
  css: [
    'vuetify/lib/styles/main.sass',
    '@mdi/font/css/materialdesignicons.min.css',
  ],
  experimental: {
    payloadExtraction: false,
  },
  modules: ['@pinia/nuxt'],
  nitro: {
    prerender: {
      crawlLinks: false,
      failOnError: false,
    },
  },
  runtimeConfig: {
    public: {
      apiUrl: process.env.API_URL || 'http://localhost:8000/',
      statamicurl: process.env.STATAMIC_URL || 'http://localhost:8000/',
      repo_branch: 'master',
    },
  },
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
})
