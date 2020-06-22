<template>
  <v-app dark>
    <v-app-bar app dark class="mb-0">
      <v-toolbar-title>
        <div class="crowstitle">CROWS</div>
      </v-toolbar-title>
    </v-app-bar>
    <v-main dark>
      <v-container dark justify-space-between align-content-space-between>
        <v-row no-gutter>
          <v-col md="6" cols="12" class="mx-auto" style="flex-direction:column">
            <h1>Sensors</h1>
            <v-card flat class="mx-auto mb-6" fluid outlined>
              <v-list-item>
                <v-list-item-content>
                  <div class="overline mb-1">Main Section</div>
                  <v-subheader class="mt-0 mb-0 pt-0 pb-0">Temperature</v-subheader>
                  <v-card-text class="mt-0 mb-0 pt-0 pb-0">
                    <v-slider
                      dense
                      height="2"
                      color="accent"
                      min="0"
                      max="30"
                      class="temperature"
                      v-model="section0.temperature"
                    >
                      <template v-slot:append>
                        <div class="sensorlabel">{{section0.temperature}}</div>
                      </template>
                    </v-slider>
                  </v-card-text>

                  <v-subheader class="mt-0 mb-0 pt-0 pb-0">Humidity</v-subheader>
                  <v-card-text class="mt-0 mb-0 pt-0 pb-0">
                    <v-slider
                      dense
                      height="2"
                      color="accent"
                      min="0"
                      max="100"
                      class="humidity"
                      v-model="section0.humidity"
                    >
                      <template v-slot:append>
                        <div class="sensorlabel">{{section0.humidity}}</div>
                      </template>
                    </v-slider>
                  </v-card-text>

                  <v-list-item>
                    <v-btn @click="personCount('in', 'section0')" color="success">Person Entering</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn @click="personCount('out', 'section0')" color="error">Person Leaving</v-btn>
                  </v-list-item>
                </v-list-item-content>
              </v-list-item>
            </v-card>

            <v-card class="mx-auto mb-6" fluid outlined>
              <v-list-item>
                <v-list-item-content>
                  <div class="overline mb-1">Section 1</div>
                  <v-subheader class="mt-0 mb-0 pt-0 pb-0">Shelf</v-subheader>
                  <v-card-text class="mt-0 mb-0 pt-0 pb-0">
                    <v-slider
                      dense
                      height="2"
                      color="accent"
                      min="0"
                      max="6"
                      step="1"
                      v-model="section1.shelf"
                    >
                      <template v-slot:append>
                        <div class="sensorlabel">{{section1.shelf}}</div>
                      </template>
                    </v-slider>
                  </v-card-text>

                  <v-list-item>
                    <v-btn @click="personCount('in', 'section1')" color="success">Person Entering</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn @click="personCount('out', 'section1')" color="error">Person Leaving</v-btn>
                  </v-list-item>
                </v-list-item-content>
              </v-list-item>
            </v-card>

            <v-card class="mx-auto mb-6" fluid outlined>
              <v-list-item>
                <v-list-item-content>
                  <div class="overline mb-4">Section 2</div>
                  <v-subheader class="mt-0 mb-0 pt-0 pb-0">Shelf</v-subheader>
                  <v-card-text class="mt-0 mb-0 pt-0 pb-0">
                    <v-slider
                      dense
                      height="2"
                      color="accent"
                      min="0"
                      max="6"
                      step="1"
                      class="shelf"
                      v-model="section2.shelf"
                    >
                      <template v-slot:append>
                        <div class="sensorlabel">{{section2.shelf}}</div>
                      </template>
                    </v-slider>
                  </v-card-text>

                  <v-list-item>
                    <v-btn @click="personCount('in', 'section2')" color="success">Person Entering</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn @click="personCount('out', 'section2')" color="error">Person Leaving</v-btn>
                  </v-list-item>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
          <v-col class="mx-auto" md="6" cols="12">
            <h1>Actuators</h1>

            <v-card class="mx-auto mb-6" fluid outlined>
              <v-list-item>
                <v-list-item-content>
                  <div class="overline mb-4">Main Section</div>
                  <v-list-item>Gate: {{section0.gate}}</v-list-item>
                  <v-list-item>Ventilator: {{section0.ventilator}}</v-list-item>
                </v-list-item-content>
              </v-list-item>
            </v-card>

            <v-card class="mx-auto mb-6" fluid outlined>
              <v-list-item>
                <v-list-item-content>
                  <div class="overline mb-4">Section 1</div>
                  <v-list-item>LED: {{section1.led}}</v-list-item>
                  <v-list-item>Gate: {{section1.gate}}</v-list-item>
                  <v-list-item>Refill Shelf: {{section1.refill_shelf}}</v-list-item>
                </v-list-item-content>
              </v-list-item>
            </v-card>

            <v-card class="mx-auto mb-6" fluid outlined>
              <v-list-item>
                <v-list-item-content>
                  <div class="overline mb-4">Section 2</div>
                  <v-list-item>LED: {{section2.led}}</v-list-item>
                  <v-list-item>Gate: {{section2.gate}}</v-list-item>
                  <v-list-item>Refill Shelf: {{section2.refill_shelf}}</v-list-item>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <v-footer class="mt-5" fixed>
      <div class="footer">Felix Bühler, Jamie Ullerich, Jan Leusmann</div>
      <v-spacer></v-spacer>
      <div class="footer">Smart Cities and Internet of Things Project Summerterm 2020</div>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      section0: {
        temperature: 20,
        humidity: 40,
        ventilator: 0,
        gate: false
      },
      section1: {
        shelf: 5,
        led: 0,
        refill_shelf: false,
        gate: false
      },
      section2: {
        shelf: 5,
        led: 0,
        refill_shelf: false,
        gate: false
      }
    };
  },
  mounted() {
    this.$mqtt.subscribe("iot/#");
  },
  mqtt: {
    "iot/actuators/section1/led"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section1.led = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section2/led"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section2.led = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section0/ventilator"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section0.ventilator = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section1/refill_shelf"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section1.refill_shelf = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section2/refill_shelf"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section2.refill_shelf = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section0/gate"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section0.gate = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section1/gate"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section1.gate = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section2/gate"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section2.gate = String.fromCharCode.apply(null, data);
    }
  },
  watch: {
    "section0.temperature": function() {
      console.log("temp: ", this.section0.temperature);
      this.PublishMqtt(
        "iot/sensors/section0/temperature",
        "" + this.section0.temperature
      );
    },
    "section0.humidity": function() {
      console.log("humid: ", this.section0.humidity);
      this.PublishMqtt(
        "iot/sensors/section0/humidty",
        "" + this.section0.humidity
      );
    },
    "section1.shelf": function() {
      console.log("s1 shelf: ", this.section1.shelf);
      this.PublishMqtt("iot/sensors/section1/shelf", "" + this.section1.shelf);
    },
    "section2.shelf": function() {
      console.log("s2 shelf: ", this.section2.shelf);
      this.PublishMqtt("iot/sensors/section2/shelf", "" + this.section2.shelf);
    }
  },
  methods: {
    PublishMqtt(path, msg) {
      this.$mqtt.publish(path, msg);
    },
    personCount(where, section) {
      console.log(where, section, "1");
      this.PublishMqtt("iot/sensors/" + section + "/button/" + where, "1");
      setTimeout(() => {
        console.log(where, section, "0");
        this.PublishMqtt("iot/sensors/" + section + "/button/" + where, "0");
      }, 100);
    },
    SubscribeMqtt() {
      console.log("subsribed");
      this.$mqtt.subscribe("iot/#");
      console.log(this.$mqtt);
    }
  },
  components: {}
};
</script>

<style>
.crowstitle {
  font-weight: 500;
}
.footer {
  font-size: 13px;
  font-weight: 400;
}
</style>