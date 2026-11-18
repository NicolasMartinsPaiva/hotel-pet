<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const API_URL = 'http://localhost:3000';

const pet = ref(null);
const tutor = ref({ nome: 'Tutor não encontrado' });

async function carregarPet() {
  try {
    const respostaPet = await fetch(`${API_URL}/pets/${route.params.id}`);

    if (!respostaPet.ok) {
      console.log('Opss, pet não encontrado');
      pet.value = null;
      return;
    }

    pet.value = await respostaPet.json();

    if (pet.value && pet.value.tutorId) {
      const respostaTutor = await fetch(
        `${API_URL}/tutores/${pet.value.tutorId}`,
      );
      tutor.value = respostaTutor.ok
        ? await respostaTutor.json()
        : { nome: 'Tutor não encontrado' };
    }
  } catch (erro) {
    console.log('Erro ao carregar os dados do pet e do tutor:', erro);
    pet.value = null;
    tutor.value = { nome: 'Tutor não encontrado' };
  }
}

onMounted(carregarPet);
</script>

<template>
  <div v-if="pet">
    <p>Nome: {{ pet.nome }}</p>
    <p>Espécie: {{ pet.especie }}</p>
    <p>Tutor: {{ tutor?.nome ?? 'Tutor não encontrado' }}</p>
  </div>

  <div v-else>Carregando pet...</div>
</template>
