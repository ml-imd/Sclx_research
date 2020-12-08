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
                                Análise da Produção Científica de Programas de Pós-graduação
                            </v-card-title>
                            <v-card-text>
                                Agrupe programas de pós graduação e observe, com foco nas produções científicas e seus índices, qual o posicionamento de um programa ou agrupamento frente a outros.
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
                    <div class="text-end mt-1 mr-1">
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
                            <span style="color:black">Podemos alterar o número de grupos que estamos trabalhando utilizando o '+' e o '-'. Devemos atualizar os gráficos ao final desta operação.</span>
                        </v-tooltip>
                    </div>
                    <v-card-title class="justify-center pt-0">
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
                            @click="numberOfClusters < 5 ? numberOfClusters++ : numberOfClusters"
                        >
                            <v-icon>mdi-plus</v-icon>
                        </v-btn>
                    </v-card-actions>
                    <v-card-actions class="justify-center">
                        <v-btn
                            dark
                            @click="updateGroupGraphs"
                            text
                        >
                            Atualizar Gráficos
                            <v-icon class="ml-1" small>mdi-refresh</v-icon>
                        </v-btn>
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
                                        <h3 class="pl-5" style="color: white">Quantidade de programas por grupo</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="prog_per_cluster" height="200" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Publicações por grupo por ano</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="pub_by_year" height="500" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Índices médios por grupo</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="scores_average" height="300" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Publicações por grupo por qualis</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="cluster_qualis" height="500" width="100%" frameBorder="0"></iframe>
                                </v-card>
                            </v-col>
                            <v-col>
                                <v-card color="#424C63">
                                    <v-row>
                                        <h3 class="pl-5" style="color: white">Qualidade de publicações por grupo</h3>
                                        <v-spacer></v-spacer>
                                        <Help />
                                    </v-row>
                                    <iframe :src="cluster_qualis_gsb" height="500" width="100%" frameBorder="0"></iframe>
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
                            <span style="color:black">Para analisar um programa basta digitar seu nome no campo 'analisar programa', escolher um grupo e clicar em 'Analisar Programa'. Se o campo ‘comparar com programas’ estiver vazio, nenhuma comparação será realizada, caso contrário, será realizada uma comparação entre os programas escolhidos.</span>
                        </v-tooltip>
                    </div>
                    <v-card-actions style="background-color : #424C63">
                        <v-container>
                            <v-row>
                                <v-col>
                                    <v-autocomplete
                                        v-model="program"
                                        :items="programList"
                                        chips
                                        deletable-chips
                                        color="#424C63"
                                        background-color="white"
                                        label="Analisar programa"
                                        filled
                                    ></v-autocomplete>
                                </v-col>
                                <v-col>
                                    <v-select
                                        :items="selectionProgramClusters"
                                        v-model="groupSelect"
                                        label="Grupo"
                                        filled
                                        color="#424C63"
                                        background-color="white"
                                        height="68"
                                    ></v-select>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="9">
                                    <v-autocomplete
                                        v-model="compareProgramList"
                                        :items="programList"
                                        multiple
                                        deletable-chips
                                        chips
                                        color="#424C63"
                                        filled
                                        label="Comparar com programas"
                                        background-color="white"
                                    >
                                    </v-autocomplete>
                                </v-col>
                                <v-col>
                                    <v-btn
                                        color="white"
                                        large
                                        height="69"
                                        @click="updateProgramGraphs"
                                        :disabled="program == '' || groupSelect == ''"
                                    >
                                        Analisar Programa 
                                        <v-icon >mdi-menu-right</v-icon>
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-actions>
                    <v-container>
                        <div v-if="canRenderProgram" :key="programComponentKey">
                            <v-row>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Métricas médias por programa</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="program_average_scores" height="300" width="100%" frameBorder="0"></iframe>                                    
                                    </v-card>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Publicações por qualis por programa</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="program_qualis" height="500" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Qualidade de publicações por programa</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="program_qualis_gsb" height="500" width="100%" frameBorder="0"></iframe>
                                    </v-card>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-card color="#424C63">
                                        <v-row>
                                            <h3 class="pl-5" style="color: white">Distribuição de qualis estrato por programa</h3>
                                            <v-spacer></v-spacer>
                                            <Help />
                                        </v-row>
                                        <iframe :src="program_qualis_estrato" height="500" width="100%" frameBorder="0"></iframe>
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
import programas_nomes from '../assets/programas_nomes.json'
import Help from './Help.vue'

