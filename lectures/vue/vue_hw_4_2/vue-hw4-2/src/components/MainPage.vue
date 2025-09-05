<template>
  <div class="main">
    <h1>pinia 연습하기</h1>
    <ParentPage
      v-for="(family, index) in familyInfo" :key="index" :family="family" />
  </div>
</template>

<script setup>
import { useFamilyStore } from '../stores/family'
import ParentPage from './ParentPage.vue'

const familyStore = useFamilyStore()
const familyInfo = familyStore.familyInfo
</script>

<style scoped>
.main {
  margin: 0 auto;
  padding: 20px;
}
</style>
