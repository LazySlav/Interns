<template>
  <div class="v-tests-list-item">
    <div class="v-tests-list-item__helper">
      <div class="v-tests-list-item__row">
        <div class="v-tests-list-item__title">
          {{ inter_data.title }}
        </div>
        <div class="v-tests-list-item__description">
          {{ inter_data.description }}
        </div>
        <div class="v-tests-list-item__status">
          Статус -
          <span
              v-if="inter_data.status === 1"
              class="blue"
          >
          В работе
        </span>
          <span
              v-if="inter_data.status === 2"
              class="yellow"
          >
          На проверке
        </span>
          <span
              v-if="inter_data.status === 3"
              class="black"
          >
          Завершен
        </span>
        </div>
      </div>
      <div class="v-tests-list-item__bottom">
        <v-link
            class="blue"
            :href="'/student/inters/' + inter_data.id"
        >
          Подробнее
        </v-link>
      </div>
    </div>
  </div>
</template>

<script>
import vLink from './v-link'
export default {
  name: "v-tests-list-item",
  components: {
    vLink
  },
  props: {
    inter_data: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style lang="scss">
.v-tests-list-item {
  width: calc(100% / 3);
  padding: 8px;

  &__helper {
    width: 100%;
    height: 100%;
    background: #fff;
    border-radius: 10px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
  }
  &__title {
    margin-bottom: 16px;
    color: #393F49;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
  }
  &__description {
    margin-bottom: 8px;
    color: #393F49;
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }
  &__status {

    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;

    span.blue {
      color: #2f80fd;
    }
    span.yellow {
      color: #F2E143;
    }
  }
  &__bottom {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    margin-top: 24px;
  }
}
@media (max-width: 1399px) {
  .v-inters-list-item {
    width: 50%;
  }
}
@media (max-width: 767px) {
  .v-inters-list-item {
    width: 100%;
  }
}
</style>