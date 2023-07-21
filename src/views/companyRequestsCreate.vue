<template>
  <div class="companyRequestsCreate">
    <v-headerComp/>
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
          <h1>Создать заявку</h1>
        </div>
        <div class="layout-main__body">
          <v-cont class="big">
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
                  <v-buttton
                      class="blue"
                      @click="$router.go(-1)"
                  >
                    Отправить
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
import vHeaderComp from '../components/v-headerComp'
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
  name: "companyRequestsCreate",
  components: {
    VMainWrapper,
    vHeaderComp,
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
        role: 'Компания',
        name: 'Название компании',
      },
      sidebar: [
        {
          id: 1,
          path: '/company/profile',
          text: 'Профиль',
          active: false,
        },
        {
          id: 2,
          path: '/company/requests',
          text: 'Заявки',
          active: true,
        },
        {
          id: 3,
          path: '/company/chat',
          text: 'Чаты',
          active: false,
        },
      ],

      inputList: [
        {
          name: 'input1',
          title: 'Название',
          value: '',
          placeholder: 'Google стажировка',
          inputType: 'text',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'input2',
          title: 'Место прохождения практики',
          value: '',
          placeholder: 'г. Москва, Гороховский пер., д.4, ст.4',
          inputType: 'text',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'input3',
          title: 'Период работы',
          value: '',
          placeholder: '01.01.2023 - 31.12.2099',
          inputType: 'text',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'input4',
          title: 'Сумма оплаты стажировки',
          value: '',
          placeholder: '0',
          inputType: 'text',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'input5',
          title: 'Необходимое количество стажёров',
          value: '',
          placeholder: '0',
          inputType: 'text',
          required: true,
          disabled: false,
          error: false,
        },
      ],
      textareaList: [
        {
          name: 'textarea1',
          title: 'Описание стажировки',
          value: '',
          placeholder: '',
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