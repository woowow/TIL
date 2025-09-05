<template>
  <div class>
    <h1>부모 페이지입니다.</h1>
    <ChildPage
      v-for="(child, index) in children"
      :key="index"
      :child="child"
      @giveMeAllowance="updateBalance(children[index])"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
  { name: '김하나', age: 30, balance: 100000 },
  { name: '김두리', age: 20, balance: 10000 },
  { name: '김서이', age: 10, balance: 1000 }
])

function updateBalance(child) {
  child.balance += 1000
}

</script>