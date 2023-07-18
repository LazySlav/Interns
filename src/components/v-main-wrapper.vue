<template>
  <div class="v-main-wrapper">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "v-main-wrapper"
}
</script>

<style lang="scss">
  .v-main-wrapper {
    width: 1200px;
    margin: 0 auto;
  }
  @media (max-width: 1399px) {
    .v-main-wrapper {
      width: 750px;
    }
  }
  @media (max-width: 768px) {
    .v-main-wrapper {
      width: 100%;
      padding: 0 15px;
    }
  }
</style>