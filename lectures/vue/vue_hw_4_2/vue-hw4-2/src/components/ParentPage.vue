<template>
  <div class="parent">
    <p class="title">부모 컴포넌트</p>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>

    <ChildPage
      v-for="(child, idx) in family.children" :key="idx" :child="child" />
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue'

defineProps({
  family: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.parent {
  background-color: #f9f9f9ec;
  padding: 16px;
  margin-bottom: 20px;
  text-align: center;
  border: 1px solid #ddd;
}

.title {
  font-weight: bold;
  font-size: 1.5rem;
  margin-bottom: 8px;
}
</style>
