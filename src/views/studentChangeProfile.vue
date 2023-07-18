<template>
  <div class="studentChangeProfile">
    <v-header/>
    <v-main-wrapper class="v-main-cont">
      <v-sidebar>
        <v-sidebar-link
            v-for="link in sidebar"
            :key="link.id"
            :link_data="link"
        />
      </v-sidebar>
      <div class="layout-main">
        <div class="layout-main__head">
          <h1>{{ article }}</h1>
        </div>
        <div class="layout-main__body">
          <v-cont>
            <v-block>
              <form @submit.prevent>
                <div class="v-block__body">
                  <v-list-input>
                    <v-input
                        v-for="input in inputList"
                        :key="input.name"
                        :input_data="input"
                    />
                    <v-textarea
                        v-for="textarea in textareaList"
                        :key="textarea.name"
                        :textarea_data="textarea"
                    />
                  </v-list-input>
                </div>
                <div class="v-block__bottom flex-between">
                  <v-buttton
                      class="red"
                      @click="$router.go(-1)"
                  >
                    Отменить
                  </v-buttton>
                  <v-buttton class="blue">
                    Сохранить
                  </v-buttton>
                </div>
              </form>
            </v-block>
          </v-cont>
        </div>
      </div>
    </v-main-wrapper>
  </div>
</template>
<script>
import vHeader from '../components/v-header'
import VMainWrapper from "@/components/v-main-wrapper";
import vSidebar from "../components/v-sidebar";
import vSidebarLink from "../components/v-sidebar-link";
import vCont from "../components/v-cont";
import vBlock from "../components/v-block";
import vButtton from '../components/v-button'
import vListInput from '../components/v-list-input'
import vInput from '../components/v-input'
import vTextarea from "@/components/v-textarea";
export default {
  name: "studentChangeProfile",
  components: {
    VMainWrapper,
    vHeader,
    vSidebar,
    vSidebarLink,
    vCont,
    vBlock,
    vButtton,
    vListInput,
    vInput,
    vTextarea
  },
  data() {
    return {
      article: 'Профиль',

      user: {
        role: 'Студент',
        name: 'Иван',
        lastname: 'Иванов',
      },
      sidebar: [
        {
          id: 1,
          path: '/student/profile',
          text: 'Профиль',
          active: true,
        },
        {
          id: 2,
          path: '/student/inters',
          text: 'Стажировки',
          active: false,
        },
        {
          id: 3,
          path: '/student/chat',
          text: 'Чаты',
          active: false,
        },
        {
          id: 4,
          path: '/student/tests',
          text: 'Тесты',
          active: false,
        },
      ],

      inputList: [
        {
          name: 'input6',
          title: 'Почта',
          value: 'example@gmail.com',
          placeholder: 'example@gmail.com',
          inputType: 'email',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'input7',
          title: 'Телефон',
          value: '8-999-999-99-99',
          placeholder: '8-999-999-99-99',
          inputType: 'tel',
          required: true,
          disabled: false,
          error: false,
        },
      ],
      textareaList: [
        {
          name: 'textarea1',
          title: 'Софт скиллы',
          value: 'ksjdnf ksjdnf kjsdnfkj sndjkfn sdkjfn ',
          placeholder: 'Введите ваши софт скиллы',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'textarea2',
          title: 'Хард скиллы',
          value: 'lorem sodkfo sdkfo sdofk osdkfo sdofkos k',
          placeholder: 'Введите ваши хард скиллы',
          required: true,
          disabled: false,
          error: false,
        },
      ],
    }
  }
}
</script>

<style lang="scss">

</style>