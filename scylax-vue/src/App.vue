<template>
  <v-app>
    <v-main>
      <RedesDeColaboracao/>
    </v-main>

    <v-navigation-drawer
      permanent
      expand-on-hover
      color="#58A4B0"
      dark
      absolute
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

export default {
  name: 'App',

  components: {
    RedesDeColaboracao
  },

  data: () => ({
    menuItems: [
      {title: "Redes de colaboração", icon: "mdi-lan"},
      {title: "Programas de pós-graduação", icon: "mdi-bank"},
      {title: "Pesquisadores", icon: "mdi-account"}
    ],
  }),
};
</script>
