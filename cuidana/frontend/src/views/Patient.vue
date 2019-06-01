<template>
  <div class="p-patient e-container">
    <div class="e-container-header isNavigation">
      <div class="e-navigation">
        <img src="../assets/icon_regresar.png" class="e-navigation-img">
        <label class="e-navigation-title">Datos del paciente</label>
      </div>

      <div class="p-patient__avatar-container">
        <img class="p-patient__avatar" src="../assets/foto_alicia.png">
        <label for class="p-patient__avatar-name">Alicia Mendoza</label>
      </div>
    </div>

    <div class="e-container-body">
      <v-tabs v-model="active" color="white" dark slider-color="yellow">
        <v-tab key="1" ripple>MEDICAMENTOS</v-tab>
        <v-tab-item key="1">
          <div class="p-patient__medicament-list">
            <div
              class="p-patient__medicament-item"
              v-for="item in $store.state.medicaments"
              :key="item"
            >
              <img
                :src="require(`../assets/${item.img}`)"
                alt
                class="p-patient__medicament-item-img"
              >
              <div class="p-patient__medicament-item-text">
                <div class="p-patient__medicament-item-text-row">
                  <img
                    src="../assets/icon_medicamento.png"
                    alt
                    class="p-patient__medicament-item-icon"
                  >
                  <label for class="p-patient__medicament-item-text-label">{{item.name}}</label>
                </div>
                <div class="p-patient__medicament-item-text-row">
                  <img src="../assets/icon_tiempo.png" alt class="p-patient__medicament-item-icon">
                  <label for class="p-patient__medicament-item-text-label">{{item.time}}</label>
                </div>
              </div>
            </div>
          </div>
        </v-tab-item>

        <v-tab key="2" ripple>INFORMACIÓN</v-tab>
        <v-tab-item key="2">En progreso ...</v-tab-item>
      </v-tabs>
    </div>

    <div class="e-container-footer"></div>
    <a href class="p-patient__btn-add e-button"></a>
    <router-link to="/medicamento" class="p-patient__btn-add e-button">
      <img src="../assets/icon_mas.png" alt>
      Añadir
    </router-link>
  </div>
</template>

<script>
export default {};
</script>

<style lang="stylus">
.p-patient {
  &.e-container {
    justify-content: flex-start;
  }

  .e-container-body {
    padding: 0 0 60px 0;
  }

  .v-tabs__item:not(.v-tabs__item--active) {
    color: #858696;
    opacity: 1;
  }

  .v-tabs__item.v-tabs__item--active {
    color: #f92f27;
  }

  .v-tabs__slider {
    background-color: #f92f27 !important;
    border-color: #f92f27 !important;
  }

  .theme--dark.v-tabs__bar .v-tabs__div {
    width: 50%;
  }
}

.p-patient__avatar-container {
  display: flex;
  align-items: center;
  padding: 10px 0 20px 0;
}

.p-patient__avatar {
  width: 64px;
  height: 64px;
  margin-right: 15px;
}

.p-patient__avatar-name {
  font-size: 16px;
  color: white;
}

.p-patient__medicament-item {
  margin: 0 20px;
  border: 1px solid #d0d5dd;
  border-radius: 10px;
  margin-top: 15px;
  background: white;
  padding: 12px;
  display: flex;
  align-items: center;
}

.p-patient__medicament-item-img {
  width: 50px;
  height: 50px;
  margin-right: 15px;
}

.p-patient__medicament-item-text-row {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.p-patient__medicament-item-icon {
  width: 18px;
  margin-right: 10px;
}

.p-patient__medicament-item-text-label {
  font-size: 14px;
  color: #202e44;
}

.p-patient__btn-add {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: auto;
  padding: 10px 20px;
  z-index: 1000;
  display: flex;
  align-items: center;

  img {
    width: 18px;
    margin-right: 5px;
    margin-top: -2px;
  }
}
</style>
