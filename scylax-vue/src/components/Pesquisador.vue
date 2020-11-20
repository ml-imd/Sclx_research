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
                            @click="number > 0 ? number-- : number"
                        >
                            <v-icon>mdi-minus</v-icon>
                        </v-btn>
                        <h1 class="mx-6">{{number}}</h1>
                        <v-btn 
                            icon
                            @click="number++"
                        >
                            <v-icon>mdi-plus</v-icon>
                        </v-btn>
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
        number: 0
    })
}
</script>