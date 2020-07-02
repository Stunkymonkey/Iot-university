<template>
  <v-app dark>
    <v-app-bar app dark class="mb-0">
      <v-toolbar-title>
        <div class="crowstitle">CROWS</div>
      </v-toolbar-title>
    </v-app-bar>
    <v-main dark>
      <v-container dark justify-space-between align-content-space-between>
        <v-col>
          <v-row class="hidden-sm-and-down">
            <v-col cols="12" lg="6" xl="6" md="6">
              <h1>Sensors</h1>
            </v-col>
            <v-col cols="12" lg="6" xl="6" md="6">
              <h1>Actuators</h1>
            </v-col>
          </v-row>
          <v-row align="stretch">
            <v-col cols="12" lg="6" xl="6" md="6" align="stretch">
              <v-card flat class="mx-auto myrow1" fluid outlined>
                <v-list-item>
                  <v-list-item-content>
                    <div class="overline mb-1">
                      Main Section
                      <span class="hidden-md-and-up">Sensors</span>
                    </div>
                    <v-subheader class="mt-0 mb-0 pt-0 pb-0">Temperature</v-subheader>
                    <v-card-text class="mt-0 mb-0 pt-0 pb-0">
                      <v-slider
                        dense
                        height="2"
                        color="accent"
                        min="0"
                        max="40"
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
                      <v-btn @click="personCount('in', 'section0')" color="success">Enter</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn @click="personCount('out', 'section0')" color="error">Leave</v-btn>
                    </v-list-item>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-col>
            <v-col cols="12" lg="6" xl="6" md="6">
              <v-card class="mx-auto myrow1" fluid outlined>
                <v-list-item>
                  <v-list-item-content>
                    <div class="overline mb-4">
                      Main Section
                      <span class="hidden-md-and-up">Actuators</span>
                    </div>
                    <v-row class="wrapper">
                      <v-col cols="4" class="mx-auto">
                        <v-row>Gate: {{section0.gate}}</v-row>
                        <v-row>
                          <v-icon class="alert" name="ban" scale="3" v-if="section0.gate === '-'"></v-icon>
                          <v-icon class="mysuc" name="check" scale="3" v-else></v-icon>
                        </v-row>
                      </v-col>
                      <v-col cols="4" class="mx-auto">
                        <v-row>Ventilator</v-row>
                        <v-row>
                          <v-icon
                            class="mysuc"
                            name="fan"
                            spin
                            scale="3"
                            v-if="section0.ventilator === 'True'"
                          ></v-icon>
                          <v-icon name="fan" scale="3" class="alert" v-else></v-icon>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" lg="6" xl="6" md="6">
              <v-card class="mx-auto myrow2" fluid outlined>
                <v-list-item>
                  <v-list-item-content>
                    <div class="overline mb-1">
                      Section 1
                      <span class="hidden-md-and-up">Sensors</span>
                    </div>
                    <v-subheader class="mt-0 mb-0 pt-0 pb-0">Shelf (in cm)</v-subheader>
                    <v-card-text class="mt-0 mb-0 pt-0 pb-0">
                      <v-slider
                        dense
                        height="2"
                        color="accent"
                        step="3.5"
                        min="2"
                        max="20"
                        v-model="section1.shelf"
                      >
                        <template v-slot:append>
                          <div class="sensorlabel">{{section1.shelf}}</div>
                        </template>
                      </v-slider>
                    </v-card-text>

                    <v-list-item>
                      <v-btn @click="personCount('in', 'section1')" color="success">Enter</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn @click="personCount('out', 'section1')" color="error">Leave</v-btn>
                    </v-list-item>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-col>
            <v-col cols="12" lg="6" xl="6" md="6">
              <v-card class="mx-auto myrow2" fluid outlined>
                <v-list-item>
                  <v-list-item-content>
                    <div class="overline mb-4">
                      Section 1
                      <span class="hidden-md-and-up">Actuators</span>
                    </div>
                    <v-row class="wrapper">
                      <v-col cols="4" class="mx-auto">
                        <v-row>Person Counter</v-row>
                        <v-row>
                          <v-img
                            v-if="section1.led === '0'"
                            contain
                            max-width="62px"
                            src="@/images/LED_0.png"
                          ></v-img>
                          <v-img
                            v-else-if="section1.led === '1'"
                            contain
                            max-width="62px"
                            src="@/images/LED_1.png"
                          ></v-img>
                          <v-img
                            v-else-if="section1.led === '2'"
                            contain
                            max-width="62px"
                            src="@/images/LED_2.png"
                          ></v-img>
                          <v-img
                            v-else-if="section1.led === '3'"
                            contain
                            max-width="62px"
                            src="@/images/LED_3.png"
                          ></v-img>
                          <v-img
                            v-else-if="section1.led === '4'"
                            contain
                            max-width="62px"
                            src="@/images/LED_4.png"
                          ></v-img>
                          <v-img
                            v-else-if="section1.led === '-'"
                            contain
                            max-width="62px"
                            src="@/images/LED_-.png"
                          ></v-img>
                          <v-img v-else contain max-width="62px" src="@/images/LED_off.png"></v-img>
                        </v-row>
                      </v-col>
                      <v-col cols="4" class="mx-auto">
                        <v-row>Refill Shelf</v-row>
                        <v-row>
                          <div v-if="section1.refill_shelf === 'True'">
                            <v-icon class="notificationicon" name="bell" scale="2"></v-icon>
                          </div>
                          <div v-else>
                            <v-icon class="inactive" name="bell" scale="2"></v-icon>
                          </div>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" lg="6" xl="6" md="6">
              <v-card class="mx-auto myrow3" fluid outlined>
                <v-list-item>
                  <v-list-item-content>
                    <div class="overline mb-1">
                      Section 2
                      <span class="hidden-md-and-up">Sensors</span>
                    </div>
                    <v-subheader class="mt-0 mb-0 pt-0 pb-0">Shelf (in cm)</v-subheader>
                    <v-card-text class="mt-0 mb-0 pt-0 pb-0">
                      <v-slider
                        dense
                        height="2"
                        color="accent"
                        step="3.5"
                        min="2"
                        max="20"
                        v-model="section2.shelf"
                      >
                        <template v-slot:append>
                          <div class="sensorlabel">{{section2.shelf}}</div>
                        </template>
                      </v-slider>
                    </v-card-text>

                    <v-list-item>
                      <v-btn @click="personCount('in', 'section2')" color="success">Enter</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn @click="personCount('out', 'section2')" color="error">Leave</v-btn>
                    </v-list-item>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-col>
            <v-col cols="12" lg="6" xl="6" md="6">
              <v-card class="mx-auto myrow3" fluid outlined>
                <v-list-item>
                  <v-list-item-content>
                    <div class="overline mb-4">
                      Section 2
                      <span class="hidden-md-and-up">Actuators</span>
                    </div>
                    <v-row class="wrapper">
                      <v-col cols="4" class="mx-auto">
                        <v-row>Person Counter</v-row>
                        <v-row>
                          <v-img
                            v-if="section2.led === '0'"
                            contain
                            max-width="62px"
                            src="@/images/LED_0.png"
                          ></v-img>
                          <v-img
                            v-else-if="section2.led === '1'"
                            contain
                            max-width="62px"
                            src="@/images/LED_1.png"
                          ></v-img>
                          <v-img
                            v-else-if="section2.led === '2'"
                            contain
                            max-width="62px"
                            src="@/images/LED_2.png"
                          ></v-img>
                          <v-img
                            v-else-if="section2.led === '3'"
                            contain
                            max-width="62px"
                            src="@/images/LED_3.png"
                          ></v-img>
                          <v-img
                            v-else-if="section2.led === '4'"
                            contain
                            max-width="62px"
                            src="@/images/LED_4.png"
                          ></v-img>
                          <v-img
                            v-else-if="section2.led === '-'"
                            contain
                            max-width="62px"
                            src="@/images/LED_-.png"
                          ></v-img>
                          <v-img v-else contain max-width="62px" src="@/images/LED_off.png"></v-img>
                        </v-row>
                      </v-col>
                      <v-col cols="4" class="mx-auto">
                        <v-row>Refill Shelf</v-row>
                        <v-row>
                          <div v-if="section2.refill_shelf === 'True'">
                            <v-icon class="notificationicon" name="bell" scale="2"></v-icon>
                          </div>
                          <div v-else>
                            <v-icon class="inactive" name="bell" scale="2"></v-icon>
                          </div>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-container>
    </v-main>
    <v-footer class="mt-12" fixed>
      <div class="footer">Felix Bühler, Jamie Ullerich, Jan Leusmann</div>
      <v-spacer></v-spacer>
      <div class="footer">Smart Cities and Internet of Things Project Summerterm 2020</div>
    </v-footer>
  </v-app>
