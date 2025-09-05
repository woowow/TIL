<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <div v-if="person">
      <p>이름: {{ person.name }}</p>
      <p>잔고: {{ person.balance }}</p>
      <button @click="increase">+ 1000원</button>
    </div>
    <div v-else>
      <p>데이터를 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '../stores/balance'
import { computed } from 'vue'

const route = useRoute()
const store = useBalanceStore()

const person = computed(() => store.getByName(route.params.name))

function increase() {
  store.increaseBalance(route.params.name, 1000)
}
</script>
