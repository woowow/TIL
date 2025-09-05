<template>
  <div class="child">
    <p class="subtitle">자식 페이지</p>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.child {
  background-color: #fff;
  padding: 12px;
  margin: 10px auto;
  text-align: center;
  width: 90%;
  border: 1px solid #dde;
}

.subtitle {
  font-weight: bold;
  margin-bottom: 6px;
}
</style>
