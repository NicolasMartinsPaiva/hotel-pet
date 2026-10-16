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
