<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';

const API_URL = 'http://localhost:3000';
const tutores = ref([]);

async function carregarTutores() {
  const resposta = await fetch(`${API_URL}/tutores`);
  tutores.value = await resposta.json();
}

async function excluirTutor(id) {
  const confirmarExclusao = window.confirm(
    'Tem certeza que deseja excluir este tutor?',
  );

  if (!confirmarExclusao) {
    return;
  }

  await fetch(`${API_URL}/tutores/${id}`, {
    method: 'DELETE',
  });

  await carregarTutores();
}

onMounted(carregarTutores);
</script>

<template>
  <div>
    <header>
      <h1>Listagem de Tutores</h1>
      <p>Listagem dos tutores cadastrados no sistema.</p>
    </header>

    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Telefone</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="tutor in tutores"
          :key="tutor.id"
        >
          <td>{{ tutor.id }}</td>
          <td>{{ tutor.nome }}</td>
          <td>{{ tutor.telefone }}</td>
          <td>
            <RouterLink
              :to="{ name: 'detalhes-tutor', params: { id: tutor.id } }"
            >
              EDITAR
            </RouterLink>

            <button
              class="btn btn-danger"
              @click="excluirTutor(tutor.id)"
            >
              EXCLUIR
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
