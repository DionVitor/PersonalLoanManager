<script>
import axios from 'axios'

export default {
  data() {
    return {
      offerFields: [],
      error: false,
      loading: false,
      sent: false
    }
  },
  created: function() {
    this.getFields();
  },
  methods: {
    getFields() {
      function catchErrorInAPI() {
        this.error = true;
      }

      axios.get("http://localhost:8000/loan-fields").then((response => {
        if(response.status === 200) {
          this.offerFields = response.data;
        } else {
          catchErrorInAPI();
        }
      }))
    },
    sendOffer() {
      function catchErrorInAPI() {
        this.error = true;
      }

      let answeredFields = {};
      for(let i = 0; i < this.offerFields.length; i++) {
        answeredFields[this.offerFields[i].name] = document.getElementById(this.offerFields[i].id).value;
      }
      console.log(answeredFields);
      axios.post(
          "http://localhost:8000/loan-offer",
          JSON.stringify({answered_fields: answeredFields}),
          {
            headers: {
              "Content-Type": "application/json"
            }
          }
      ).then((response => {
        if(response.status === 201) {
          this.sent = true;
          console.log(response.data);
        } else {
          catchErrorInAPI();
        }
      }))
    },
    backOfferPage() {
      this.error = false;
      this.loading = false;
      this.sent = false;
    }
  }
}
</script>

<template>
  <main v-if="!error & !loading & !sent">
    <div v-for="field in offerFields">
      <p>{{ field.name }}</p>
      <input v-bind:id="field.id">
    </div>

    <button v-on:click="sendOffer">Enviar</button>
  </main>

  <div id="getFieldError" v-if="error">
    <p>Erro na conexão com a API!</p>
  </div>

  <div id="loading" v-if="loading">
    <p>Carregando...</p>
  </div>

  <div id="sent" v-if="sent">
    <p>Enviado!</p>
    <button v-on:click="backOfferPage">Cadastre outro!</button>
  </div>
</template>
