<template>
  <div class="v-list-input">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "v-list-input"
}
</script>

<style lang="scss">
.v-list-input {
  margin: -8px 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
</style>