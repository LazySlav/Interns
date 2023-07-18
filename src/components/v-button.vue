<template>
  <button :class="['v-button', color].join(' ')">
    <span>
      <slot></slot>
    </span>
  </button>
</template>

<script>
export default {
  name: "v-button",
  props: {
    color: {
      validator (value) {
        return ['blue','yellow', 'red'].includes(value)
      },
      default: 'blue',
    }
  }
}
</script>

<style lang="scss">
.v-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 145px;
  height: 40px;
  border-radius: 10px;
  background: #D9D9D9;
  border: 2px solid #D9D9D9;
  color: #FFF;
  font-size: 14px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  transition: .3s;
  cursor: pointer;

  &.blue {
    background: #2f80fd;
    border-color: #2f80fd;
  }
  &.yellow {
    background: #F2E143;
    border-color: #F2E143;
  }
  &.red {
    background: #EB5757;
    border-color: #EB5757;
  }

  span {
    background: transparent;
  }

  @media (min-width: 1400px) {
    &.blue:hover {
      background: transparent;
      color: #2f80fd;
    }
    &.yellow:hover {
      background: transparent;
      color: #F2E143;
    }
    &.red:hover {
      background: transparent;
      color: #EB5757;
    }
  }
}
</style>