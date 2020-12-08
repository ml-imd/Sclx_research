<template>
  <div class="text-end mx-6">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          icon
          dark
          v-bind="attrs"
          v-on="on"
          small
        >
          <v-icon small>mdi-help</v-icon>
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2">
          Ajuda
        </v-card-title>

        <v-carousel :show-arrows="false">
          <v-carousel-item>
            <v-card-text style="color: black">
              Para mudar a cor de uma agregação, clique na legenda e escolha uma cor.
              <v-divider></v-divider>
              <v-img src="@/assets/help1.png"></v-img>
            </v-card-text>
          </v-carousel-item>
          <v-carousel-item>
            <v-card-text style="color: black">
              Para remover uma agregação da exibição no gráfico, selecione o item na legenda e clique no menos.
              <v-divider></v-divider>
              <v-img src="@/assets/help2.png"></v-img>
            </v-card-text>
          </v-carousel-item>
          <v-carousel-item>
            <v-card-text style="color: black">
              Para visualizar apenas a agregação desejada, clique nela no gráfico ou clique na legenda e no mais.
              <v-divider></v-divider>
              <v-img src="@/assets/help3.png"></v-img>
            </v-card-text>
          </v-carousel-item>
          <v-carousel-item>
            <v-card-text style="color: black">
              Podemos refinar o nosso gráfico utilizando filtros. Ao criar um filtro estaremos exibindo um subconjunto dos dados exibidos.
              <v-divider></v-divider>
              <v-img src="@/assets/help4.png"></v-img>
            </v-card-text>
          </v-carousel-item>
        </v-carousel>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
    name: 'Help',    

    data: () => ({
      dialog: false,
    }),
}
</script>