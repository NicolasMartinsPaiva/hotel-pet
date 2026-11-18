
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

    <table class="table table-striped table-hover align-middle">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Telefone</th>
          <th>Email</th>
          <th>CPF/CNPJ</th>
          <th>Data de Nascimento</th>
          <th>CEP</th>
          <th>Número</th>
          <th>Bairro</th>
          <th>Cidade</th>
          <th>Estado</th>
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
          <td>{{ tutor.email}}</td>
          <td>{{ tutor.cpfCnpj }}</td>
          <td>{{ tutor.dataNascimento }}</td>
          <td>{{ tutor.cep }}</td>
          <td>{{ tutor.numero }}</td>
          <td>{{ tutor.bairro }}</td>
          <td>{{ tutor.cidade }}</td>
          <td>{{ tutor.estado }}</td>
          <td>
            <div class="d-flex gap-2">
              <RouterLink
                class="btn btn-sm btn-primary"
                :to="{ name: 'detalhes-tutor', params: { id: tutor.id } }"
              >
                Visualizar
              </RouterLink>

              <button
                class="btn btn-sm btn-danger"
                @click="excluirTutor(tutor.id)"
              >
                EXCLUIR
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
