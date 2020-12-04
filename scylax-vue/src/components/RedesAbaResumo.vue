<template>
    <v-container
        fluid
        class="pa-6"
    >
        <v-row>
            <v-col>
                <v-card color="#424C63">
                    <h3 class="pl-5" style="color: white">Total de publicações</h3>
                    <iframe :src="total_prod" height="200" width="100%" frameBorder="0"></iframe>
                </v-card>
            </v-col>
            <v-col>
                <v-card color="#424C63">
                    <h3 class="pl-5" style="color: white">Média de publicações por ano</h3>
                    <iframe :src="average_prod_by_year" height="200" width="100%" frameBorder="0"></iframe>
                </v-card>
            </v-col>
            <v-col>
                <v-card color="#424C63">
                    <h3 class="pl-5" style="color: white">Intervalo de atividade</h3>
                    <iframe :src="activity_interval" height="200" width="100%" frameBorder="0"></iframe>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card color="#424C63">
                    <h3 class="pl-5" style="color: white">Publicações por tipo por ano</h3>
                    <iframe :src="total_by_year" height="500" width="100%" frameBorder="0"></iframe>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card color="#424C63">
                    <h3 class="pl-5" style="color: white">Publicações por tipo</h3>
                    <iframe :src="total_by_type" height="500" width="100%" frameBorder="0"></iframe>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: "RedesAbaResumo",

    props: {
        networkCoProductions: {
            type: Array
        }
    },

    data: () => ({
    }),

    methods: {
        networkCoProductionsToUrl: function(){
            var networkCoProductionsUrl = '(';

            for(var i = 0; i < this.networkCoProductions.length; i++){
                networkCoProductionsUrl += "(match_phrase:(producao.keyword:'" + this.networkCoProductions[i] + "'))";
                if(i != this.networkCoProductions.length - 1 && this.networkCoProductions.length != 0){
                    networkCoProductionsUrl += ",";
                }
            }

            return networkCoProductionsUrl += ")"
        }
    },

    computed: {
        total_by_year: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.networkCoProductionsToUrl() + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Ano,drop_partials:!f,extended_bounds:(),field:ano,interval:y,min_doc_count:1,scaleMetricValues:!f,timeRange:(from:now-15m,to:now),useNormalizedEsInterval:!t),schema:segment,type:date_histogram),(enabled:!t,id:'3',params:(customLabel:Tipo,field:tipo_producao.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        },

        total_prod: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.networkCoProductionsToUrl() + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Produ%C3%A7%C3%B5es),schema:metric,type:count)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        average_prod_by_year: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.networkCoProductionsToUrl() + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customBucket:(enabled:!t,id:'1-bucket',params:(drop_partials:!f,extended_bounds:(),field:ano,interval:y,min_doc_count:1,scaleMetricValues:!f,useNormalizedEsInterval:!t),type:date_histogram),customLabel:Produções,customMetric:(enabled:!t,id:'1-metric',params:(),type:count)),schema:metric,type:avg_bucket)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:60,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        activity_interval: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=metric&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.networkCoProductionsToUrl() + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'2',params:(customLabel:de,field:ano),schema:metric,type:min),(enabled:!t,id:'1',params:(customLabel:'%20at%C3%A9',field:ano),schema:metric,type:max)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green%20to%20Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:30,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'',type:metric))"
        },

        total_by_type: function(){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=pie&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + this.networkCoProductions.join("','") + "'),type:phrases,value:'" + this.networkCoProductions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.networkCoProductionsToUrl() + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Tipo,field:tipo_producao.keyword,missingBucket:!f,missingBucketLabel:Missing,order:asc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms)),params:(addLegend:!t,addTooltip:!t,isDonut:!f,labels:(last_level:!t,show:!t,truncate:100,values:!t),legendPosition:right,type:pie),title:'',type:pie))"
        }
    }
}
</script>