</template>

<script>
import Icon from "vue-awesome/components/Icon";
export default {
  name: "App",
  data() {
    return {
      section0: {
        temperature: 20,
        humidity: 40,
        ventilator: "False",
        gate: "0"
      },
      section1: {
        shelf: 5,
        led: "0",
        refill_shelf: "False",
        gate: "False"
      },
      section2: {
        shelf: 5,
        led: "0",
        refill_shelf: "False",
        gate: "False"
      }
    };
  },
  mounted() {
    this.$mqtt.subscribe("iot/#");
  },
  mqtt: {
    "iot/actuators/section1/gate"(data, topic) {
      console.log(String.fromCharCode.apply(null, data), topic);
      this.section1.led = String.fromCharCode.apply(null, data);
    },
    "iot/actuators/section2/gate"(data, topic) {
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
    }
    // "iot/actuators/section1/gate"(data, topic) {
    //   console.log(String.fromCharCode.apply(null, data), topic);
    //   this.section1.gate = String.fromCharCode.apply(null, data);
    // },
    // "iot/actuators/section2/gate"(data, topic) {
    //   console.log(String.fromCharCode.apply(null, data), topic);
    //   this.section2.gate = String.fromCharCode.apply(null, data);
    // }
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
        "iot/sensors/section0/humidity",
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
  components: { "v-icon": Icon }
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
.alert {
  color: #ff5252;
}
.mysuc {
  color: #4caf50;
}
.inactive {
  color: #666666;
}
.sensorlabel {
  min-width: 35px;
}
.emptyshelf {
  display: inline-block;
}
.wrapper {
  text-align: center;
}
.myrow1 {
  overflow-y: auto;
  height: 255px;
}
.myrow2 {
  overflow-y: auto;
  height: 185px;
}
.myrow3 {
  overflow-y: auto;
  height: 185px;
}
@keyframes shake {
  0% { transform: translate(1px, 1px) rotate(0deg); }
  10% { transform: translate(-1px, 0px) rotate(-1deg); }
  20% { transform: translate(-3px, 0px) rotate(1deg); }
  30% { transform: translate(3px, 0px) rotate(0deg); }
  40% { transform: translate(1px, 0px) rotate(1deg); }
  50% { transform: translate(-1px, 0px) rotate(-1deg); }
  60% { transform: translate(-3px, 0px) rotate(0deg); }
  70% { transform: translate(3px, 0px) rotate(-1deg); }
  80% { transform: translate(-1px, 0px) rotate(1deg); }
  90% { transform: translate(1px, 0px) rotate(0deg); }
  100% { transform: translate(1px, 0px) rotate(-1deg); }
}
.notificationicon {
  animation: shake 0.5s;
  animation-iteration-count: infinite;
}
</style>