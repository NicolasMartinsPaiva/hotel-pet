# main.py
from fastapi import FastAPI, HTTPException
from database import tutores_db, pets_db

app = FastAPI(title="API Hotel Pet - Desenvolvimento Web II", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Hotel Pet!"}

# 1. Endpoint: listartutores
@app.get("/tutores")
def listar_tutores():
    return tutores_db

# 2. Endpoint: consultartutor (por id)
@app.get("/tutores/{tutor_id}")
def consultar_tutor(tutor_id: int):
    for tutor in tutores_db:
        if tutor["id"] == tutor_id:
            return tutor
    raise HTTPException(status_code=404, detail="Tutor não encontrado")

# 3. Endpoint: listarpets
@app.get("/pets")
def listar_pets():
    return pets_db

# 4. Endpoint: consultarpet (por id)
@app.get("/pets/{pet_id}")
def consultar_pet(pet_id: int):
    for pet in pets_db:
        if pet["id"] == pet_id:
            return pet
    raise HTTPException(status_code=404, detail="Pet não encontrado")
