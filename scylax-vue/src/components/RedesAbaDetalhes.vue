<template>
    <v-container
        fluid
        class="pa-6"
    >
        <v-row class="mb-3" v-for="(value, key) in subNetworkProductions" :key="key">
            <v-card width="100%">
                <v-card-title>
                    <h3 style="color: #424C63">{{ key.split(",").join(" + ") }}</h3>
                </v-card-title>

                <v-container grid-list-xs>
                    <v-row>
                        <v-col>
                            <v-card color="#424C63">
                                <h3 class="pl-5" style="color: white">Publicações por qualis</h3>
                                <iframe :src="qualis_by_year(value)" height="300" width="100%" frameBorder="0"></iframe>
                            </v-card>  
                            <v-card color="#424C63" class="mt-3">
                                <h3 class="pl-5" style="color: white">Citescore das produções</h3>
                                <iframe :src="citescore_distribution(value)" height="300" width="100%" frameBorder="0"></iframe>
                            </v-card>
                        </v-col>
                        <v-col>    
                            <v-card color="#424C63">
                                <h3 class="pl-5" style="color: white">Produções por pesquisador</h3>
                                <iframe :src="heatmap_productions(key)" height="647" width="100%" frameBorder="0"></iframe>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>   
            </v-card>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: "RedesAbaDetalhes",

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
            //(input:(language:kuery,query:'producao.keyword%20:%2210001926%22%20or%20producao.keyword%20:%2210001927%22%20'),label:Autor),(input:(language:kuery,query:'producao.keyword%20:%20%2210001928%22%20'),label:Autor2))
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
            return "http://localhost:5601/app/visualize#/edit/ba8784d0-3735-11eb-8554-d764e573d442?embed=true&type=heatmap&indexPattern=ed2eeb90-3590-11eb-8ebb-8dc5ca511f23&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(),defaultColors:('0%20-%200.2':'rgb(247,251,255)','0.2%20-%200.4':'rgb(208,225,242)','0.4%20-%200.6':'rgb(148,196,223)','0.6%20-%200.8':'rgb(74,152,201)','0.8%20-%201':'rgb(23,100,171)'))),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'%20'),schema:metric,type:count),(enabled:!t,id:'2',params:(filters:!(" + this.networkAuthorsProductionsToUrl(authors) + "),schema:segment,type:filters)),params:(addLegend:!t,addTooltip:!t,colorSchema:'Yellow%20to%20Red',colorsNumber:5,colorsRange:!((from:0,to:100)),enableHover:!f,invertColors:!f,legendPosition:top,percentageMode:!f,setColorRange:!f,times:!(),type:heatmap,valueAxes:!((id:ValueAxis-1,labels:(color:black,overwriteColor:!f,rotate:0,show:!t),scale:(defaultYExtents:!f,type:linear),show:!f,type:value))),title:network_heatmap_productions,type:heatmap))"
        }
    },
}
</script>