<template>
  <div class="studentChat">
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
            <v-block
                v-if="chatList.length > 0"
            >
              <v-chat-list>
                <v-chat-list-item
                  v-for="chat in chatList"
                  :key="chat.id"
                  :chat_data="chat"
                />
              </v-chat-list>
            </v-block>
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
import vBlock from "../components/v-block";
import vChatList from "../components/v-chat-list";
import vChatListItem from "../components/v-chat-list-item";
export default {
  name: "studentChat",
  components: {
    VMainWrapper,
    vHeader,
    vSidebar,
    vSidebarLink,
    vCont,
    vBlock,
    vChatList,
    vChatListItem,
  },
  data() {
    return {
      article: 'Чаты',
      warnMessage: 'Пока нет доступных чатов',

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
          active: true,
        },
        {
          id: 4,
          path: '/student/tests',
          text: 'Тесты',
          active: false,
        },
      ],
      chatList: [
        {
          id: 1,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 100,
        },
        {
          id: 2,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 6,
        },
        {
          id: 3,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 0,
        },
        {
          id: 4,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 4,
        },
        {
          id: 5,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 0,
        },
        {
          id: 6,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 65,
        },
        {
          id: 7,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 21,
        },
        {
          id: 8,
          article: 'Название компании',
          lastMessage: 'Это последнее сообщение в чате с команией',
          unreadCounter: 0,
        },
      ],
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