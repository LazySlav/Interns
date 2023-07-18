<template>
  <div :class="['v-cont', size].join(' ')">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "v-cont",
  props: {
    size: {
      validator (value) {
        return ['small', 'big'].includes(value)
      },
      default: 'small',
    }
  }
}
</script>

<style lang="scss">
  .v-cont {
    width: 350px;

    &.big {
      width: 100%;
    }
  }
  @media (max-width: 767px) {
    .v-cont {
      width: 100%;
    }
  }
</style>