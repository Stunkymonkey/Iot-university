<template>
  <v-container dark justify-space-between align-content-space-between>
    <v-row no-gutter>
      <v-col md="6" cols="12">
        <h1>Sensors</h1>
        <v-card class="mx-auto" fluid outlined>
          <v-list-item>
            <v-list-item-content>
              <div class="overline mb-4">Main Section</div>
              <v-list-item>
                <v-slider
                  label="temperature"
                  color="accent"
                  min="0"
                  max="30"
                  class="temperature"
                  v-model="section0.temperature"
                ></v-slider>
                {{section0.temperature}}
              </v-list-item>
              <v-list-item>
                <v-slider
                  label="humidity"
                  color="accent"
                  min="0"
                  max="100"
                  class="humidity"
                  v-model="section0.humidity"
                ></v-slider>
                {{section0.humidity}}
              </v-list-item>
              <v-list-item>
                <v-btn @click="personCount('in', 'section0')" color="success">Person Entering</v-btn>
                <v-spacer></v-spacer>
                <v-btn @click="personCount('out', 'section0')" color="error">Person Leaving</v-btn>
              </v-list-item>
            </v-list-item-content>
          </v-list-item>
        </v-card>
        <v-card class="mx-auto" fluid outlined>
          <v-list-item>
            <v-list-item-content>
              <div class="overline mb-4">Section 1</div>
              <v-list-item>
                <v-slider
                  label="Shelf"
                  color="accent"
                  min="0"
                  max="6"
                  step="1"
                  class="shelf"
                  v-model="section1.shelf"
                ></v-slider>
                {{section1.shelf}}
              </v-list-item>

              <v-list-item>
                <v-btn @click="personCount('in', 'section1')" color="success">Person Entering</v-btn>
                <v-spacer></v-spacer>
                <v-btn @click="personCount('out', 'section1')" color="error">Person Leaving</v-btn>
              </v-list-item>
            </v-list-item-content>
          </v-list-item>
        </v-card>
        <v-card class="mx-auto" fluid outlined>
          <v-list-item>
            <v-list-item-content>
              <div class="overline mb-4">Section 2</div>
              <v-list-item>
                <v-slider
                  label="Shelf"
                  color="accent"
                  min="0"
                  max="6"
                  step="1"
                  class="shelf"
                  v-model="section2.shelf"
                ></v-slider>
                {{section2.shelf}}
              </v-list-item>

              <v-list-item>
                <v-btn @click="personCount('in', 'section2')" color="success">Person Entering</v-btn>
                <v-spacer></v-spacer>
                <v-btn @click="personCount('out', 'section2')" color="error">Person Leaving</v-btn>
              </v-list-item>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col md="6" cols="12">
        <h1>Actuators</h1>
        <v-card class="mx-auto" fluid outlined>
          <v-list-item>
            <v-list-item-content>
              <div class="overline mb-4">Main Section</div>
            </v-list-item-content>
          </v-list-item>
        </v-card>
        <v-card class="mx-auto" fluid outlined>
          <v-list-item>
            <v-list-item-content>
              <div class="overline mb-4">Section 1</div>
              LED: {{section1.led}}
            </v-list-item-content>
          </v-list-item>
        </v-card>
        <v-card class="mx-auto" fluid outlined>
          <v-list-item>
            <v-list-item-content>
              <div class="overline mb-4">Section 2</div>
              LED: {{section2.led}}
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
        gate: 0
      },
      section1: {
        shelf: 5,
        led: 0
      },
      section2: {
        shelf: 5,
        led: 0
      }
    };
  },
  mounted() {
    this.$mqtt.subscribe("iot/#");
  },
  mqtt: {
    "iot/sensors/section1/led"(data, topic) {
      console.log(topic);
      this.section1.led = String.fromCharCode.apply(null, data);
    },
    "iot/sensors/section2/led"(data, topic) {
      this.section2.led = String.fromCharCode.apply(null, data);
      console.log(String.fromCharCode.apply(null, data), topic);
    }
  },
  watch: {
    "section0.temperature": function() {
      console.log("temp: ", this.section0.temperature);
      this.PublishMqtt(
        "iot/sensors/section0/temperature",
        this.section0.temperature
      );
    },
    "section0.humidity": function() {
      console.log("humid: ", this.section0.humidity);
      this.PublishMqtt("iot/sensors/section0/humidty", this.section0.humidity);
    },
    "section1.shelf": function() {
      console.log("s1 shelf: ", this.section1.shelf);
      this.PublishMqtt("iot/sensors/section1/shelf", this.section1.shelf);
    },
    "section2.shelf": function() {
      console.log("s2 shelf: ", this.section2.shelf);
      this.PublishMqtt("iot/sensors/section2/shelf", this.section2.shelf);
    }
  },
  methods: {
    PublishMqtt(path, msg) {
      this.$mqtt.publish(path, msg);
    },
    personCount(where, section) {
      console.log(where, section, "1");
      this.PublishMqtt("iot/sensors/" + section + "/button/" + where, 1);
      setTimeout(() => {
        console.log(where, section, "0");
        this.PublishMqtt("iot/sensors/" + section + "/button/" + where, 0);
      }, 100);
    }
  },
  components: {}
};
</script>

<style>

</style>