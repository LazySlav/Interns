<template>
  <div class="v-sidebar">
    <div class="v-sidebar__list">
        <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-sidebar"
}
</script>

<style lang="scss">
.v-sidebar {
  padding: 25px 0;
  border-radius: 10px;
  background: #F6F6FA;
  width: 250px;
}
.v-sidebar__list {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
@media (max-width: 767px) {
  .v-sidebar {
    width: 100%;
    margin-bottom: 24px;
  }
}
</style>