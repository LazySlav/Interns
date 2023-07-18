<template>
  <div class="studentProfile">
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
                <div class="v-block__bottom flex-center">
                  <v-link
                      class="yellow"
                      href="/student/profile/edit"
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
import vHeader from '../components/v-header'
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
    vHeader,
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
          name: 'input1',
          title: 'Фамилия',
          value: 'Иванов',
          placeholder: 'Иванов',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input2',
          title: 'Имя',
          value: 'Иван',
          placeholder: 'Иван',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input3',
          title: 'Отчество',
          value: 'Иванович',
          placeholder: 'Иванович',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input4',
          title: 'Наставник',
          value: 'Иванов Иван Иванович',
          placeholder: 'Иванов Иван Иванович',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input5',
          title: 'Специализация',
          value: 'Разработка',
          placeholder: 'Разработка',
          inputType: 'text',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input6',
          title: 'Почта',
          value: 'example@gmail.com',
          placeholder: 'example@gmail.com',
          inputType: 'email',
          required: true,
          disabled: true,
          error: false,
        },
        {
          name: 'input7',
          title: 'Телефон',
          value: '8-999-999-99-99',
          placeholder: '8-999-999-99-99',
          inputType: 'tel',
          required: true,
          disabled: true,
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
          disabled: true,
          error: false,
        },
        {
          name: 'textarea2',
          title: 'Хард скиллы',
          value: 'lorem sodkfo sdkfo sdofk osdkfo sdofkos k',
          placeholder: 'Введите ваши хард скиллы',
          required: true,
          disabled: true,
          error: false,
        },
      ],
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