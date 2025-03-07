<script setup lang="ts">
import { ref } from "vue";

// const inputValues = ref([0.5, 0.8, -0.1, 0.3, 0.9, 1.2, -0.5, 0.4, 0.2, 0.7]);
const prediction = ref(null);

const BASE_URL = import.meta.env.VITE_API_BASE_URL;

// `${BASE_URL}/predict` - string literal
// BASE_URL + '/predict' - string concatenation

const sendRequest = async () => {
  const response = await fetch(`${BASE_URL}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      values: [0.5, 0.8, -0.1, 0.3, 0.9, 1.2, -0.5, 0.4, 0.2, 0.7],
    }),
  });

  prediction.value = await response.json();
};
</script>

<template>
  <div>
    <h1>FastAPI Prediction Test</h1>
    <button @click="sendRequest">Send Request</button>
    <p v-if="prediction">Prediction: {{ prediction }}</p>
  </div>
</template>
