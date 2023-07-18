<template>
  <div class="v-block">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "v-block"
}
</script>

<style lang="scss">
  .v-block {
    width: 100%;
    padding: 24px;
    border-radius: 10px;
    background: #F6F6FA;
    &__head {
      margin-bottom: 24px;
      &:only-child {
        margin-bottom: 0;
      }
    }
    &__body {
      width: 100%;
    }
    &__bottom {
      width: 100%;
      display: flex;
      align-items: flex-start;
      justify-content: flex-start;
      flex-wrap: wrap;
      margin-top: 24px;

      &:only-child {
        margin-top: 0;
      }
      &.flex-center {
        justify-content: center;
      }
      &.flex-between {
        justify-content: space-between;
      }
    }
  }
</style>