const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:3000';

export async function apiRequest(path, options = {}) {
  const resposta = await fetch(`${API_URL}${path}`, options);

  if (!resposta.ok) {
    throw new Error(`Erro na API: ${resposta.status} ${resposta.statusText}`);
  }

  if (resposta.status === 204) {
    return null;
  }

  return resposta.json();
}
