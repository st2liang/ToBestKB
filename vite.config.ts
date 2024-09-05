import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import viteMockServe from 'vite-plugin-mock'
export default defineConfig({
  plugins: [
    // viteMockServe({
    //   mockPath: 'mock',
    //   watch:true,
    // }
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})

