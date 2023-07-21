<template>
  <div class="companyRequests">
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
          <v-cont class="big">
            <v-inters-list v-if="inters.length > 0">
              <v-inters-list-item
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
            <router-link
                to="/company/requests/create"
                custom
                v-slot="{ navigate }"
            >
              <v-buttton
                  @click="navigate"
                  role="link"
              >
                Создать
              </v-buttton>
            </router-link>
          </v-cont>
        </div>
      </div>
    </v-main-wrapper>
  </div>
</template>
<script>
import vHeaderComp from '../components/v-headerComp';
import VMainWrapper from "@/components/v-main-wrapper";
import vSidebar from "../components/v-sidebar";
import vSidebarLink from "../components/v-sidebar-link";
import vCont from "../components/v-cont";
import vIntersList from "../components/v-inters-list";
import vIntersListItem from "../components/v-inters-list-item";
import vButtton from "@/components/v-button.vue";

export default {
  name: "companyRequests",
  components: {
    VMainWrapper,
    vHeaderComp,
    vSidebar,
    vSidebarLink,
    vCont,
    vButtton,
    vIntersList,
    vIntersListItem,
  },
  data() {
    return {
      article: 'Заявки',
      warnMessage: 'Пока нет активных заявков!',

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
      inters: [
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