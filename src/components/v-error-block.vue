<template>
  <div class="v-error-block">
    <div class="v-error-block__head">
      <div class="v-error-block__title">
        {{ pageTitle }}
      </div>
    </div>
    <div class="v-error-block__body">
      <v-link @click="$router.go(-1)">Назад</v-link>
    </div>
  </div>
</template>

<script>
import vLink from './v-link'
export default {
  name: "v-error-block",
  components: {
    vLink
  },
  data() {
    return {
      pageTitle: 'Ошибка...',
    }
  }
}
</script>

<style lang="scss">
.v-error-block {
  width: 300px;
  margin: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  &__head {
    margin-bottom: 24px;
  }
  &__title {
    font-size: 64px;
    font-weight: 700;
  }
}
</style>