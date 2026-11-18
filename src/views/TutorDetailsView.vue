<script setup>
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

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

async function salvarEdicao() {
  if (!tutor.value) {
    return;
  }

  try {
    await fetch(`${API_URL}/tutores/${route.params.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(tutor.value),
    });

    router.push({ name: 'tutores' });
  } catch (erro) {
    console.log('Erro ao salvar as alterações do tutor:', erro);
  }
}

onMounted(carregarTutor);
</script>

<template>
  <div v-if="tutor">
    <header class="mb-4">
      <h1>Editar Tutor</h1>
      <p class="mb-0 text-body-secondary">Atualize os dados do tutor.</p>
    </header>

    <form @submit.prevent="salvarEdicao">
      <div class="col-md-6 mb-3">
        <label
          for="nome"
          class="form-label"
          >Nome:</label
        >
        <input
          id="nome"
          v-model="tutor.nome"
          type="text"
          class="form-control"
          required
        />
      </div>

      <div class="col-md-6 mb-3">
        <label
          for="telefone"
          class="form-label"
          >Telefone:</label
        >
        <input
          id="telefone"
          v-model="tutor.telefone"
          type="tel"
          class="form-control"
          required
        />
      </div>

      <button
        type="submit"
        class="btn btn-success"
      >
        Salvar alterações
      </button>
    </form>
  </div>

  <div v-else>Carregando tutor...</div>
</template>
