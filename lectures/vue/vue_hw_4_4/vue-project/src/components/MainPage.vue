<template>
  <div>
    <p>이름: {{ info.name }}</p>
    <p>잔고: {{ info.balance }}</p>
    <button @click="goUpdate">updateBalance</button>
  </div>
  <hr>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  info: {
    type: Object,
    required: true
  }
})

const router = useRouter()

function goUpdate() {
  router.push({ name: 'update', params: { name: props.info.name } })
}
</script>

<style scoped>
.card {
  border: 1px solid #aaa;
  margin: 10px;
  padding: 10px;
}
</style>
