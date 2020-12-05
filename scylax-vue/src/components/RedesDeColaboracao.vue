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
            <v-col cols="10">
                <v-autocomplete
                    :items="researchersList"
                    chips
                    deletable-chips
                    multiple
                    v-model="network"
                    color="#424C63"
                    background-color="white"
                    label=" Adicionar pesquisadores"
                    filled
                ></v-autocomplete>
            </v-col>
            <v-col>
                <v-btn
                    :disabled="network.length < 2"
                    block
                    height="68"
                    dark
                    color="#424C63"
                    @click="analyzeNetwork"
                >
                    Analisar rede
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
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card v-if="canRender">
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
                            <RedesAbaResumo :networkCoProductions="networkCoProductions"/>
                        </v-tab-item>
                        <v-tab>
                            Detalhes
                        </v-tab>
                        <v-tab-item>
                            <RedesAbaDetalhes />
                        </v-tab-item>
                    </v-tabs>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import autores_nomes from '../assets/autores_nomes.json'
import tabela_autores from '../assets/tabela_autores_ufrn.json'
import RedesAbaDetalhes from './RedesAbaDetalhes.vue'
import RedesAbaResumo from './RedesAbaResumo.vue'

export default {
    name: "RedesDeColaboração",

    components: {
        RedesAbaDetalhes,
        RedesAbaResumo
    },

    data: () => ({
        network: [],
        networkCoProductions: [],
        subNetworkProductions: {},
        currentTab: "",
        canRender: false,
        authorsDataset: tabela_autores,
        researchersList: autores_nomes,
    }),

    methods: {
        analyzeNetwork: function(){
            var authorsProductions = {}, allSubNetworks = [], snProductionsList = [];
            this.subNetworkProductions = this.networkCoProductions = {};

            for(let i = 0; i < this.network.length; i++){
                authorsProductions[this.network[i]] = [];
            }

            for(let i = 0; i < this.authorsDataset.length; i++){
                if(this.authorsDataset[i].nome_normalizado in authorsProductions){
                    authorsProductions[this.authorsDataset[i].nome_normalizado] = authorsProductions[this.authorsDataset[i].nome_normalizado].concat(String(this.authorsDataset[i].producoes).split(", "));
                }
            }

            allSubNetworks = this.getCombinations(this.network).filter(a => a.length >= 2 && a.length < this.network.length);

            for(let i = 0; i < allSubNetworks.length; i++){
                snProductionsList = []
                
                for(let j = 0; j < allSubNetworks[i].length; j++){
                    snProductionsList.push(authorsProductions[allSubNetworks[i][j]])
                }

                this.subNetworkProductions[allSubNetworks[i]] = snProductionsList.reduce((a, b) => a.filter(c => b.includes(c)));
            }

            this.networkCoProductions = Object.values(authorsProductions).reduce((a, b) => a.filter(c => b.includes(c)));

            if(this.networkCoProductions.length > 0){
                this.canRender = true;
            } else { 
                this.canRender = false;
            }
        },

        getCombinations: function(array){
            return new Array(1 << array.length).fill().map((e1, i) => array.filter((e2, j) => i & 1 << j));
        }
    },
}
</script>