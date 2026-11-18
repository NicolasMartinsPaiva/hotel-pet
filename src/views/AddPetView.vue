<script setup>
  import { onMounted, ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { apiRequest } from '../services/api.js';

 // chamando a minha API para exibir os dados de tutor
  const router = useRouter();
  const erroApi = ref('');

  // chamando a minha API para exibir os dados de tutor
  const tutores = ref([]);

  async function carregarTutores() {
    try {
      tutores.value = await apiRequest('/tutores');
      erroApi.value = '';
    } catch (erro) {
      console.error('Erro ao carregar tutores:', erro);
      erroApi.value = erro.message;
    }
  }

  // chamando a minha API para salvar os dados de pet
  const novoPet = ref({
    nome: '',
    especie: '',
    tutorId: '',
  });

  async function salvarPet() {
    try {
      await apiRequest('/pets', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(novoPet.value),
      });
      router.push({ name: 'pets' });
    } catch (erro) {
      console.error('Erro ao salvar o pet:', erro);
      erroApi.value = erro.message;
    }
  }

  onMounted(carregarTutores);
</script>

<template>
  <div>
    <header class="mb-4">
      <h1 class="text-2xl font-bold">Cadastro de Pets</h1>
      <p class="text-body-secondary mb-0">Cadastro de Pets no sistema.</p>
    </header>

    <div
      v-if="erroApi"
      class="alert alert-danger"
      role="alert"
    >
      {{ erroApi }}
    </div>

    <!--
    <RouterLink
      class="btn btn-primary"
      :to="{ name: 'addPet' }"
    >
      Adicionar Pet
    </RouterLink>
    -->


    <form @submit.prevent="salvarPet">
      <div class="col-md-6 mb-3">
        <label for="nome" class="form-label">Nome do pet:</label>
        <input
          type="text"
          id="nome"
          v-model="novoPet.nome"
          class="form-control"
          required
        />
      </div>


      <div class="col-md-6">
        <label for="especie" class="form-label">Espécie:</label>
        <select
          v-model="novoPet.especie"
          class="form-select"
          required
        >
          <option value="" disabled>Selecione a espécie</option>
          <option value="Cachorro">Cachorro</option>
        </select>
      </div>


       <div class="col-md-6">
        <label for="tutorId" class="form-label">Tutor:</label>
        <select
          v-model="novoPet.tutorId"
          class="form-select"
          required
        >
          <option value="" disabled>Selecione o tutor</option>
          <option v-for="tutor in tutores" :value="tutor.id" :key="tutor.id">
            {{ tutor.nome }}
            </option>
        </select>
      </div>


      <button type="submit" class="btn btn-success">Salvar</button>
    </form>
  </div>
</template>
