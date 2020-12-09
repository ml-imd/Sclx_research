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
                    <div class="text-end" style="background-color : #424C63">
                        <v-tooltip bottom color="white">
                            <template v-slot:activator="{ on, attrs }">
                                <v-icon
                                dark
                                v-bind="attrs"
                                v-on="on"
                                small
                                >
                                mdi-help
                                </v-icon>
                            </template>
                            <span style="color:black">Para fazer uma análise de uma rede de colaboração você deve adicionar o nome dos pesquisadores e clicar em analisar rede.</span>
                        </v-tooltip>
                    </div>
                    <v-row>
                        <v-col>
                            <v-card-title class="pt-0">
                                Redes de Colaboração
                            </v-card-title>
                            <v-card-text>
                                Selecione uma rede de pesquisadores e analise as produções em comum do conjunto.
                            </v-card-text>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-container>
                            <v-expansion-panels flat focusable>
                                <v-expansion-panel>
                                    <v-expansion-panel-header color="#424C63">
                                        Mais
                                    </v-expansion-panel-header>
                                    <v-expansion-panel-content color="#424C63">
                                        <p>Uma rede de colaboração é dada por um grupo de autores que possui pelo menos uma publicação em comum. Além desse conceito, também é utilizado o conceito de sub-rede, que compreende qualquer subconjunto entre os autores que compõem uma rede de colaboração.</p>

                                        <p>Esta funcionalidade objetiva analisar qualitativamente uma rede de colaboração e também identificar seus pontos mais fortes e menos fortes. Isso é feito através dos índices dos autores que compõem uma rede e também através dos índices das publicações produzidas pela rede.</p>

                                        <p>No sistema, a funcionalidade foi dividida em três partes: resumo - produção; resumo - colaboração; e detalhes. Na primeira, resumo - produção, são exibidos os dados gerais da rede como um todo. Na segunda, resumo - colaboração, são exibidas informações relacionadas à colaborações internacionais com participação da rede. Na terceira e última parte, detalhes, são detalhadas informações relativas às sub-redes possíveis para a rede de colaboração em questão.</p>
                                    </v-expansion-panel-content>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </v-container>
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
                <v-card v-if="canRender" :key="key">
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
                            <RedesAbaResumo :networkCoProductions="networkCoProductions" :authorsProductions="authorsProductions"/>
                        </v-tab-item>
                        <v-tab>
                            Detalhes
                        </v-tab>
                        <v-tab-item>
                            <RedesAbaDetalhes :subNetworkProductions="subNetworkProductions" :authorsProductions="authorsProductions"/>
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
        key: 0,
        network: [],
        networkCoProductions: [],
        subNetworkProductions: {},
        authorsProductions: {},
        currentTab: "",
        canRender: false,
        authorsDataset: tabela_autores,
        researchersList: autores_nomes,
    }),

    methods: {
        analyzeNetwork: function(){
            this.key++;
            this.authorsProductions = {};
            var allSubNetworks = [], snProductionsList = [];
            this.subNetworkProductions = this.networkCoProductions = {};

            for(let i = 0; i < this.network.length; i++){
                this.authorsProductions[this.network[i]] = [];
            }

            for(let i = 0; i < this.authorsDataset.length; i++){
                if(this.authorsDataset[i].nome_normalizado in this.authorsProductions){
                    this.authorsProductions[this.authorsDataset[i].nome_normalizado] = this.authorsProductions[this.authorsDataset[i].nome_normalizado].concat(String(this.authorsDataset[i].producoes).split(", "));
                }
            }

            allSubNetworks = this.getCombinations(this.network).filter(a => a.length >= 2);

            for(let i = 0; i < allSubNetworks.length; i++){
                snProductionsList = []
                
                for(let j = 0; j < allSubNetworks[i].length; j++){
                    snProductionsList.push(this.authorsProductions[allSubNetworks[i][j]])
                }

                this.subNetworkProductions[allSubNetworks[i]] = snProductionsList.reduce((a, b) => a.filter(c => b.includes(c)));
            }

            this.networkCoProductions = Object.values(this.authorsProductions).reduce((a, b) => a.filter(c => b.includes(c)));

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