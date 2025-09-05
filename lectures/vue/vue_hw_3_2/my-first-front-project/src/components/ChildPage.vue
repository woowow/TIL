<template>
  <div class="box">
    <h3>자식 페이지입니다.</h3>
    <p>이름: {{ child.name }}</p>
    <p>나이: {{ child.age }}</p>
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
.box{
  border: 1px solid;
  padding: 10px;
  margin: 10px;
}
</style>