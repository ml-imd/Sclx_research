<template>
    <v-container
        fluid
        class="pa-6"
    >
        <v-row class="mb-3" v-for="(value, key) in subNetworkProductions" :key="key">
            <v-card width="100%">
                <v-card-title>
                    <h3 style="color: #424C63">Sub-rede: {{ key.split(",").join(" + ") }}</h3>
                </v-card-title>

                <v-container grid-list-xs>
                    <v-row>
                        <v-col>
                            <v-card color="#424C63">
                                <v-row>
                                    <h3 class="pl-5" style="color: white">Publicações por qualis</h3>
                                    <v-spacer></v-spacer>
                                    <Help />
                                </v-row>
                                <iframe :src="qualis_by_year(value)" height="300" width="100%" frameBorder="0"></iframe>
                            </v-card>
                        </v-col>
                        <v-col>
                            <v-card color="#424C63">
                                <v-row>
                                    <h3 class="pl-5" style="color: white">Citescore das produções</h3>
                                    <v-spacer></v-spacer>
                                    <Help />
                                </v-row>
                                <iframe :src="citescore_distribution(value)" height="300" width="100%" frameBorder="0"></iframe>
                            </v-card>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col>    
                            <v-card color="#424C63">
                                <v-row>
                                    <h3 class="pl-5" style="color: white">Produções por pesquisador</h3>
                                    <v-spacer></v-spacer>
                                    <Help />
                                </v-row>
                                <iframe :src="heatmap_productions(key)" height="300" width="100%" frameBorder="0"></iframe>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>   
            </v-card>
        </v-row>
    </v-container>
</template>

<script>
import Help from './Help.vue'

export default {
    name: "RedesAbaDetalhes",

    components: {
        Help,
    },

    props: {
        subNetworkProductions: {
            type: Object,
        },
        authorsProductions: {
            type: Object,
        }
    },

    data: () => ({
        
    }),

    methods: {
        networkCoProductionsToUrl: function(productions){
            var networkCoProductionsUrl = '(';

            for(var i = 0; i < productions.length; i++){
                networkCoProductionsUrl += "(match_phrase:(producao.keyword:'" + productions[i] + "'))";
                if(i != productions.length - 1 && productions.length != 0){
                    networkCoProductionsUrl += ",";
                }
            }

            return networkCoProductionsUrl += ")"
        },

        networkAuthorsProductionsToUrl: function(authors){
            authors = authors.split(',');
            var str = '';
            for(let i = 0; i < authors.length; i++){
                str += "(input:(language:kuery,query:'";
                for(let j = 0; j < this.authorsProductions[authors[i]].length; j++){
                    str += "producao.keyword:" + this.authorsProductions[authors[i]][j];
                    if(j != this.authorsProductions[authors[i]].length - 1 && this.authorsProductions[authors[i]].length != 0){
                        str += "%20or%20"
                    }
                }
                if(i != authors.length - 1 && authors.length != 0){
                    str += "'),label:'" + authors[i] + "'),";
                } else {
                    str += "'),label:'" + authors[i] + "')";
                }
            }
            return str += ")"
        },
    
        qualis_by_year: function(productions){
            return "http://localhost:5601/app/visualize#/edit/4a25d070-365e-11eb-99bf-7b67c063e059?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + productions.join("','") + "'),type:phrases,value:'" + productions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.networkCoProductionsToUrl(productions) + ")))),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%237EB26D,A2:%23508642,A3:%23F2C96D,A4:%23E5AC0E,B1:%23F9934E,B2:%23EA6460,B3:%23BF1B00,B4:%23052B51,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:10),schema:segment,type:terms)),params:(addLegend:!t,addTooltip:!t,isDonut:!f,labels:(last_level:!t,show:!t,truncate:100,values:!t),legendPosition:top,type:pie),title:network_total_qualis,type:pie))"
        },

        citescore_distribution: function(productions){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=pie&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(('$state':(store:appState),meta:(alias:Produções,disabled:!f,index:ed2eeb90-3590-11eb-8ebb-8dc5ca511f23,key:producao.keyword,negate:!f,params:!('" + productions.join("','") + "'),type:phrases,value:'" + productions.toString() + "'),query:(bool:(minimum_should_match:1,should:!" + this.networkCoProductionsToUrl(productions) + ")))),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(filters:!((input:(language:kuery,query:'citescore%20%3C%3D%2018'),label:'Relev%C3%A2ncia%20baixa'),(input:(language:kuery,query:'citescore%20%3E%2018%20and%20citescore%20%3C%3D%2036'),label:'Relev%C3%A2ncia%20m%C3%A9dia'),(input:(language:kuery,query:'citescore%20%3E%2036'),label:'Relev%C3%A2ncia%20alta'))),schema:segment,type:filters)),params:(addLegend:!t,addTooltip:!t,isDonut:!f,labels:(last_level:!t,show:!f,truncate:100,values:!t),legendPosition:top,type:pie),title:'',type:pie))"
        },

        heatmap_productions: function(authors){
            return "http://localhost:5601/app/visualize#/create?embed=true&type=histogram&indexPattern=0922d430-2ec3-11eb-a9e4-f3fe9303f5c9&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:Quantidade),schema:metric,type:count),(enabled:!t,id:'2',params:(filters:!(" + this.networkAuthorsProductionsToUrl(authors) + "),schema:segment,type:filters)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!t),legendPosition:top,seriesParams:!((data:(id:'1',label:Quantidade),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:'',type:histogram))"
        }
    },
}
</script>