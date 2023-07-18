<template>
  <div class="studentSignup center">
      <v-cont :class="small">
        <v-block>
          <div class="v-block__head align-center">
            <h2>{{ article }}</h2>
          </div>
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
              <v-buttton>
                Отправить
              </v-buttton>
            </div>
          </form>
        </v-block>
      </v-cont>
  </div>
</template>

<script>
import vCont from '../components/v-cont'
import vBlock from '../components/v-block'
import vButtton from '../components/v-button'
import vListInput from '../components/v-list-input'
import vInput from '../components/v-input'
import vTextarea from "@/components/v-textarea";
export default {
  name: "studentSingup",
  components: {
    vCont,
    vBlock,
    vButtton,
    vListInput,
    vInput,
    vTextarea
  },
  data() {
    return {
      article: 'Регистрация',

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
          value: '',
          placeholder: 'example@gmail.com',
          inputType: 'email',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'input7',
          title: 'Телефон',
          value: '',
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
          value: '',
          placeholder: 'Введите ваши софт скиллы',
          required: true,
          disabled: false,
          error: false,
        },
        {
          name: 'textarea2',
          title: 'Хард скиллы',
          value: '',
          placeholder: 'Введите ваши хард скиллы',
          required: true,
          disabled: false,
          error: false,
        },
      ]
    }
  }
}
</script>

<style scoped>
.studentSignup {
  padding: 24px 0;
}
</style>