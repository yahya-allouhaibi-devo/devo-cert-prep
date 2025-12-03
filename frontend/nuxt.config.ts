// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  // TypeScript configuration
  typescript: {
    strict: true,
    typeCheck: true
  },

  // Modules
  modules: [
    '@pinia/nuxt',
  ],

  // Runtime config for API base URL
  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE_URL || 'http://localhost:8000'
    }
  },

  // CSS configuration
  css: [
    '~/assets/css/main.css',
  ],

  // Auto-import components
  components: {
    dirs: [
      '~/components'
    ]
  },

  // Vite configuration
  vite: {
    css: {
      preprocessorOptions: {}
    }
  }
})
