'
<script setup>
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { apiRequest } from '../services/api.js';

const route = useRoute();
const router = useRouter();

const tutor = ref(null);
const erroApi = ref('');

async function carregarTutor() {
  try {
    tutor.value = await apiRequest(`/tutores/${route.params.id}`);
    erroApi.value = '';
  } catch (erro) {
    console.error('Erro ao carregar os dados do tutor:', erro);
    erroApi.value = erro.message;
    tutor.value = null;
  }
}

async function salvarEdicao() {
  if (!tutor.value) {
    return;
  }

  try {
    await apiRequest(`/tutores/${route.params.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(tutor.value),
    });

    router.push({ name: 'tutores' });
  } catch (erro) {
    console.error('Erro ao salvar as alterações do tutor:', erro);
    erroApi.value = erro.message;
  }
}

onMounted(carregarTutor);
</script>

<template>
  <div v-if="tutor">
    <header class="mb-4">
      <h1 class="text-2xl font-bold">Editar Tutor</h1>
      <p class="mb-0 text-body-secondary">
        Atualize os dados do tutor.
      </p>
    </header>

    <form @submit.prevent="salvarEdicao">

      <h4>Dados Gerais</h4>

      <div class="row">

        <div class="col-md-4 mb-3">
          <label for="nome" class="form-label">Nome Completo:</label>
          <input
            id="nome"
            v-model="tutor.nome"
            type="text"
            class="form-control"
            required
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="cpfCnpj" class="form-label">CPF /CNPJ:</label>
          <input
            id="cpfCnpj"
            v-model="tutor.cpfCnpj"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="telefone" class="form-label">Telefone / WhatsApp:</label>
          <input
            id="telefone"
            v-model="tutor.telefone"
            type="tel"
            class="form-control"
            required
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="dataNascimento" class="form-label">Data de Nascimento:</label>
          <input
            id="dataNascimento"
            v-model="tutor.dataNascimento"
            type="date"
            class="form-control"
          />
        </div>

        <div class="col-md-8 mb-3">
          <label for="observacoes" class="form-label">Observações:</label>
          <textarea
            id="observacoes"
            v-model="tutor.observacoes"
            class="form-control"
            rows="2"
          ></textarea>
        </div>

      </div>

      <h4 class="mt-3">Endereço</h4>

      <div class="row">

        <div class="col-md-4 mb-3">
          <label for="cep" class="form-label">CEP:</label>
          <input
            id="cep"
            v-model="tutor.cep"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="rua" class="form-label">Rua:</label>
          <input
            id="rua"
            v-model="tutor.rua"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="numero" class="form-label">Número:</label>
          <input
            id="numero"
            v-model="tutor.numero"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="bairro" class="form-label">Bairro:</label>
          <input
            id="bairro"
            v-model="tutor.bairro"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="cidade" class="form-label">Cidade:</label>
          <input
            id="cidade"
            v-model="tutor.cidade"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-3">
          <label for="estado" class="form-label">Estado:</label>
          <input
            id="estado"
            v-model="tutor.estado"
            type="text"
            class="form-control"
          />
        </div>

      </div>

      <button type="submit" class="btn btn-success">
        Salvar alterações
      </button>

    </form>
  </div>

  <div v-else>
    <p v-if="erroApi" class="alert alert-danger" role="alert">
      {{ erroApi }}
    </p>
    <p v-else>Carregando tutor...</p>
  </div>
</template>
'
