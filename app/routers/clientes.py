from fastapi import APIRouter
from fastapi import HTTPException
from typing import Optional
from app.schemas.cliente import ClienteCriar, ClienteAtualizar, StatusEnum

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

clientes = []
proximo_id = 1

@router.get("")
#ou seja: "quando chegar uma requisição GET na rota /clientes, execute a funçao abaixo"
def listar_clientes(nome: Optional[str] = None, status: Optional[StatusEnum] = None, cpf: Optional[str] = None):
    resultado = clientes
    if nome is not None:
        #list comprehension
        resultado = [c for c in resultado if nome.lower() in c["nome"].lower()]

    if status is not None:
        resultado = [c for c in resultado if c["status"] == status]

    if cpf is not None:
        resultado = [c for c in resultado if str(c["cpf"]) == cpf]

    return resultado
    

@router.get("/{id}")
def buscar_cliente(id: int):
    for c in clientes:
        if c["id"] == id:
            return c
    raise HTTPException(status_code=404, detail="cliente não encontrado")

@router.post("", status_code=201)
def criar_cliente(dados: ClienteCriar):
    global proximo_id
    #condição se tornou desnecessária após a adoção do EmailStr
    # if "@" not in dados.email or "." not in dados.email:
        # raise HTTPException(status_code=400, detail="e-mail inválido")
    
    cliente = {"id": proximo_id, "nome": dados.nome, "cpf": dados.cpf, "email": dados.email, "telefone": dados.telefone, "status": dados.status}
    clientes.append(cliente)
    proximo_id += 1
    return cliente

@router.patch("/{id}")
def atualizar_cliente(id: int, dados: ClienteAtualizar):
    for c in clientes:
        if c["id"] == id:
            if dados.nome is not None:
                c["nome"] = dados.nome
            if dados.cpf is not None:
                c["cpf"] = dados.cpf
            if dados.email is not None:
                c["email"] = dados.email
            if dados.telefone is not None:
                c["telefone"] = dados.telefone
            if dados.status is not None:
                c["status"] = dados.status

            return c
    raise HTTPException(status_code=404, detail="cliente não encontrado")

@router.delete("/{id}")
def remover_cliente(id: int):
    for i, c in enumerate(clientes):
        if c["id"] == id:
            clientes.pop(i)
            return {"mensagem": "cliente removido"}
    raise HTTPException(status_code=404, detail="cliente não encontrado")