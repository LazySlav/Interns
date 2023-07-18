<template>
<div class="v-inters-list">
  <slot></slot>
</div>
</template>

<script>
export default {
  name: "v-inters-list"
}
</script>

<style lang="scss">
.v-inters-list {
  width: calc(100% + 16px);
  margin: -8px;
  display: flex;
  align-items: initial;
  justify-content: flex-start;
  flex-wrap: wrap;
}
</style>