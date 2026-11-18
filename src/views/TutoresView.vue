
<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';
import { apiRequest } from '../services/api.js';

const tutores = ref([]);
const pets = ref([]);
const erroApi = ref('');

async function carregarTutores() {
  try {
    [tutores.value, pets.value] = await Promise.all([
      apiRequest('/tutores'),
      apiRequest('/pets'),
    ]);
    erroApi.value = '';
  } catch (erro) {
    console.error('Erro ao carregar tutores:', erro);
    erroApi.value = erro.message;
  }
}

function petsDoTutor(tutorId) {
  return pets.value.filter((pet) => String(pet.tutorId) === String(tutorId));
}

async function excluirTutor(id) {
  const confirmarExclusao = window.confirm(
    'Tem certeza que deseja excluir este tutor?',
  );

  if (!confirmarExclusao) {
    return;
  }

  try {
    await apiRequest(`/tutores/${id}`, {
      method: 'DELETE',
    });

    await carregarTutores();
  } catch (erro) {
    console.error('Erro ao excluir tutor:', erro);
    erroApi.value = erro.message;
  }
}

onMounted(carregarTutores);
</script>

<template>
  <div>
    <header class="mb-4">
      <h1 class="text-2xl font-bold">Listagem de Tutores</h1>
      <p class="text-body-secondary">
        Listagem dos tutores cadastrados no sistema.
      </p>
    </header>

    <RouterLink
      :to="{ name: 'addTutor' }"
      class="btn btn-success mb-3"
    >
      Cadastrar Tutor
    </RouterLink>

    <div
      v-if="erroApi"
      class="alert alert-danger"
      role="alert"
    >
      {{ erroApi }}
    </div>

    <div class="table-responsive">
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>CPF / CNPJ</th>
            <th>Telefone</th>
            <th>Cidade</th>
            <th>Pets/quantidade</th>
            <th>Pets/nome</th>
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
            <td>{{ tutor.cpfCnpj }}</td>
            <td>{{ tutor.telefone }}</td>
            <td>{{ tutor.cidade }}</td>
            <td>{{ petsDoTutor(tutor.id).length }}</td>
            <td>
              {{ petsDoTutor(tutor.id).map((pet) => pet.nome).join(', ') || 'Nenhum pet' }}
            </td>

            <td>
              <RouterLink
                class="btn btn-primary btn-sm me-2"
                :to="{ name: 'detalhes-tutor', params: { id: tutor.id } }"
              >
                EDITAR
              </RouterLink>

              <button
                class="btn btn-danger btn-sm"
                @click="excluirTutor(tutor.id)"
              >
                EXCLUIR
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
