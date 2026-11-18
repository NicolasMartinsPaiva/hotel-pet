
<script setup>
import { ref } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { apiRequest } from '../services/api.js';

const router = useRouter();
const erroApi = ref('');

const novoTutor = ref({
  nome: '',
  cpfCnpj: '',
  telefone: '',
  email: '',
  cpfCnpj: '',
  dataNascimento: '',
  cep: '',
  rua: '',
  numero: '',
  bairro: '',
  cidade: '',
  estado: '',
});

const cepApi = ref({});

async function buscaCep(cep) {
  const API_CEP = 'https://viacep.com.br/ws';
  const respostaCep = await fetch(`${API_CEP}/${cep}/json/`);
  cepApi.value = await respostaCep.json();

  novoTutor.value.rua = cepApi.value.logradouro;
  novoTutor.value.bairro = cepApi.value.bairro;
  novoTutor.value.cidade = cepApi.value.localidade;
  novoTutor.value.estado = cepApi.value.uf;
}

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
      rua: '',
      numero: '',
      bairro: '',
      cidade: '',
      estado: '',
    };
  } catch (erro) {
    console.error('Erro ao salvar o novo tutor:', erro);
    erroApi.value = erro.message;
  }
}
</script>

<template>
  <div>
    <header class="mb-4">
      <h1 class="text-2xl font-bold">Cadastrar Tutores</h1>
      <p class="text-body-secondary">
        Cadastro de Tutores no sistema.
      </p>
    </header>

    <RouterLink
      :to="{ name: 'tutores' }"
      class="btn btn-outline-primary mb-2"
    >
      Lista Tutores
    </RouterLink>

    <div
      v-if="erroApi"
      class="alert alert-danger"
      role="alert"
    >
      {{ erroApi }}
    </div>

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
          placeholder="Digite o nome do tutor"
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
          placeholder="(00) 00000-0000"
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
          placeholder="exemplo@email.com"
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
          placeholder="CPF ou CNPJ"
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
          @blur="buscaCep(novoTutor.cep)"
          type="text"
          class="form-control"
          placeholder="00000-000"
        />
      </div>

      <div class="mb-3">
        <label
          for="rua"
          class="form-label"
        >
          Rua:
        </label>
        <input
          id="rua"
          v-model="novoTutor.rua"
          type="text"
          class="form-control"
          placeholder="Rua"
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
          placeholder="Número"
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
          placeholder="Bairro"
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
          placeholder="Cidade"
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
          placeholder="Estado"
        />
      </div>

      <button
        type="submit"
        class="btn btn-success mt-2"
      >
        Salvar
      </button>

    </form>
  </div>
</template>
