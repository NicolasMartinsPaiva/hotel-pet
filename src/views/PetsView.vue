<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';

const API_URL = 'http://localhost:3000';

const pets = ref([]);
const tutores = ref([]);

async function carregarDados() {
  const respostaPets = await fetch(`${API_URL}/pets`);
  pets.value = await respostaPets.json();

  const respostaTutores = await fetch(`${API_URL}/tutores`);
  tutores.value = await respostaTutores.json();
}

function nomeDoTutor(tutorId) {
  for(const tutor of tutores.value) {
    if (tutor.id == tutorId) {
      return tutor.nome;
    }
  }
  return 'Tutor não encontrado';
}

function excluirPet(id) {
  fetch(`${API_URL}/pets/${id}`, { method: 'DELETE' })
    .then(() => {
      pets.value = pets.value.filter(pet => pet.id !== id);
    })
    .catch(erro => {
      console.log('Erro ao excluir o pet:', erro);
    });
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
            <RouterLink :to="{ name: 'detalhes-pet', params: { id: pet.id } }">EDITAR</RouterLink>

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
