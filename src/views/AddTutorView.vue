<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const API_URL = 'http://localhost:3000';
const router = useRouter();

const novoTutor = ref({
  nome: '',
  telefone: '',
});

async function salvarTutor() {
  try {
    await fetch(`${API_URL}/tutores`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(novoTutor.value),
    });

    router.push({ name: 'tutores' });

    novoTutor.value = {
      nome: '',
      telefone: '',
    };
  } catch (erro) {
    console.log('Erro ao salvar o novo tutor:', erro);
  }
}
</script>

<template>
  <div>
    <header class="mb-4">
      <h1 class="text-2xl font-bold">Cadastro de Tutor</h1>
      <p class="text-body-secondary mb-0">
        Adicionar um novo tutor ao sistema.
      </p>
    </header>

    <form @submit.prevent="salvarTutor">
      <div class="col-md-6 mb-3">
        <label
          for="nome"
          class="form-label"
          >Nome do tutor:</label
        >
        <input
          id="nome"
          v-model="novoTutor.nome"
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
          v-model="novoTutor.telefone"
          type="tel"
          class="form-control"
          required
        />
      </div>

      <button
        type="submit"
        class="btn btn-success"
      >
        Salvar
      </button>
    </form>
  </div>
</template>
