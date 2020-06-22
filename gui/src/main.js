import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueMqtt from 'vue-mqtt';

Vue.use(VueMqtt, "ws://boethin.uberspace.de:46981", {clientId: 'mqtt-' + parseInt(Math.random() * 100000)});

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
