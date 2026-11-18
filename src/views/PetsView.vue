<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';
import { apiRequest } from '../services/api.js';

const pets = ref([]);
const tutores = ref([]);
const erroApi = ref('');

async function carregarDados() {
  try {
    const [listaPets, listaTutores] = await Promise.all([
      apiRequest('/pets'),
      apiRequest('/tutores'),
    ]);
    pets.value = listaPets;
    tutores.value = listaTutores;
    erroApi.value = '';
  } catch (erro) {
    console.error('Erro ao carregar pets e tutores:', erro);
    erroApi.value = erro.message;
  }
}

function nomeDoTutor(tutorId) {
  for(const tutor of tutores.value) {
    if (tutor.id == tutorId) {
      return tutor.nome;
    }
  }
  return 'Tutor não encontrado';
}

async function excluirPet(id) {
  const confirmarExclusao =  window.confirm('Tem certeza que deseja excluir este pet?');

  if (confirmarExclusao) {
    try {
      await apiRequest(`/pets/${id}`, {
        method: 'DELETE',
      });
      await carregarDados();
    } catch (erro) {
      console.error('Erro ao excluir pet:', erro);
      erroApi.value = erro.message;
    }
  }
}

onMounted(carregarDados);
</script>

<template>
  <div>
    <header>
      <h1>Listagem de Pets</h1>
      <p>
        Listagem dos Pets cadastrados no sistema.
      </p>
    </header>

    <div
      v-if="erroApi"
      class="alert alert-danger"
      role="alert"
    >
      {{ erroApi }}
    </div>

    <table class="table table-striped table-hover ">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Espécie</th>
          <th>Tutor</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="pet in pets"
          :key="pet.id"
        >
          <td>{{ pet.id }}</td>
          <td>{{ pet.nome }}</td>
          <td>{{ pet.especie }}</td>
          <td>
            {{ nomeDoTutor(pet.tutorId) }}
          </td>
          <td>
            <RouterLink
              class="btn btn-primary"
              :to="{ name: 'detalhes-pet', params: { id: pet.id } }"
            >
              EDITAR
            </RouterLink>

            <button
              class="btn btn-danger"
              @click="excluirPet(pet.id)"
            >
              EXCLUIR
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
