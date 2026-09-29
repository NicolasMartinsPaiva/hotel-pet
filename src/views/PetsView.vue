<script setup>
import { onMounted, ref } from 'vue';

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
        </tr>
      </tbody>
    </table>
  </div>
</template>
