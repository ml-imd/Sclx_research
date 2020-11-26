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
                                    @click="updateGraphs"
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
    </v-container>
</template>


<script>
export default {
    name: "Pesquisador",

    data: () => ({
        numberOfClusters: 2
    })
}
</script>