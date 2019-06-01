<template>
  <div class="p-register e-container">
    <div class="e-container-header"></div>
    <div class="e-container-body">
      <h3 class="e-h1 e-color-purple">Registro</h3>
      <p class="e-p1">Lorem ipsum dolor sit amet, consectetur adipisicing elit,</p>
      <v-flex xs12 md4>
        <v-text-field label="Email" append-icon="email"></v-text-field>
        <!-- <v-text-field v-model="lastname" :rules="nameRules" label="Email" required></v-text-field> -->
      </v-flex>
      <v-flex xs12 md4>
        <v-text-field label="Contraseña" append-icon="lock"></v-text-field>
        <!-- <v-text-field v-model="lastname" :rules="nameRules" label="Contraseña" required></v-text-field> -->
      </v-flex>
    </div>

    <div class="e-container-footer">
      <button class="e-button">Continuar</button>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    //   HelloWorld
  }
};
</script>

<style lang="stylus">
.p-register {
  background: #f4f8ff;
}
</style>
