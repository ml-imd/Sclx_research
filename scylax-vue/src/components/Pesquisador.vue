<template>
    <v-container 
        fluid
        class="pa-6"
    >
        <v-row>
            <v-col cols="9">
                <v-card 
                    width="100%"
                    height="100%"
                    color="#424C63"
                    dark
                >
                    <v-row>
                        <v-col>
                            <v-card-title>
                                Análise de Pesquisadores
                            </v-card-title>
                            <v-card-text>
                                Agrupe pesquisadores e observe, com foco nas produções científicas e nos índices de qualidade através do tempo, qual o posicionamento de um pesquisador ou agrupamento frente a outros.
                            </v-card-text>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-container>
                            <v-expansion-panels flat focusable>
                                <v-expansion-panel>
                                    <v-expansion-panel-header color="#424C63" disable-icon-rotate>
                                        Mais
                                        <template v-slot:actions>
                                            <v-icon>
                                                mdi-plus
                                            </v-icon>
                                        </template>
                                    </v-expansion-panel-header>
                                    <v-expansion-panel-content color="#424C63">
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                                    </v-expansion-panel-content>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </v-container>
                    </v-row>
                </v-card>
            </v-col>
            <v-col class="d-flex justify-center">
                <v-card 
                    width="100%" 
                    color="#424C63"
                    dark
                >
                    <v-card-title class="justify-center">
                        Número de grupos
                    </v-card-title>
                    <v-card-actions class="justify-center">
                        <v-btn 
                            icon
                            @click="numberOfClusters > 2 ? numberOfClusters-- : numberOfClusters"
                        >
                            <v-icon>mdi-minus</v-icon>
                        </v-btn>
                        <h1 class="mx-6">{{numberOfClusters}}</h1>
                        <v-btn 
                            icon
                            @click="numberOfClusters < 4 ? numberOfClusters++ : numberOfClusters"
                        >
                            <v-icon>mdi-plus</v-icon>
                        </v-btn>
                    </v-card-actions>
                    <v-card-actions class="justify-center">
                        <v-tooltip bottom>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn
                                    dark
                                    v-bind="attrs"
                                    v-on="on"
                                    @click="updateGroupGraphs"
                                    text
                                >
                                    Atualizar Gráficos
                                    <v-icon class="ml-1" small>mdi-refresh</v-icon>
                                </v-btn>
                            </template>
                            <span>Atualizar gráficos</span>
                        </v-tooltip>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card v-if="canRender" width="100%" color="#fafbfd">
                    <v-container>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Publicações por década por grupo</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="total_by_cluster" height="500" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">H-index médio por grupo</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="h_index_average" height="300" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63" height="100%">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Colaboração internacional média por grupo</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="average_n_colab" height="300" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Média de pesq. em colaborações internacionais por grupo</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="average_p_colab" height="300" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Publicações por grupo por qualis na década 1</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="researcher_qualis_d1" height="500" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Publicações por grupo por qualis na década 2</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="researcher_qualis_d2" height="500" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Publicações por grupo por qualis na década 3</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="researcher_qualis_d3" height="500" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Publicações por grupo por qualis na década 4</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="researcher_qualis_d4" height="500" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card v-if="canRender" width="100%" color="#fafbfd">
                    <v-card-actions style="background-color : #424C63">
                        <v-container>
                            <v-row>
                                <v-col cols="9">
                                    <v-autocomplete
                                        v-model="researcher"
                                        :items="researchersList"
                                        deletable-chips
                                        chips
                                        color="#424C63"
                                        background-color="white"
                                        label="Analisar pesquisador"
                                        filled
                                    ></v-autocomplete>
                                </v-col>
                                <v-col>
                                    <v-btn 
                                        color="white"
                                        large
                                        height="68"
                                        @click="updateResearcherGraphs"
                                        :disabled="researcher == ''"
                                    >
                                        Analisar pesquisador
                                        <v-icon>mdi-menu-right</v-icon>
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-actions>
                    <v-container>
                        <div v-if="canRenderResearcher" :key="researcherComponentKey">
                            <v-row>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Publicações por década</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="single_researcher_total_prod" height="500" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-card color="#424C63">
                                        <iframe :src="single_researcher_scores" height="300" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Publicações por qualis na década 1</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="single_researcher_qualis_d1" height="500" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Publicações por qualis na década 2</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="single_researcher_qualis_d2" height="500" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Publicações por qualis na década 3</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="single_researcher_qualis_d3" height="500" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Publicações por qualis na década 4</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="single_researcher_qualis_d4" height="500" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                            </v-row>
                        </div>
                    </v-container>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import autores_nomes from '../assets/autores_nomes.json'
