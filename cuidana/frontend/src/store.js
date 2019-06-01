import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    medicaments: [
      {
        name: "Galantamina (Razadyne)",
        time: "Hora: 5:00 pm",
        img: "foto_medicamento_1.png"
      },
      {
        name: "Exelon (Rivastigimina)",
        time: "Hora: 7:00 pm",
        img: "foto_medicamento_2.png"
      },
      {
        name: "Ciflox (Ciprofloxacina)",
        time: "Hora: 10:00 pm",
        img: "foto_medicamento_3.png"
      },
    ]

  },
  mutations: {

  },
  actions: {

  }
})
