<template>  
    <v-container
        fluid
        class="pa-16"
    >
        <v-row>
            <v-col cols="11">
                <v-text-field
                    v-model="searchedAuthor"
                    color="#58A4B0"
                    label="Pesquisador"
                    
                    prepend-inner-icon="mdi-account"
                ></v-text-field>
            </v-col>
            <v-col>
                <v-btn 
                    fab
                    color="#58A4B0"
                    dark
                    @click="addAuthor"
                >
                    <v-icon>mdi-plus</v-icon>
                </v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-card 
                    v-if="network.length > 0"
                    width="100%">
                    
                    <v-card-title primary-title>
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

                            <v-spacer></v-spacer>

                            <v-list-item-action>
                                <v-btn icon @click="removeAuthor(index)">
                                    <v-icon>mdi-delete</v-icon>
                                </v-btn>
                            </v-list-item-action>
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: "RedesDeColaboração",

    data: () => ({
        searchedAuthor: "",
        network: [],
    }),

    methods: {
        addAuthor: function(){
            if(this.searchedAuthor != ""){
                this.network.push(this.searchedAuthor);
            }
        },

        removeAuthor: function(index){
            this.network.splice(index, 1);
        }
    }
}
</script>