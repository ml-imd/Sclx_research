<template>  
    <v-container
        fluid
        class="pa-6"
    >
        <v-row>
            <v-col>
                <v-card 
                    width="100%"
                    height="100%"
                    color="#424C63"
                    dark
                >
                    <v-row>
                        <v-col>
                            <v-card-title>
                                Redes de Colaboração
                            </v-card-title>
                            <v-card-text>
                                Selecione uma rede de pesquisadores e analise as produções em comum do conjunto.
                            </v-card-text>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="11">
                <v-text-field
                    v-model="searchedAuthor"
                    color="#424C63"
                    background-color="white"
                    placeholder=" Adicionar pesquisador"
                    filled
                    append-icon="mdi-close"
                    prepend-inner-icon="mdi-account-plus"
                    @keyup.enter="addAuthor"
                    @click:append="searchedAuthor = ''"
                ></v-text-field>
            </v-col>
            <v-col cols="1">
                <v-btn
                    small
                    class="mt-2"
                    fab
                    dark
                    color="#424C63"
                    @click="addAuthor"
                >
                    <v-icon>mdi-plus</v-icon>
                </v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-card
                    v-if="network.length > 0"
                    width="100%"
                    color="#424C63"
                >
                    
                    <v-card-title 
                        class="white--text"
                    >
                        Rede de Colaboração
                    </v-card-title>

                    <v-list>
                        <v-list-item 
                            v-for="(author, index) in network" 
                            :key="index"
                        >
                            <v-list-item-avatar>
                                <v-icon>mdi-account</v-icon>
                            </v-list-item-avatar>

                            <v-list-item-content>
                                <v-list-item-title>{{author}}</v-list-item-title>
                            </v-list-item-content>

                            <v-spacer></v-spacer>

                            <v-list-item-action>
                                <v-btn icon @click="removeAuthor(index)">
                                    <v-icon>mdi-delete</v-icon>
                                </v-btn>
                            </v-list-item-action>
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card v-if="network.length > 1">
                    <v-tabs
                        v-model="currentTab"
                        background-color="#424C63"
                        dark
                        grow
                    >
                        <v-tab>
                            Resumo
                        </v-tab>
                        <v-tab-item>
                            <RedesAbaResumo />
                        </v-tab-item>
                        <v-tab>
                            Produções
                        </v-tab>
                        <v-tab-item>
                            <RedesAbaProducoes />
                        </v-tab-item>
                        <v-tab>
                            Colaboração
                        </v-tab>
                        <v-tab-item>
                            <RedesAbaColaboracao />
                        </v-tab-item>
                    </v-tabs>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import RedesAbaColaboracao from './RedesAbaColaboracao.vue'
import RedesAbaProducoes from './RedesAbaProducoes.vue'
import RedesAbaResumo from './RedesAbaResumo.vue'

export default {
    name: "RedesDeColaboração",

    components: {
        RedesAbaColaboracao,
        RedesAbaProducoes,
        RedesAbaResumo
    },

    data: () => ({
        searchedAuthor: "",
        network: [],
        currentTab: "",
    }),

    methods: {
        addAuthor: function(){
            if(this.searchedAuthor != ""){
                this.network.push(this.searchedAuthor);
            }
        },

        removeAuthor: function(index){
            this.network.splice(index, 1);
        }
    }
}
</script>