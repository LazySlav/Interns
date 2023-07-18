<template>
  <div class="error center">
    <v-main-wrapper>
      <v-error-block />
    </v-main-wrapper>
  </div>
</template>

<script>
import vMainWrapper from '../components/v-main-wrapper'
import vErrorBlock from '../components/v-error-block'
export default {
  name: "errorPage",
  components: {
    vMainWrapper, vErrorBlock
  }
}
</script>

<style lang="scss">

</style>