
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const API_URL = 'http://localhost:3000';
const router = useRouter();

const novoTutor = ref({
  nome: '',
  cpfCnpj: '',
  telefone: '',
  dataNascimento: '',
  observacoes: '',
  cep: '',
  rua: '',
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
      console.log('Erro ao cadastrar tutor');
      return;
    }

    router.push({ name: 'tutores' });

  } catch (erro) {
    console.log('Erro ao salvar o novo tutor:', erro);
  }
}
</script>

<template>
  <div>
    <header class="mb-4">
      <h1 class="text-2xl font-bold">Cadastrar Tutores</h1>
      <p class="text-body-secondary mb-0">
        Cadastro de Tutores no sistema.
      </p>
    </header>

    <form @submit.prevent="salvarTutor">

      <h4>Dados Gerais</h4>

      <div class="row">

        <div class="col-md-4 mb-2">
          <label for="nome" class="form-label">
            Nome Completo:
          </label>
          <input
            id="nome"
            v-model="novoTutor.nome"
            type="text"
            class="form-control"
            required
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="cpfCnpj" class="form-label">
            CPF /CNPJ:
          </label>
          <input
            id="cpfCnpj"
            v-model="novoTutor.cpfCnpj"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="telefone" class="form-label">
            Telefone / WhatsApp:
          </label>
          <input
            id="telefone"
            v-model="novoTutor.telefone"
            type="tel"
            class="form-control"
            required
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="dataNascimento" class="form-label">
            Data de Nascimento:
          </label>
          <input
            id="dataNascimento"
            v-model="novoTutor.dataNascimento"
            type="date"
            class="form-control"
          />
        </div>

        <div class="col-md-8 mb-2">
          <label for="observacoes" class="form-label">
            Observações:
          </label>
          <textarea
            id="observacoes"
            v-model="novoTutor.observacoes"
            class="form-control"
            rows="2"
          ></textarea>
        </div>

      </div>

      <h4 class="mt-3">Endereço</h4>

      <div class="row">

        <div class="col-md-4 mb-2">
          <label for="cep" class="form-label">CEP:</label>
          <input
            id="cep"
            v-model="novoTutor.cep"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="rua" class="form-label">Rua:</label>
          <input
            id="rua"
            v-model="novoTutor.rua"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="numero" class="form-label">Número:</label>
          <input
            id="numero"
            v-model="novoTutor.numero"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="bairro" class="form-label">Bairro:</label>
          <input
            id="bairro"
            v-model="novoTutor.bairro"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="cidade" class="form-label">Cidade:</label>
          <input
            id="cidade"
            v-model="novoTutor.cidade"
            type="text"
            class="form-control"
          />
        </div>

        <div class="col-md-4 mb-2">
          <label for="estado" class="form-label">Estado:</label>
          <input
            id="estado"
            v-model="novoTutor.estado"
            type="text"
            class="form-control"
          />
        </div>

      </div>

      <button type="submit" class="btn btn-success mt-2">
        Salvar Tutor
      </button>

    </form>
  </div>
</template>
