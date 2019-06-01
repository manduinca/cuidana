<template>
  <div class="p-dashboard e-container">
    <div class="e-container-header">
      <div class="p-dashboard__avatar-img"></div>
      <div class="p-dashboard__avatar-texts">
        <label for class="p-dashboard__avatar-name">Victor</label>
        <label for class="p-dashboard__avatar-mail">victormorales@gmail.com</label>
      </div>
    </div>
    <div class="e-container-body">
      <label for class="p-dashboard__title">A tu cuidado:</label>

      <div class="p-dashboard__person-list">
        <div class="p-dashboard__person">
          <div class="p-dashboard__person-img">
            <img src="../assets/foto_alicia.png">
          </div>
          <label for class="p-dashboard__person-name">Alicia</label>
        </div>

        <div class="p-dashboard__person">
          <div class="p-dashboard__person-img">
            <img src="../assets/foto_jorge.png">
          </div>
          <label for class="p-dashboard__person-name">Jorge</label>
        </div>

        <div class="p-dashboard__person">
          <div class="p-dashboard__person-img">+</div>
          <label for class="p-dashboard__person-name">Agregar</label>
        </div>
      </div>

      <div class="p-dashboard__notification">
        <div class="p-dashboard__notification-header">
          <label for class="p-dashboard__notification-title">Notificaciones</label>
          <div>
            <img class="p-dashboard__notification-title-icon" src="../assets/icon_notificacion.png">
          </div>
        </div>

        <div class="p-dashboard__notification-item">
          <div class="p-dashboard__notification-left">
            <div class="p-dashboard__notification-item-row">
              <div class="p-dashboard__notification-item-icon">
                <img src="../assets/icon_mujer.png">
              </div>
              <label for class="p-dashboard__notification-item-text bold">Alicia Lizarzaburu</label>
            </div>

            <div class="p-dashboard__notification-item-row">
              <div class="p-dashboard__notification-item-icon">
                <img src="../assets/icon_medicamento.png">
              </div>
              <label for class="p-dashboard__notification-item-text">Galantamina (Razadyne)</label>
            </div>

            <div class="p-dashboard__notification-item-row">
              <div class="p-dashboard__notification-item-icon">
                <img src="../assets/icon_tiempo.png">
              </div>
              <label for class="p-dashboard__notification-item-text">En 30 minutos</label>
            </div>
          </div>

          <div class="p-dashboard__notification-right">
            <img src="../assets/icon_check.png">
          </div>
        </div>

        <div class="p-dashboard__notification-item">
          <div class="p-dashboard__notification-left">
            <div class="p-dashboard__notification-item-row">
              <div class="p-dashboard__notification-item-icon">
                <img src="../assets/icon_mujer.png">
              </div>
              <label for class="p-dashboard__notification-item-text bold">Alicia Lizarzaburu</label>
            </div>

            <div class="p-dashboard__notification-item-row">
              <div class="p-dashboard__notification-item-icon">
                <img src="../assets/icon_medicamento.png">
              </div>
              <label for class="p-dashboard__notification-item-text">Galantamina (Razadyne)</label>
            </div>

            <div class="p-dashboard__notification-item-row">
              <div class="p-dashboard__notification-item-icon">
                <img src="../assets/icon_tiempo.png">
              </div>
              <label for class="p-dashboard__notification-item-text">En 30 minutos</label>
            </div>
          </div>

          <div class="p-dashboard__notification-right">
            <img src="../assets/icon_check_disabled.png">
          </div>
        </div>
      </div>
    </div>

    <div class="e-container-footer">
      <button class="e-button" type="submit">Continuar</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    onSubmit: function() {}
  }
};
</script>

<style lang="stylus">
.p-dashboard {
  .e-container-header {
    display: flex;
    align-items: center;
  }
}

.p-dashboard__avatar-img {
  width: 36px;
  height: 36px;
  background: gray;
  border-radius: 50%;
}

.p-dashboard__avatar-texts {
  display: flex;
  flex-direction: column;
  margin-left: 10px;
  line-height: 1;
}

.p-dashboard__avatar-name {
  font-weight: 600;
  margin-bottom: 4px;
}

.p-dashboard__avatar-mail {
  color: #8e9aab;
}

.p-dashboard__title {
  color: #2e3191;
  font-size: 14px;
  font-weight: 600;
}

.p-dashboard__person-list {
  margin-top: 18px;
  display: flex;
  flex-wrap: wrap;
}

.p-dashboard__person {
  text-align: center;
  margin-right: 20px;

  &:last-child {
    margin-right: 0;

    .p-dashboard__person-img {
      background: #e6edfa;
      font-size: 30px;
      color: #ffad00;
      font-weight: 600;
      align-items: center;
      display: flex;
      justify-content: center;
    }
  }
}

.p-dashboard__person-img {
  width: 90px;
  height: 90px;
  background: gray;
  border-radius: 50%;
  margin-bottom: 10px;

  img {
    width: 100%;
    height: 100%;
  }
}

.p-dashboard__person-name {
  color: #4d5b71;
}

.p-dashboard__notification-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 40px;
}

.p-dashboard__notification-title {
  color: #f92f27;
  font-weight: 600;
  font-size: 16px;
}

.p-dashboard__notification-title-icon {
  width: 25px;
}

.p-dashboard__notification-item {
  background: white;
  border-radius: 10px;
  border: 1px solid #d0d5dd;
  margin-top: 10px;
  padding: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.p-dashboard__notification-item-row {
  display: flex;
  align-items: center;
}

.p-dashboard__notification-item-text.bold {
  font-weight: 600;
}

.p-dashboard__notification-item-icon img {
  width: 15px;
  margin-right: 10px;
}

.p-dashboard__notification-right img {
  width: 48px;
  height: 48px;
}
</style>
