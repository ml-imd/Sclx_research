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
                            @click="numberOfClusters < 5 ? numberOfClusters++ : numberOfClusters"
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
                                    icon
                                    @click="updateGroupGraphs"
                                >
                                    <v-icon>mdi-refresh</v-icon>
                                </v-btn>
                            </template>
                            <span>Atualizar grupos</span>
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
                                <h3 class="pl-5">Programas por grupo</h3>
                                <iframe :src="prog_per_cluster" height="300" width="100%" frameBorder="0"></iframe>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <h3 class="pl-5">Publicações por grupo por ano</h3>
                                <iframe :src="pub_by_year" height="500" width="100%" frameBorder="0"></iframe>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <h3 class="pl-5">Citescore médio por grupo</h3>
                                <iframe :src="citescore_average" height="500" width="100%" frameBorder="0"></iframe>
                            </v-col>
                            <v-col>
                                <h3 class="pl-5">Quartil citescore médio por grupo</h3>
                                <iframe :src="quartil_citescore_average" height="500" width="100%" frameBorder="0"></iframe>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <h3 class="pl-5">Percentil médio por grupo</h3>
                                <iframe :src="percentile_average" height="500" width="100%" frameBorder="0"></iframe>
                            </v-col>
                            <v-col>
                                <h3 class="pl-5">Quartil percentil médio por grupo</h3>
                                <iframe :src="quartil_percentile_average" height="500" width="100%" frameBorder="0"></iframe>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <h3 class="pl-5">Publicações por grupo por qualis</h3>
                                <iframe :src="cluster_qualis" height="500" width="100%" frameBorder="0"></iframe>
                            </v-col>
                            <v-col>
                                <h3 class="pl-5">Qualidade de publicações por grupo</h3>
                                <iframe :src="cluster_qualis_gsb" height="500" width="100%" frameBorder="0"></iframe>
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
                                        :disabled="isDisabled"
                                    >
                                        Analisar Programa 
                                        <v-icon >mdi-menu-right</v-icon>
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-actions>
                    <v-container>
                        <div v-if="canRenderProgram">
                            <v-row>
                                <v-col class="justify-end">
                                    <v-btn 
                                        icon
                                        @click="canRenderProgram = false"
                                    >
                                        <v-icon>mdi-close</v-icon>
                                    </v-btn>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <iframe :src="program_scores" height="300" width="100%" frameBorder="0"></iframe>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <iframe :src="program_citescore" height="300" width="100%" frameBorder="0"></iframe>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <h3 class="pl-5">Publicações por qualis por programa</h3>
                                    <iframe :src="program_qualis" height="500" width="100%" frameBorder="0"></iframe>
                                </v-col>
                                <v-col>
                                    <h3 class="pl-5">Qualidade de publicações por programa</h3>
                                    <iframe :src="program_qualis_gsb" height="500" width="100%" frameBorder="0"></iframe>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <h3 class="pl-5">Distribuição de qualis estrato em {{mainProgram}}</h3>
                                    <iframe :src="program_qualis_estrato" height="500" width="100%" frameBorder="0"></iframe>
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
export default {
    name: "ProgPosGrad",

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
        programList: ["ADMINISTRAÇÃO","ANTROPOLOGIA SOCIAL","ARQUITETURA  E URBANISMO","ARQUITETURA. PROJETO E MEIO AMBIENTE","ARTES CÊNICAS","BIOINFORMÁTICA","Biologia Estrutural e Funcional","Biologia Parasitária","Bioquímica e Biologia Molecular","BIOTECNOLOGIA _ Rede RENORBIO","CIÊNCIA E ENGENHARIA DE MATERIAIS","CIÊNCIA E ENGENHARIA DE PETRÓLEO","CIÊNCIA. TECNOLOGIA E INOVAÇÃO","CIÊNCIAS Climáticas","CIÊNCIAS CONTÁBEIS","CIÊNCIAS DA REABILITAÇÃO","CIÊNCIAS DA SAÚDE","CIÊNCIAS FARMACÊUTICAS","CIÊNCIAS Florestais","CIÊNCIAS ODONTOLÓGICAS","CIÊNCIAS SOCIAIS","DEMOGRAFIA","DESENVOLVIMENTO E MEIO AMBIENTE","DESENVOLVIMENTO E MEIO AMBIENTE UFPI_UFRN_FUFSE_UESC_UFPB/JP","Design","DIREITO","ECOLOGIA","ECONOMIA","EDUCAÇÃO","EDUCAÇÃO FÍSICA","Energia ELÉTRICA","ENFERMAGEM","ENGENHARIA DE PRODUÇÃO","ENGENHARIA ELÉTRICA","ENGENHARIA MECÂNICA","Engenharia Mecatrônica","ENGENHARIA QUÍMICA","ENGENHARIA SANITÁRIA E AMBIENTAL", "ENGENHARIA TÊXTIL","ENSINO DE CIÊNCIAS E MATEMÁTICA","ENSINO DE CIÊNCIAS NATURAIS  E MATEMÁTICA","ENSINO NA SAÚDE","ESTUDOS DA LINGUAGEM","ESTUDOS DA MÍDIA","ESTUDOS URBANOS E REGIONAIS","FILOSOFIA","FÍSICA","FISIOTERAPIA","GEODINÂMICA E GEOFÍSICA","GEOGRAFIA","Gestão DA Informação E DO CONHECIMENTO","Gestão da Qualidade em Serviços de SAÚDE","Gestão de Processos Institucionais","Gestão E INOVAÇÃO EM SAÚDE","Gestão Pública","HISTÓRIA","INOVAÇÃO EM TECNOLOGIAS EDUCACIONAIS","LETRAS","MATEMÁTICA APLICADA E ESTATISTICA","Música","NEUROCIÊNCIAS","Nutrição","PRODUÇÃO ANIMAL","PSICOBIOLOGIA","PSICOLOGIA","QUÍMICA","SAÚDE Coletiva","SAÚDE COLETIVA","SAÚDE E SOCIEDADE","SERVIÇO SOCIAL","SISTEMAS E COMPUTAÇÃO","Sistemática e Evolução","Tecnologia da Informação","TURISMO"]
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
            this.canRenderProgram = true;
            
            this.mainProgramCluster = this.groupSelect;
            this.mainProgram = this.program;

            this.urlProgramList = "(";
            this.urlProgramList += "(input:(language:kuery,query:'programas_nomes.keyword:" + this.mainProgram + "'),label:'" + this.mainProgram + "')";
            this.urlProgramList += ")";
        }
    },

    computed: {

        //PROGRAMAS SECAO UM
        cluster_qualis: function(){
            return "http://localhost:5601/app/visualize#/edit/88f530d0-2ec4-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'3',params:(customLabel:Qualis,field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:11),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:cluster_qualis,type:histogram))"
        },

        cluster_qualis_gsb: function(){
            return "http://localhost:5601/app/visualize#/edit/3a2a3670-2f56-11eb-b8d7-2bd9025fb19b?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,Bronze:%2399440A,C%2FNI%2FNP:%233F2B5B,Gold:%23E5AC0E,Silver:%23DEDAF7))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Programa,field:" + this.clusterUrlId + ".keyword,include:'',missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'3',params:(filters:!((input:(language:kuery,query:'qualis.keyword%20:%20%22A1%22%20or%20qualis.keyword%20%0A:%20%22A2%22%20or%20qualis.keyword%20:%20%22A3%22%20or%20qualis.keyword%20:%20%22A4%22'),label:Gold),(input:(language:kuery,query:'qualis.keyword%20:%20%22B1%22%20or%20qualis.keyword%20:%20%22B3%22%20or%20qualis.keyword%20:%20%22B4%22%20or%20qualis.keyword%20:%20%22B2%22%20'),label:Silver),(input:(language:kuery,query:'qualis.keyword%20:%20%22C%2FNI%2FNP%22%20'),label:Bronze))),schema:group,type:filters)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:cluster_qualis_gsb,type:histogram))"
        },

        citescore_average: function(){
            return "http://localhost:5601/app/visualize#/edit/1eca5170-2ec6-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Citescore',field:citescore),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:average_citescore_metric,type:metric))"
        },

        quartil_citescore_average: function(){
            return "http://localhost:5601/app/visualize#/edit/1eca5170-2ec6-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Quartil%20citescore',field:quartil_citescore),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:average_citescore_metric,type:metric))"
        },

        percentile_average: function(){
            return "http://localhost:5601/app/visualize#/edit/1eca5170-2ec6-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Percentil,field:percentile),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:average_citescore_metric,type:metric))"
        },

        quartil_percentile_average: function(){
            return "http://localhost:5601/app/visualize#/edit/1eca5170-2ec6-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Quartil%20percentil',field:quartil_percentile),schema:metric,type:avg),(enabled:!t,id:'2',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:average_citescore_metric,type:metric))"
        },

        pub_by_year: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=line&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(cluster1:%23447EBC))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Ano,field:ano.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:100),schema:segment,type:terms),(enabled:!t,id:'3',params:(customLabel:Grupo,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(),legendPosition:right,orderBucketsBySum:!f,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,interpolate:linear,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:line,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:line,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(defaultYExtents:!f,mode:normal,setYExtents:!f,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:line))"
        },

        //PROGRAMAS SECAO DOIS
        program_qualis: function(){
            return "http://localhost:5601/app/visualize#/edit/f394bf70-2ecc-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(filters:!" + this.urlProgramList + "),schema:segment,type:filters),(enabled:!t,id:'3',params:(customLabel:Qualis,field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:11),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:program_qualis,type:histogram))"
        },

        program_qualis_gsb: function(){
            return "http://localhost:5601/app/visualize#/edit/c78238c0-2ec4-11eb-a9e4-f3fe9303f5c9?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23508642,A2:%239AC48A,A3:%23CCA300,A4:%23F2C96D,B1:%23E0752D,B2:%23E24D42,B3:%23890F02,B4:%230A437C,Bronze:%2399440A,C%2FNI%2FNP:%233F2B5B,Gold:%23E5AC0E,Silver:%23DEDAF7))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(filters:!" + this.urlProgramList + "),schema:segment,type:filters),(enabled:!t,id:'3',params:(filters:!((input:(language:kuery,query:'qualis.keyword%20:%20%22A1%22%20or%20qualis.keyword%20%0A:%20%22A2%22%20or%20qualis.keyword%20:%20%22A3%22%20or%20qualis.keyword%20:%20%22A4%22'),label:Gold),(input:(language:kuery,query:'qualis.keyword%20:%20%22B1%22%20or%20qualis.keyword%20:%20%22B3%22%20or%20qualis.keyword%20:%20%22B4%22%20or%20qualis.keyword%20:%20%22B2%22%20'),label:Silver),(input:(language:kuery,query:'qualis.keyword%20:%20%22C%2FNI%2FNP%22%20'),label:Bronze))),schema:group,type:filters)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:program_qualis_gsb,type:histogram))"
        },

        prog_per_cluster: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Programas,field:programas.keyword),schema:metric,type:cardinality),(enabled:!t,id:'2',params:(field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        program_citescore: function(){
            return "http://localhost:5601/app/visualize#/edit/c2a69990-31b2-11eb-8045-b53bd470100c?embed=true&type=metric&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'3',params:(customLabel:'Citescore%20m%C3%ADnimo',field:citescore),schema:metric,type:min),(enabled:!t,id:'1',params:(customLabel:'Citescore%20m%C3%A9dio',field:citescore),schema:metric,type:avg),(enabled:!t,id:'2',params:(filters:!" + this.urlProgramList + "),schema:group,type:filters),(enabled:!t,id:'4',params:(customLabel:'Citescore%20m%C3%A1ximo',field:citescore),schema:metric,type:max)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:program_citescore_metric,type:metric))"
        },
        
        program_scores: function(){
            return "http://localhost:5601/app/visualize#/edit/c2a69990-31b2-11eb-8045-b53bd470100c?embed=true&type=metric&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'3',params:(customLabel:'Quartil%20citescore%20m%C3%A9dio',field:quartil_citescore),schema:metric,type:avg),(enabled:!t,id:'4',params:(customLabel:'Percentil%20m%C3%A9dio',field:percentile),schema:metric,type:avg),(enabled:!t,id:'1',params:(customLabel:'Quartil%20percentil%20m%C3%A9dio',field:quartil_percentile),schema:metric,type:avg),(enabled:!t,id:'2',params:(filters:!((input:(language:kuery,query:'programas_nomes.keyword%20:" + this.mainProgram + "'),label:'" + this.mainProgram + "'))),schema:group,type:filters)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:program_citescore_metric,type:metric))"
        },

        program_qualis_estrato: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=pie&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:" + this.clusterUrlId + ".keyword,negate:!f,params:(query:" + this.mainProgramCluster + "),type:phrase),query:(match_phrase:(" + this.clusterUrlId + ".keyword:" + this.mainProgramCluster + "))),('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'0922d430-2ec3-11eb-a9e4-f3fe9303f5c9',key:programas_nomes.keyword,negate:!f,params:(query:'" + this.mainProgram + "'),type:phrase),query:(match_phrase:(programas_nomes.keyword:'" + this.mainProgram + "')))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:('0':%233F2B5B,'0.05':%230A437C,'0.2':%23890F02,'0.35':%23EA6460,'0.5':%23F9934E,'0.7':%23F2C96D,'0.8':%23CCA300,'0.9':%239AC48A,'1':%23508642))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'3',params:(field:qualis_estrato,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:10),schema:segment,type:terms)),params:(addLegend:!t,addTooltip:!t,isDonut:!f,labels:(last_level:!t,show:!f,truncate:100,values:!t),legendPosition:right,type:pie),title:'',type:pie))"
        },

        isDisabled: function(){
            var disabled = false;
            if(this.program == "" || this.groupSelect == ""){
                disabled = true;
            } else if(this.canRenderProgram){
                disabled = true;
            }

            return disabled;
        }
    }
}
</script>