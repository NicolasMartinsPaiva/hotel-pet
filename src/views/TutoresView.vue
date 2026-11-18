
<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';

const API_URL = 'http://localhost:3000';
const tutores = ref([]);

async function carregarTutores() {
  try {
    const resposta = await fetch(`${API_URL}/tutores`);

    if (!resposta.ok) {
      console.log('Erro ao carregar tutores');
      return;
    }

    tutores.value = await resposta.json();

  } catch (erro) {
    console.log('Erro ao carregar tutores:', erro);
  }
}

async function excluirTutor(id) {
  const confirmarExclusao = window.confirm(
    'Tem certeza que deseja excluir este tutor?',
  );

  if (!confirmarExclusao) {
    return;
  }

  try {
    const resposta = await fetch(`${API_URL}/tutores/${id}`, {
      method: 'DELETE',
    });

    if (!resposta.ok) {
      console.log('Erro ao excluir tutor');
      return;
    }

    await carregarTutores();

  } catch (erro) {
    console.log('Erro ao excluir tutor:', erro);
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

    <div class="mb-3">
      <RouterLink
        :to="{ name: 'addTutor' }"
        class="btn btn-success"
      >
        Cadastrar Tutor
      </RouterLink>
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
