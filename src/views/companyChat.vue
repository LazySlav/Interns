<template>
  <div class="companyChat">
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
import vHeaderComp from '../components/v-headerComp'
import VMainWrapper from "@/components/v-main-wrapper";
import vSidebar from "../components/v-sidebar";
import vSidebarLink from "../components/v-sidebar-link";
import vCont from "../components/v-cont";
import vBlock from "../components/v-block";
import vChatList from "../components/v-chat-list";
import vChatListItem from "../components/v-chat-list-item";
export default {
  name: "companyChat",
  components: {
    VMainWrapper,
    vHeaderComp,
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
          active: false,
        },
        {
          id: 3,
          path: '/company/chat',
          text: 'Чаты',
          active: true,
        },
      ],
      chatList: [
        {
          id: 1,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
          unreadCounter: 100,
        },
        {
          id: 2,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
          unreadCounter: 6,
        },
        {
          id: 3,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
          unreadCounter: 0,
        },
        {
          id: 4,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
          unreadCounter: 4,
        },
        {
          id: 5,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
          unreadCounter: 0,
        },
        {
          id: 6,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
          unreadCounter: 65,
        },
        {
          id: 7,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
          unreadCounter: 21,
        },
        {
          id: 8,
          article: 'Имя студента',
          lastMessage: 'Это последнее сообщение в чате со студентом',
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