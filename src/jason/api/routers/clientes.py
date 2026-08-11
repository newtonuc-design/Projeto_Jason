from typing import Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/clientes", tags=["Clientes"])


class ClienteCreate(BaseModel):
    nome: str
    telefone: str


class Cliente(BaseModel):
    id: int
    nome: str
    telefone: Optional[str] = None


clientes = [
    {
        "id": 1,
        "nome": "João Silva"
    },
    {
        "id": 2,
        "nome": "Carlos Souza"
    }
]


@router.get("/", response_model=list[Cliente])
def listar_clientes():
    return [Cliente(**cliente) for cliente in clientes]


@router.get("/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for cliente in clientes:
        if cliente["id"] == id:
            return Cliente(**cliente)

    raise HTTPException(status_code=404, detail="Cliente não encontrado")


@router.post("", response_model=Cliente, status_code=status.HTTP_201_CREATED)
def cadastrar_cliente(cliente: ClienteCreate):
    novo_cliente = {
        "id": max((cliente["id"] for cliente in clientes), default=0) + 1,
        "nome": cliente.nome,
        "telefone": cliente.telefone,
    }
    clientes.append(novo_cliente)
    return Cliente(**novo_cliente)
