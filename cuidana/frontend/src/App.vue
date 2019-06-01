<template>
  <v-app>
    <!-- <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>open_in_new</v-icon>
      </v-btn>
    </v-toolbar>

    <v-content>
    </v-content>-->
    <router-view/>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      //
    };
  }
};
</script>

<style lang="stylus">
* {
  font-family: 'Montserrat', sans-serif;
}

.e-container-header {
  padding: 20px 20px 0 20px;
}

.e-container-body {
  padding: 20px;
}

.e-container-footer {
  padding: 0px 20px 20px 20px;
}

.e-h1 {
  font-size: 24px;
}

.e-p1 {
  font-size: 16px;
  line-height: 20px;
  color: #202e44;
}

.e-color-purple {
  color: #2e3191;
}

.e-button {
  padding: 10px 0;
  width: 100%;
  background: #2e3191;
  color: white;
  border-radius: 10px;
  font-weight: 600;
}

.e-text-semibold {
}

.e-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
