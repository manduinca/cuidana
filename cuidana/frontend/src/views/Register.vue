<template>
  <form class="p-register e-container" v-on:submit="onSubmit">
    <div class="e-container-header"></div>
    <div class="e-container-body">
      <h3 class="e-h1 e-color-purple">Registro</h3>
      <p class="e-p1">Lorem ipsum dolor sit amet, consectetur adipisicing elit,</p>

      <v-flex xs12 md4>
        <v-text-field label="Email" append-icon="email"></v-text-field>
      </v-flex>

      <v-flex xs12 md4>
        <v-text-field label="Contraseña" append-icon="lock"></v-text-field>
      </v-flex>
    </div>

    <div class="e-container-footer">
      <button class="e-button" type="submit">Continuar</button>
    </div>
  </form>
</template>

<script>
export default {
  methods: {
    onSubmit: function(e) {
      e.preventDefault();
      this.$router.push({ name: "CompletedRegister" });
      console.log("aa");
    }
  }
};
</script>

<style lang="stylus">
.p-register {
  background: #f4f8ff;
}
</style>
