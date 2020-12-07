<template>
    <v-tabs
        v-model="currentTab"
        background-color="#424C63"
        dark
        grow
        height="35"
    >
        <v-tab>
            Produção
        </v-tab>
        <v-tab-item>
            <v-container
                fluid
                class="pa-6"
            >
                <v-row>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Total de publicações</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="total_prod" height="300" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white; font-size: 18px">Média de publi. por ano</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="average_prod_by_year" height="300" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Intervalo de atividade</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="activity_interval" height="300" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Citescore médio</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="average_citescore" height="300" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="7">
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Publicações por tipo por ano</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="total_by_year" height="500" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Publicações por tipo</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="total_by_type" height="500" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="5">
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Publicações por qualis</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="total_qualis" height="500" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Publicações por qualis por ano</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="qualis_by_year" height="500" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-tab-item>
        <v-tab>
            Colaboração
        </v-tab>
        <v-tab-item>
            <v-container>
                <v-row>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Colaborações internacionais por autor</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="n_colab_by_author" height="500" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card color="#424C63">
                            <v-row>
                                <h3 class="pl-5" style="color: white">Pesquisadores em colaborações internacionais</h3>
                                <v-spacer></v-spacer>
                                <Help />
                            </v-row>
                            <iframe :src="p_colab_by_author" height="500" width="100%" frameBorder="0"></iframe>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-tab-item>
    </v-tabs>
</template>

<script>
import Help from './Help.vue'

export default {
    name: "RedesAbaResumo",

    components: {
        Help,
    },

    props: {
        networkCoProductions: {
            type: Array
        },
        authorsProductions: {
            type: Object
        }
    },

    data: () => ({
        currentTab: '',
    }),

    methods: {
        arrayToUrl: function(array, field){
            var str = '(';

            for(var i = 0; i < array.length; i++){
                str += "(match_phrase:(" + field + ":'" + array[i] + "'))";
                if(i != array.length - 1 && array.length != 0){
                    str += ",";
                }
            }

            return str += ")"
        },
    },

    computed: {
        //Productions
        total_by_year: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Ano,drop_partials:!f,extended_bounds:(),field:ano,interval:y,min_doc_count:1,scaleMetricValues:!f,timeRange:(from:now-15m,to:now),useNormalizedEsInterval:!t),schema:segment,type:date_histogram),(enabled:!t,id:'3',params:(customLabel:Tipo,field:tipo_producao.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:top,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        },

        total_prod: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Produ%C3%A7%C3%B5es),schema:metric,type:count)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        average_prod_by_year: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customBucket:(enabled:!t,id:'1-bucket',params:(drop_partials:!f,extended_bounds:(),field:ano,interval:y,min_doc_count:1,scaleMetricValues:!f,useNormalizedEsInterval:!t),type:date_histogram),customLabel:Produções,customMetric:(enabled:!t,id:'1-metric',params:(),type:count)),schema:metric,type:avg_bucket)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        activity_interval: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'2',params:(customLabel:de,field:ano),schema:metric,type:min),(enabled:!t,id:'1',params:(customLabel:'%20at%C3%A9',field:ano),schema:metric,type:max)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:30,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        total_by_type: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=pie&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Tipo,field:tipo_producao.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTooltip:!t,isDonut:!f,labels:(last_level:!t,show:!t,truncate:100,values:!t),legendPosition:top,type:pie),title:'',type:pie))"
        },

        qualis_by_year: function(){
            return "http://localhost:5601/app/visualize#/edit/5e6dfe10-365c-11eb-99bf-7b67c063e059?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%239AC48A,A2:%23508642,A3:%23F2C96D,A4:%23E5AC0E,B1:%23C15C17,B2:%23EA6460,B3:%23BF1B00,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Ano,drop_partials:!f,extended_bounds:(),field:ano,interval:y,min_doc_count:1,scaleMetricValues:!f,timeRange:(from:now-15m,to:now),useNormalizedEsInterval:!t),schema:segment,type:date_histogram),(enabled:!t,id:'3',params:(customLabel:Qualis,field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:10),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:top,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:network_qualis_by_year,type:histogram))"
        },

        total_qualis: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=pie&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%237EB26D,A2:%23508642,A3:%23F2C96D,A4:%23E5AC0E,B1:%23F9934E,B2:%23EA6460,B3:%23BF1B00,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:10),schema:segment,type:terms)),params:(addLegend:!t,addTooltip:!t,isDonut:!f,labels:(last_level:!t,show:!t,truncate:100,values:!t),legendPosition:top,type:pie),title:'',type:pie))"
        },

        average_citescore: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(this.networkCoProductions, "producao.keyword") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Citescore%20m%C3%A9dio',field:citescore),schema:metric,type:avg)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        //Colaboration
        n_colab_by_author: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Autores,disabled:!f,index:ba783330-32ae-11eb-965f-ff26f33090ed,key:nome_normalizado,negate:!f,params:!('" + Object.keys(this.authorsProductions).join("','") + "'),type:phrases,value:'" + Object.keys(this.authorsProductions).toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(Object.keys(this.authorsProductions), "nome_normalizado") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade,field:n_colab_inter),schema:metric,type:max),(enabled:!t,id:'2',params:(customLabel:Autor,field:nome_normalizado,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        },

        p_colab_by_author: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ba783330-32ae-11eb-965f-ff26f33090ed&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Autores,disabled:!f,index:ba783330-32ae-11eb-965f-ff26f33090ed,key:nome_normalizado,negate:!f,params:!('" + Object.keys(this.authorsProductions).join("','") + "'),type:phrases,value:'" + Object.keys(this.authorsProductions).toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.arrayToUrl(Object.keys(this.authorsProductions), "nome_normalizado") + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade,field:p_colab_inter),schema:metric,type:max),(enabled:!t,id:'2',params:(customLabel:Autor,field:nome_normalizado,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        }
    }
}
</script>