<template>  
    <v-container
        fluid
        class="pa-6"
    >
        <v-row>
            <v-col cols="11">
                <v-text-field
                    v-model="searchedAuthor"
                    dark
                    background-color="#58A4B0"
                    label=" Adicionar pesquisador"
                    solo
                    append-icon="mdi-close"
                    prepend-inner-icon="mdi-account-plus"
                    @keyup.enter="addAuthor"
                    @click:append="searchedAuthor = ''"
                ></v-text-field>
            </v-col>
            <v-col cols="1">
                <v-btn
                    small
                    class="mt-1"
                    fab
                    dark
                    color="#58A4B0"
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
                    color="#58A4B0"
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
                        background-color="#58A4B0"
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