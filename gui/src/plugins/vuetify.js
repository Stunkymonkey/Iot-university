import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
    options: {
        customProperties: true
    },
    theme: {
        dark: true,
        themes: {
           
            dark: {
                dark_primary: '#272727',
                light_primary: '#424242',
                primary: '#303030',
                background: '#121212',
                accent: '#00BCD4',
                primary_text: '#FFFFFF',
                secondary_text: '#b3b3b3',
                dark_text: '#FFFFFF',
                divider: '#BDBDBD',
            },
        }
    },
});
