<template>
  <a :href="chat_data.id" class="v-chat-list-item">
    <div class="v-chat-list-item__col">
      <div class="v-chat-list-item__icon">

      </div>
      <div class="v-chat-list-item__info">
        <div class="v-chat-list-item__article">
          {{ chat_data.article }}
        </div>
        <div class="v-chat-list-item__text">
          {{ chat_data.lastMessage }}
        </div>
      </div>
    </div>
    <div class="v-chat-list-item__col">
      <div v-if="chat_data.unreadCounter > 0"
          class="v-chat-list-item__counter">
        {{ chat_data.unreadCounter }}
      </div>
    </div>
  </a>
</template>

<script>
export default {
  name: "v-chat-list-item",
  props: {
    chat_data: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style lang="scss">
.v-chat-list-item {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 24px;
  background: #fff;
  border-radius: 10px;
  &:nth-child(2n + 2) {
    background: transparent;
  }
  &__col {
    display: flex;
    align-items: center;
    justify-content: space-between;

    &:first-child {
      width: calc(100% - 24px - 8px);
    }
    &:last-child {
      width: 24px;
    }
  }
  &__icon {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #2f80fd;
  }
  &__info {
    width: calc(100% - 24px - 8px);
  }
  &__article {
    color: #393F49;
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;

    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }
  &__text {
    color: #BEC5D7;
    font-size: 12px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;

    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }
  &__counter {
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: #97C3FF;
    color: #FFF;
    font-size: 12px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }
}
@media (max-width: 767px) {
  .v-chat-list-item {
    padding: 10px 8px;
  }
}
</style>