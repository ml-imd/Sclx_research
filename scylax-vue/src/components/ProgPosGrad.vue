<template>
    <v-container 
        fluid
        class="pa-6"
    >
        <v-row>
            <v-col class="d-flex justify-center">
                <v-card 
                    width="50%" 
                    color="#58A4B0"
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
                        <v-btn 
                            icon
                            @click="updateGraphs"
                        >
                            <v-icon>mdi-refresh</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card v-if="canRender" width="100%">
                    <v-container>
                        <v-row>
                            <v-col>
                                <iframe :src="graph1" height="500" width="100%"></iframe>
                            </v-col>
                            <v-col>
                                <iframe :src="graph2" height="500" width="100%"></iframe>
                            </v-col>
                        </v-row>
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
        numberOfClusters: 2,
        canRender: false,
        clusterUrlId: "",
        clusterUrlIdList : {
            2 : "cluster_k2",
            3 : "cluster_k3",
            4 : "cluster_k4",
            5 : "cluster_k5"
        }
    }),

    methods: {
        updateGraphs: function(){
            this.canRender = true;
            this.clusterUrlId = this.clusterUrlIdList[this.numberOfClusters];
        }
    },

    computed: {
        graph1: function(){
            return "http://localhost:5601/app/visualize#/edit/2dc5a180-2d12-11eb-8366-fb835f67c0ec?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23629E51,A2:%239AC48A,A3:%23E5AC0E,A4:%236ED0E0,B1:%23EF843C,B2:%23E24D42,B3:%23890F02,B4:%230A437C,C%2FNI%2FNP:%233F2B5B))),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Agrupamentos,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'3',params:(customLabel:Qualis,field:qualis.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:_key,otherBucket:!f,otherBucketLabel:Other,size:10),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,orderBucketsBySum:!f,seriesParams:!((data:(id:'1',label:Count),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:cluster_qualis,type:histogram))"
        },

        graph2: function(){
            return "http://localhost:5601/app/visualize#/edit/0562f7e0-2d14-11eb-8366-fb835f67c0ec?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(vis:(colors:(A1:%23629E51,A2:%239AC48A,A3:%23E5AC0E,A4:%236ED0E0,B1:%23EF843C,B2:%23E24D42,B3:%23890F02,B4:%230A437C,Bronze:%2399440A,C%2FNI%2FNP:%233F2B5B,Gold:%23E5AC0E,Silver:%23DEDAF7))),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(customLabel:Agrupamentos,field:" + this.clusterUrlId + ".keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:segment,type:terms),(enabled:!t,id:'3',params:(filters:!((input:(language:kuery,query:'qualis.keyword%20:%20%22A1%22%20or%20qualis.keyword%20:%20%22A2%22%20or%20qualis.keyword%20:%20%22A3%22%20or%20qualis.keyword%20:%20%22A4%22'),label:Gold),(input:(language:kuery,query:'qualis.keyword%20:%20%22B1%22%20or%20qualis.keyword%20:%20%22B2%22%20or%20qualis.keyword%20:%20%22B3%22%20or%20qualis.keyword%20:%20%22B4%22%20'),label:Silver),(input:(language:kuery,query:'qualis.keyword%20:%20%22C%2FNI%2FNP%22%20'),label:Bronze))),schema:group,type:filters)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,rotate:0,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,valueAxis:ValueAxis-1),labels:(show:!f),legendPosition:right,orderBucketsBySum:!f,seriesParams:!((data:(id:'1',label:Count),drawLinesBetweenPoints:!t,lineWidth:2,mode:normal,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Quantidade),type:value))),title:cluster_qualis_gsb,type:histogram))"
        }
    }
}
</script>