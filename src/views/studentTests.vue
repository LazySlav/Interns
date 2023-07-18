<template>
  <div class="studentTests">
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
          <v-cont class="big">
            <v-inters-list v-if="inters.length > 0">
              <v-tests-list-item
                  v-for="inter in inters"
                  :key="inter.id"
                  :inter_data="inter"
              />
            </v-inters-list>
            <div v-else
                 class="warn-message"
            >
              {{ warnMessage }}
            </div>
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
import vIntersList from "../components/v-inters-list";
import vTestsListItem from "../components/v-tests-list-item";
export default {
  name: "studentTests",
  components: {
    VMainWrapper,
    vHeader,
    vSidebar,
    vSidebarLink,
    vCont,
    vIntersList,
    vTestsListItem,
  },
  data() {
    return {
      article: 'Тестовые задания',
      warnMessage: 'Пока нет доступных или выполненных тестовых заданий!',

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
          active: false,
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
          active: true,
        },
      ],
      inters: [
        {
          id: 1,
          title: 'nesciunt iure omnis dolorem tempora et accusantium',
          description: 'dignissimos aperiam dolorem qui eum\\nfacilis quibusdam animi sint suscipit qui sint possimus cum\\nquaerat magni maiores excepturi\\nipsam ut commodi dolor voluptatum modi aut vitae',
          status: 1,
        },
        {
          id: 2,
          title: 'nesciunt iure omnis dolor',
          description: 'dignissimos aperiam dolorem qui eum\\nfacilis quibusdam animi sint suscipit qui sint possimus cum\\nquaerat magni maiores excepturi\\nipsam ut commodi dolor voluptatum modi aut vitae',
          status: 1,
        },
        {
          id: 3,
          title: 'nesciunt iure omnis dolorem tempora et accusantium',
          description: 'dignissimos aperiam',
          status: 1,
        },
        {
          id: 4,
          title: 'nesciunt iure omnis dolor',
          description: 'dignissimos aperiam dolorem qui eum\\nfacilis quibusdam animi sint suscipit qui sint possimus cum\\nquaerat magni maiores excepturi\\nipsam ut commodi dolor voluptatum modi aut vitae',
          status: 2,
        },
        {
          id: 5,
          title: 'nesciunt iure omnis dolor',
          description: 'dignissimos aperiam dolorem qui eum\\nfacilis quibusdam animi sint suscipit qui sint possimus cum\\nquaerat magni maiores excepturi\\nipsam ut commodi dolor voluptatum modi aut vitae',
          status: 2,
        },
        {
          id: 6,
          title: 'nesciunt iure omnis dolor',
          description: 'dignissimos aperiam dolorem qui eum\\nfacilis quibusdam animi sint suscipit qui sint possimus cum\\nquaerat magni maiores excepturi\\nipsam ut commodi dolor voluptatum modi aut vitae',
          status: 3,
        },
      ]
    }
  }
}
</script>

<style lang="scss">
.warn-message {
  color: #EB5757;
  font-size: 16px;
  font-weight: 700;
}
@media (max-width: 767px) {
  .v-main-cont {
    flex-direction: column;
    align-items: center;
  }
  .layout-main {
    width: 100%;
  }
}
</style>