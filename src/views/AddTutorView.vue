<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const API_URL = 'http://localhost:3000';
const router = useRouter();

const novoTutor = ref({
  nome: '',
  telefone: '',
  email: '',
  cpfCnpj: '',
  dataNascimento: '',
  cep: '',
  numero: '',
  bairro: '',
  cidade: '',
  estado: '',
});

async function salvarTutor() {
  try {
    const resposta = await fetch(`${API_URL}/tutores`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(novoTutor.value),
    });

    if (!resposta.ok) {
      throw new Error('Erro ao cadastrar tutor');
    }

    router.push({ name: 'tutores' });

    novoTutor.value = {
      nome: '',
      telefone: '',
      email: '',
      cpfCnpj: '',
      dataNascimento: '',
      cep: '',
      numero: '',
      bairro: '',
      cidade: '',
      estado: '',
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
        >
          Nome do tutor:
        </label>
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
        >
          Telefone:
        </label>
        <input
          id="telefone"
          v-model="novoTutor.telefone"
          type="tel"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label
          for="email"
          class="form-label"
        >
          Email:
        </label>
        <input
          id="email"
          v-model="novoTutor.email"
          type="email"
          class="form-control"
        />
      </div>

      <div class="mb-3">
        <label
          for="cpfCnpj"
          class="form-label"
        >
          CPF/CNPJ:
        </label>
        <input
          id="cpfCnpj"
          v-model="novoTutor.cpfCnpj"
          type="text"
          class="form-control"
        />
      </div>

      <div class="mb-3">
        <label
          for="dataNascimento"
          class="form-label"
        >
          Data de Nascimento:
        </label>
        <input
          id="dataNascimento"
          v-model="novoTutor.dataNascimento"
          type="date"
          class="form-control"
        />
      </div>

      <h2 class="mt-4">Endereço</h2>

      <div class="mb-3">
        <label
          for="cep"
          class="form-label"
        >
          CEP:
        </label>
        <input
          id="cep"
          v-model="novoTutor.cep"
          type="text"
          class="form-control"
        />
      </div>

      <div class="mb-3">
        <label
          for="numero"
          class="form-label"
        >
          Número:
        </label>
        <input
          id="numero"
          v-model="novoTutor.numero"
          type="text"
          class="form-control"
        />
      </div>

      <div class="mb-3">
        <label
          for="bairro"
          class="form-label"
        >
          Bairro:
        </label>
        <input
          id="bairro"
          v-model="novoTutor.bairro"
          type="text"
          class="form-control"
        />
      </div>

      <div class="mb-3">
        <label
          for="cidade"
          class="form-label"
        >
          Cidade:
        </label>
        <input
          id="cidade"
          v-model="novoTutor.cidade"
          type="text"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label
          for="estado"
          class="form-label"
        >
          Estado:
        </label>
        <input
          id="estado"
          v-model="novoTutor.estado"
          type="text"
          class="form-control"
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
