<template>
  <div :class="['v-input', input_data.error ? 'error' : ''].join(' ')">
    <div class="v-input__head">
      {{ input_data.title }}
    </div>
    <div class="v-input__body">
      <div class="v-input__block">
        <input
            :disabled="input_data.disabled"
            :type="input_data.inputType"
            :value="input_data.value"
            :class="['v-input__input', input_data.required ? 'required' : ''].join(' ')"
            :placeholder=" input_data.placeholder "
        >
        <div class="v-input__error-text">
          Некорректный ввод
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-input",
  props: {
    input_data: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style lang="scss">
.v-input {
  width: 100%;
  padding: 8px 0;
  &__head {
    padding-left: 16px;
    width: 100%;
    margin-bottom: 4px;
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 17px;
    color: #BEC5D7;
    display: flex;
    align-items: center;
    user-select: none;
    justify-content: space-between;
  }
  &__body {
    width: 100%;
  }
  &__block {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    transition: .3s;
  }
  &__error-text {
    position: absolute;
    bottom: calc(100% + 2px);
    right: 16px;
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 14px;
    color: #EB5757;
    display: none;
  }
  &__input {
    padding: 10px calc(24px + 8px + 15px) 10px 16px;
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 14px;
    color: #393F49;
    width: 100%;
    border: 1px solid #BEC5D7;
    background: #FFFFFF;
    border-radius: 20px;
    position: relative;
    transition: .3s;

    &[disabled] {
      border-color: #fff;
    }
    &:not(:placeholder-shown):not([disabled]),
    &:active:not([disabled]),
    &:focus:not([disabled]),
    &:focus-visible:not([disabled]) {
      border-color: #393F49;
    }
    &::placeholder {
      color: #BEC5D7;
    }
  }
  &.error &__input {
    border-color: #EB5757;
  }
  &.error &__error-text {
    display: block;
  }
}
</style>