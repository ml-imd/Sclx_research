<template>
    <v-container fluid class="pa-6">
    </v-container>
</template>

<script>
export default {
    name: "RedesAbaProducoes",

    props: {
        networkCoProductions: {
            type: Array
        }
    },

    data: () => ({
        currentTab: ""
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

    computed:{

    }
}
</script>