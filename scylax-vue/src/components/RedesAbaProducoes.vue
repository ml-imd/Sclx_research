<template>
    <v-tabs
        v-model="currentTab"
        background-color="#58A4B0"
        dark
        grow
        height="30px"
    >
        <v-tab>
            Sumário
        </v-tab>
        <v-tab>
            Detalhes
        </v-tab>
    </v-tabs>
</template>

<script>
export default {
    name: "RedesAbaProducoes",

    data: () => ({
        currentTab: ""
    })
}
</script>