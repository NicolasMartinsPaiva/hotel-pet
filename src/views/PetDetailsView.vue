<script setup>
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { apiRequest } from '../services/api.js';

const route = useRoute();
const router = useRouter();

const pet = ref(null);
const tutores = ref([]);

async function carregarPet() {
  try {
    pet.value = await apiRequest(`/pets/${route.params.id}`);
    tutores.value = await apiRequest('/tutores');
  } catch (erro) {
    console.error('Erro ao carregar os dados do pet:', erro);
  }
}

async function salvarEdicao() {
  try {
    await apiRequest(`/pets/${route.params.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(pet.value),
    });
    router.push({ name: 'pets' });
  } catch (erro) {
    console.error('Erro ao salvar as alterações do pet:', erro);
  }
}

onMounted(carregarPet);
</script>

<template>
  <div v-if="pet">
    <form @submit.prevent="salvarEdicao">
      <div class="mb-3">
        <label for="nome" class="form-label">Nome do pet:</label>
        <input
          id="nome"
          v-model="pet.nome"
          type="text"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label for="especie" class="form-label">Espécie:</label>
        <select
          id="especie"
          v-model="pet.especie"
          class="form-select"
          required
        >
          <option value="" disabled>Selecione a espécie</option>
          <option value="Cachorro">Cachorro</option>
          <option value="Gato">Gato</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="tutorId" class="form-label">Tutor:</label>
        <select
          id="tutorId"
          v-model="pet.tutorId"
          class="form-select"
          required
        >
          <option value="" disabled>Selecione o tutor</option>
          <option v-for="tutor in tutores" :key="tutor.id" :value="tutor.id">
            {{ tutor.nome }}
          </option>
        </select>
      </div>

      <button type="submit" class="btn btn-success">
        Salvar alterações
      </button>
    </form>
  </div>

  <div v-else>Carregando pet...</div>
</template>
