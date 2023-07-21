<template>
  <div class="companyProfile">
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
                <div class="v-block__bottom flex-center">
                  <v-link
                      class="yellow"
                      href="/company/profile/edit"
                  >
                    Изменить
                  </v-link>
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
import vLink from '../components/v-link'
import vListInput from '../components/v-list-input'
import vInput from '../components/v-input'
import vTextarea from "@/components/v-textarea";
export default {
  name: "studentProfile",
  components: {
    VMainWrapper,
    vHeaderComp,
    vSidebar,
    vSidebarLink,
    vCont,
    vBlock,
    vLink,
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
          active: true,
        },
        {
          id: 2,
          path: '/company/requests',
          text: 'Заявки',
          active: false,
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
          title: 'Название компании',
          value: 'Название компании',
          placeholder: 'Название компании',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input2',
          title: 'Номер телефона',
          value: '8-999-999-99-99',
          placeholder: '8-999-999-99-99',
          inputType: 'tel',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input3',
          title: 'Почта',
          value: 'example@gmail.com',
          placeholder: 'example@gmail.com',
          inputType: 'email',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input4',
          title: 'Физический адрес',
          value: '...',
          placeholder: '...',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input5',
          title: 'Юридический адрес',
          value: '...',
          placeholder: '...',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
      ],
      textareaList: [
        {
          name: 'textarea1',
          title: 'Описание компании',
          value: '...',
          placeholder: '...',
          required: true,
          disabled: true,
          error: false,
        },
      ]
    }
  }
}
</script>

<style lang="scss">
.v-main-cont {
  padding-top: 78px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}
.layout-main {
  width: calc(100% - 250px - 24px);
}
.layout-main__head {
  margin-bottom: 24px;
}
</style>