export default {
    name: "ProgPosGrad",

    components: {
        Help,
    },

    data: () => ({
        groupSelect: "",
        numberOfClusters: 2,
        canRender: false,
        clusterUrlId: "",
        program: "",
        mainProgram: "",
        clusterUrlIdList : {
            2 : "cluster_k2",
            3 : "cluster_k3",
            4 : "cluster_k4",
            5 : "cluster_k5"
        },
        mainProgramCluster: "",
        selectionProgramClusters: [],
        compareProgramList: [],
        urlProgramList: "",
        canRenderProgram: false,
        fontSize: 30,
        programComponentKey: 0,
        programList: programas_nomes,
    }),

    methods: {
        updateGroupGraphs: function(){
            this.selectionProgramClusters = [];
            this.canRender = true;
            this.clusterUrlId = this.clusterUrlIdList[this.numberOfClusters];
            for(var k = 0; k < this.numberOfClusters; k++){
                this.selectionProgramClusters.push("cluster" + k);
            }
        },

        updateProgramGraphs: function(){
            this.programComponentKey += 1;
            this.canRenderProgram = true;
            
            this.mainProgramCluster = this.groupSelect;
            this.mainProgram = this.program;

            this.urlProgramList = "(";
            this.urlProgramList += "(input:(language:kuery,query:'programas_nomes.keyword:" + this.mainProgram + "'),label:'" + this.mainProgram + "')";

            for(var i = 0; i < this.compareProgramList.length; i++){
                this.urlProgramList += ",(input:(language:kuery,query:'programas_nomes.keyword:" + this.compareProgramList[i] + "'),label:'" + this.compareProgramList[i] + "')";
            }

            this.urlProgramList += ")";
        },
    },

    computed: {

        //PROGRAMAS SECAO UM
        cluster_qualis: function(){
            return "http://localhost:5601/app/visualize#/edit/88f530d0-2ec4-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'3',params:(customLabel:Qualis,field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:11),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:top,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:cluster_qualis,type:histogram))"
        },

        cluster_qualis_gsb: function(){
            return "http://localhost:5601/app/visualize#/edit/3a2a3670-2f56-11eb-b8d7-2bd9025fb19b?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,Bronze:%2399440A,C%2FNI%2FNP:%233F2B5B,Gold:%23E5AC0E,Silver:%23DEDAF7))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Programa,field:" + this.clusterUrlId + ".keyword,include:'',missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'3',params:(filters:!((input:(language:kuery,query:'qualis.keyword%20:%20%22A1%22%20or%20qualis.keyword%20%0A:%20%22A2%22%20or%20qualis.keyword%20:%20%22A3%22%20or%20qualis.keyword%20:%20%22A4%22'),label:Gold),(input:(language:kuery,query:'qualis.keyword%20:%20%22B1%22%20or%20qualis.keyword%20:%20%22B3%22%20or%20qualis.keyword%20:%20%22B4%22%20or%20qualis.keyword%20:%20%22B2%22%20'),label:Silver),(input:(language:kuery,query:'qualis.keyword%20:%20%22C%2FNI%2FNP%22%20'),label:Bronze))),schema:group,type:filters)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:top,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:cluster_qualis_gsb,type:histogram))"
        },
        
        scores_average: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Citescore%20m%C3%A9dio',field:citescore),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'5',params:(customLabel:'Quartil%20citescore%20m%C3%A9dio',field:quartil_citescore),schema:metric,type:avg),(enabled:!t,id:'3',params:(customLabel:'Percentil%20m%C3%A9dio',field:percentile),schema:metric,type:avg),(enabled:!t,id:'4',params:(customLabel:'Quartil%20percentil%20m%C3%A9dio',field:quartil_percentile),schema:metric,type:avg)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!t),legendPosition:top,orderBucketsBySum:!f,row:!t,seriesParams:!((data:(id:'1',label:'Citescore%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:'Quartil%20citescore%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:'Percentil%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:'Quartil%20percentil%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:'Average%20citescore'),type:value))),title:'',type:histogram))"
        },

        pub_by_year: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=line&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(cluster1:%23447EBC))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Ano,field:ano.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:100),schema:segment,type:terms),(enabled:!t,id:'3',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(),legendPosition:right,orderBucketsBySum:!f,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,interpolate:linear,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:line,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:line,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(defaultYExtents:!f,mode:normal,setYExtents:!f,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:line))"
        },

        prog_per_cluster: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Programas,field:programas.keyword),schema:metric,type:cardinality),(enabled:!t,id:'2',params:(field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:" + this.fontSize*2 + ",labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        //PROGRAMAS SECAO DOIS
        program_qualis: function(){
            return "http://localhost:5601/app/visualize#/edit/f394bf70-2ecc-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(filters:!" + this.urlProgramList + "),schema:segment,type:filters),(enabled:!t,id:'3',params:(customLabel:Qualis,field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:11),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:top,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:program_qualis,type:histogram))"
        },

        program_qualis_gsb: function(){
            return "http://localhost:5601/app/visualize#/edit/c78238c0-2ec4-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,Bronze:%2399440A,C%2FNI%2FNP:%233F2B5B,Gold:%23E5AC0E,Silver:%23DEDAF7))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(filters:!" + this.urlProgramList + "),schema:segment,type:filters),(enabled:!t,id:'3',params:(filters:!((input:(language:kuery,query:'qualis.keyword%20:%20%22A1%22%20or%20qualis.keyword%20%0A:%20%22A2%22%20or%20qualis.keyword%20:%20%22A3%22%20or%20qualis.keyword%20:%20%22A4%22'),label:Gold),(input:(language:kuery,query:'qualis.keyword%20:%20%22B1%22%20or%20qualis.keyword%20:%20%22B3%22%20or%20qualis.keyword%20:%20%22B4%22%20or%20qualis.keyword%20:%20%22B2%22%20'),label:Silver),(input:(language:kuery,query:'qualis.keyword%20:%20%22C%2FNI%2FNP%22%20'),label:Bronze))),schema:group,type:filters)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:top,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:program_qualis_gsb,type:histogram))"
        },

        program_average_scores: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Citescore%20m%C3%A9dio',field:citescore),schema:metric,type:avg),(enabled:!t,id:'2',params:(filters:!" + this.urlProgramList + "),schema:segment,type:filters),(enabled:!t,id:'5',params:(customLabel:'Quartil%20citescore%20m%C3%A9dio',field:quartil_citescore),schema:metric,type:avg),(enabled:!t,id:'3',params:(customLabel:'Percentil%20m%C3%A9dio',field:percentile),schema:metric,type:avg),(enabled:!t,id:'4',params:(customLabel:'Quartil%20percentil%20m%C3%A9dio',field:quartil_percentile),schema:metric,type:avg)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!t),legendPosition:top,orderBucketsBySum:!f,row:!t,seriesParams:!((data:(id:'1',label:'Citescore%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'5',label:'Quartil%20citescore%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'3',label:'Percentil%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1),(data:(id:'4',label:'Quartil%20percentil%20m%C3%A9dio'),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:'Average%20citescore'),type:value))),title:'',type:histogram))"
        },

        program_qualis_estrato: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=pie&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:('0':%233F2B5B,'0.05':%23052B51,'0.2':%2358140C,'0.35':%23EA6460,'0.5':%23C15C17,'0.7':%23F2C96D,'0.8':%23CCA300,'0.9':%237EB26D,'1':%23508642))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'3',params:(filters:!" + this.urlProgramList + "),schema:split,type:filters),(enabled:!t,id:'2',params:(customLabel:'Qualis%20estrato',field:qualis_estrato,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:9),schema:segment,type:terms)),params:(addLegend:!t,addTooltip:!t,isDonut:!f,labels:(last_level:!t,show:!t,truncate:100,values:!t),legendPosition:top,row:!f,type:pie),title:'',type:pie))"    
        },
    }
}
</script>