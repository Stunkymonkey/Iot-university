<template>
  <v-app dark>
    <v-app-bar app dark>
      <v-btn color="accent" @click="SubscribeMqtt">Subscribe</v-btn>
    </v-app-bar>

    <v-main dark>
      <Crows />
    </v-main>
  </v-app>
</template>

<script>
import Crows from "./components/Crows";

export default {
  name: "App",

  components: {
    Crows
  },
  methods: {
    SubscribeMqtt() {
      this.$mqtt.subscribe("iot/#");
    }
  },

  data: () => ({
    //
  })
};
</script>
