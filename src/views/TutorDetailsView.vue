<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const API_URL = 'http://localhost:3000';

const tutor = ref(null);

async function carregarTutor() {
  try {
    const respostaTutor = await fetch(`${API_URL}/tutores/${route.params.id}`);

    if (!respostaTutor.ok) {
      console.log('Opss, tutor não encontrado');
      tutor.value = null;
      return;
    }

    tutor.value = await respostaTutor.json();
  } catch (erro) {
    console.log('Erro ao carregar os dados do tutor:', erro);
    tutor.value = null;
  }
}

async function removerTutor() {
  const confirmarExclusao = window.confirm(
    'Tem certeza que deseja remover este tutor?',
  );

  if (!confirmarExclusao) {
    return;
  }

  try {
    await fetch(`${API_URL}/tutores/${route.params.id}`, {
      method: 'DELETE',
    });

    router.push({ name: 'tutores' });
  } catch (erro) {
    console.log('Erro ao remover o tutor:', erro);
  }
}

onMounted(carregarTutor);
</script>

<template>
  <div v-if="tutor">
    <header class="mb-4">
      <h1>Detalhes do Tutor</h1>
      <p class="mb-0 text-body-secondary">
        Informações do tutor e pets vinculados.
      </p>
    </header>

    <div class="mb-4">
      <h2>Dados do tutor</h2>
      <p><strong>ID:</strong> {{ tutor.id }}</p>
      <p><strong>Nome:</strong> {{ tutor.nome }}</p>
      <p><strong>Telefone:</strong> {{ tutor.telefone }}</p>
      <p><strong>Email:</strong> {{ tutor.email }}</p>
      <p><strong>CPF/CNPJ:</strong> {{ tutor.cpfCnpj }}</p>
      <p><strong>Data de nascimento:</strong> {{ tutor.dataNascimento }}</p>
    </div>

    <div class="mb-4">
      <h2>Endereço</h2>
      <p><strong>CEP:</strong> {{ tutor.cep }}</p>
      <p><strong>Rua:</strong> {{ tutor.rua || 'Rua não informada' }}</p>
      <p><strong>Número:</strong> {{ tutor.numero }}</p>
      <p><strong>Bairro:</strong> {{ tutor.bairro }}</p>
      <p><strong>Cidade:</strong> {{ tutor.cidade }}</p>
      <p><strong>Estado:</strong> {{ tutor.estado }}</p>
    </div>

    <div class="mb-4">
      <h2>Pets vinculados</h2>
      <ul
        v-if="tutor.pets && tutor.pets.length"
        class="list-group"
      >
        <li
          v-for="pet in tutor.pets"
          :key="pet.id"
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          <span>{{ pet.nome }}</span>
          <RouterLink
            class="btn btn-sm btn-primary"
            :to="{ name: 'detalhes-pet', params: { id: pet.id } }"
          >
            Visualizar
          </RouterLink>
        </li>
      </ul>
      <p
        v-else
        class="mb-0"
      >
        Nenhum pet vinculado a este tutor.
      </p>
    </div>

    <div class="d-flex gap-2">
      <RouterLink
        class="btn btn-primary"
        :to="{ name: 'tutores' }"
      >
        Voltar
      </RouterLink>

      <button
        class="btn btn-danger"
        @click="removerTutor"
      >
        Remover Tutor
      </button>
    </div>
  </div>

  <div v-else>Carregando tutor...</div>
</template>
