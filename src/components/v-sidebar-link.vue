<template>
  <a
      :href="link_data.path"
      :class="['v-sidebar-link', link_data.active ? 'active' : ''].join(' ')"
  >
    {{ link_data.text }}
  </a>
</template>

<script>
export default {
  name: "v-sidebar-link",
  props: {
    link_data: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style lang="scss">
.v-sidebar-link {
  display: block;
  width: 100%;
  padding: 10px 24px;
  color: #393F49;
  font-size: 14px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  transition: .3s;

  &:hover {
    background: #97C3FF;
    color: #fff;
  }

  &.active {
    background: #97C3FF;
    color: #fff;
    pointer-events: none;
    cursor: default;
  }
}
</style>