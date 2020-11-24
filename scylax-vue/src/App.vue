<template>
  <v-app style="background-color : #d8dbe2">
    <v-main>
      <component :is="selectedTab"></component>
    </v-main>

    <v-navigation-drawer
      app
      permanent
      expand-on-hover
      color="#58A4B0"
      dark
      absolute
      height="100%"
    >
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-menu</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Menu</v-list-item-title>
      </v-list-item>
      <v-divider></v-divider>
      <v-list dense>
        <v-list-item 
          v-for="(item, index) in menuItems" 
          :key="index"
          link
          @click="selectedTab = item.componentName"
        >
          <v-list-item-icon>
            <v-icon>{{item.icon}}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-app>
</template>

<script>
import RedesDeColaboracao from './components/RedesDeColaboracao.vue'
import ProgPosGrad from './components/ProgPosGrad.vue'
import Pesquisador from './components/Pesquisador.vue'

export default {
  name: 'App',

  components: {
    RedesDeColaboracao,
    ProgPosGrad,
    Pesquisador
  },

  data: () => ({
    menuItems: [
      {title: "Redes de colaboração", icon: "mdi-lan", componentName: "RedesDeColaboracao"},
      {title: "Programas de pós-graduação", icon: "mdi-bank", componentName: "ProgPosGrad"},
      {title: "Pesquisadores", icon: "mdi-account", componentName: "Pesquisador"}
    ],

    selectedTab: null,
  }),
};
</script>