import Help from './Help.vue'

export default {
    name: "Pesquisador",

    components: {
        Help,
    },

    data: () => ({
        numberOfClusters: 2,
        canRender: false,
        canRenderResearcher: false,
        researcher: "",
        clusterUrlId: "",
        mainResearcher: "",
        clusterUrlIdList: {
            2 : "cluster_k2",
            3 : "cluster_k3",
            4 : "cluster_k4",
        },
        researcherComponentKey: 0,
        fontSize: 30,
        researchersList: autores_nomes,
    }),

    methods: {
        updateGroupGraphs: function(){
            this.canRender = true;
            this.clusterUrlId = this.clusterUrlIdList[this.numberOfClusters];
        },

        updateResearcherGraphs: function(){
            this.researcherComponentKey += 1;
            this.canRenderResearcher = true;
            this.mainResearcher = this.researcher;
        }
    },

    computed: {

        //PESQUISADORES SECAO UM
        researcher_qualis_d1: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d1_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d1_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d1_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d1_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d1_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d1_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d1_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d1_B4),schema:metric,type:sum),(enabled:!t,id:'10',params:(customLabel:Grupos,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d1_C%2FNI%2FNP),schema:metric,type:sum)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        },
        
        researcher_qualis_d2: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d2_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d2_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d2_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d2_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d2_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d2_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d2_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d2_B4),schema:metric,type:sum),(enabled:!t,id:'10',params:(customLabel:Grupos,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d2_C%2FNI%2FNP),schema:metric,type:sum)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        },
        
        researcher_qualis_d3: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d3_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d3_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d3_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d3_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d3_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d3_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d3_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d3_B4),schema:metric,type:sum),(enabled:!t,id:'10',params:(customLabel:Grupos,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d3_C%2FNI%2FNP),schema:metric,type:sum)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        },
        
        researcher_qualis_d4: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d4_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d4_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d4_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d4_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d4_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d4_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d4_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d4_B4),schema:metric,type:sum),(enabled:!t,id:'10',params:(customLabel:Grupos,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d4_C%2FNI%2FNP),schema:metric,type:sum)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        },

        h_index_average: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'H-index%20m%C3%A9dio',field:h_index),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:'H-index%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:'H-index%20m%C3%A9dio'),type:value))),title:'',type:histogram))"
        },

        average_n_colab: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'M%C3%A9dia%20de%20colabora%C3%A7%C3%B5es',field:n_colab_inter),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:'M%C3%A9dia%20de%20colabora%C3%A7%C3%B5es'),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:'M%C3%A9dia%20de%20colabora%C3%A7%C3%B5es'),type:value))),title:'',type:histogram))"
        },

        average_p_colab: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'M%C3%A9dia%20de%20colaboradores',field:p_colab_inter),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:'M%C3%A9dia%20de%20colaboradores'),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:'M%C3%A9dia%20de%20colaboradores'),type:value))),title:'',type:histogram))"
        },
        /**
        h_index_average: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'H-index%20m%C3%A9dio',field:h_index),schema:metric,type:avg),(enabled:!t,id:'2',params:(field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:" + this.fontSize + ",labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        average_n_colab: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Colabora%C3%A7%C3%A3o%20internacional%20m%C3%A9dia',field:n_colab_inter),schema:metric,type:avg),(enabled:!t,id:'2',params:(field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:" + this.fontSize + ",labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },
        
        average_p_colab: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'M%C3%A9dia%20de%20colaboradores',field:p_colab_inter),schema:metric,type:avg),(enabled:!t,id:'2',params:(field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:" + this.fontSize + ",labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },
        **/

        total_by_cluster: function(){
            return "http://localhost:5601/app/visualize#/edit/af8cf470-32b2-11eb-965f-ff26f33090ed?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Década 1',field:d1_total),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:'Década 2',field:d2_total),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:'Década 3',field:d3-total),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:'Década 4',field:d4_total),schema:metric,type:sum),(enabled:!t,id:'10',params:(customLabel:Grupos,field:" + this.clusterUrlId + ",missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!t),legendPosition:right,seriesParams:!((data:(id:'1',label:'Década 1'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:'Década 2'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:'Década 3'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:'Década 4'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:researcher_total_prod,type:histogram))"
        },

        //PESQUISADORES SECAO DOIS
        single_researcher_total_prod: function(){
            return "http://localhost:5601/app/visualize#/edit/af8cf470-32b2-11eb-965f-ff26f33090ed?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Década 1',field:d1_total),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:'Década 2',field:d2_total),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:'Década 3',field:d3-total),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:'Década 4',field:d4_total),schema:metric,type:sum),(enabled:!t,id:'5',params:(filters:!((input:(language:kuery,query:'nome_normalizado%20:" + this.mainResearcher + "'),label:'" + this.mainResearcher + "'))),schema:segment,type:filters)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!t),legendPosition:right,seriesParams:!((data:(id:'1',label:'Década 1'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:'Década 2'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:'Década 3'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:'Década 4'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:researcher_total_prod,type:histogram))"
        },

        single_researcher_scores: function(){
            return "http://localhost:5601/app/visualize#/edit/5d2fe700-32b2-11eb-965f-ff26f33090ed?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:H-index,field:h_index),schema:metric,type:avg),(enabled:!t,id:'3',params:(customLabel:'Colabora%C3%A7%C3%B5es%20internacionais',field:n_colab_inter),schema:metric,type:avg),(enabled:!t,id:'4',params:(customLabel:'Colabores%20internacionais',field:p_colab_inter),schema:metric,type:avg),(enabled:!t,id:'5',params:(field:nome_normalizado,include:'" + this.mainResearcher + "',missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:" + this.fontSize + ",labelColor:!f,subText:''),useRanges:!f),type:metric),title:researcher_scores,type:metric))"
        },

        single_researcher_qualis_d1: function(){
            return "http://localhost:5601/app/visualize#/edit/a5023e80-32b1-11eb-965f-ff26f33090ed?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d1_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d1_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d1_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d1_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d1_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d1_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d1_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d1_B4),schema:metric,type:sum),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d1_C%2FNI%2FNP),schema:metric,type:sum),(enabled:!t,id:'12',params:(customLabel:'',field:nome_normalizado,include:'" + this.mainResearcher + "',missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:researcher_qualis,type:histogram))"
        },

        single_researcher_qualis_d2: function(){
            return "http://localhost:5601/app/visualize#/edit/a5023e80-32b1-11eb-965f-ff26f33090ed?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d1_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d2_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d2_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d2_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d2_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d2_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d2_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d2_B4),schema:metric,type:sum),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d2_C%2FNI%2FNP),schema:metric,type:sum),(enabled:!t,id:'12',params:(customLabel:'',field:nome_normalizado,include:'" + this.mainResearcher + "',missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:researcher_qualis,type:histogram))"
        },

        single_researcher_qualis_d3: function(){
            return "http://localhost:5601/app/visualize#/edit/a5023e80-32b1-11eb-965f-ff26f33090ed?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d3_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d3_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d3_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d3_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d3_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d3_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d3_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d3_B4),schema:metric,type:sum),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d3_C%2FNI%2FNP),schema:metric,type:sum),(enabled:!t,id:'12',params:(customLabel:'',field:nome_normalizado,include:'" + this.mainResearcher + "',missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:researcher_qualis,type:histogram))"
        },

        single_researcher_qualis_d4: function(){
            return "http://localhost:5601/app/visualize#/edit/a5023e80-32b1-11eb-965f-ff26f33090ed?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23F2C96D,A4:%23CCA300,B1:%23EA6460,B2:%23890F02,B3:%2358140C,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:A1,field:d4_A1),schema:metric,type:sum),(enabled:!t,id:'2',params:(customLabel:A2,field:d4_A2),schema:metric,type:sum),(enabled:!t,id:'3',params:(customLabel:A3,field:d4_A3),schema:metric,type:sum),(enabled:!t,id:'4',params:(customLabel:A4,field:d4_A4),schema:metric,type:sum),(enabled:!t,id:'5',params:(customLabel:B1,field:d4_B1),schema:metric,type:sum),(enabled:!t,id:'6',params:(customLabel:B2,field:d4_B2),schema:metric,type:sum),(enabled:!t,id:'7',params:(customLabel:B3,field:d4_B3),schema:metric,type:sum),(enabled:!t,id:'8',params:(customLabel:B4,field:d4_B4),schema:metric,type:sum),(enabled:!t,id:'11',params:(customLabel:C%2FNI%2FNP,field:d4_C%2FNI%2FNP),schema:metric,type:sum),(enabled:!t,id:'12',params:(customLabel:'',field:nome_normalizado,include:'" + this.mainResearcher + "',missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:A1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'2',label:A2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:A3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:A4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:B1),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'6',label:B2),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'7',label:B3),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'8',label:B4),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'11',label:C%2FNI%2FNP),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:researcher_qualis,type:histogram))"
        },
    },
}
</script>