from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum




class StatusEnum(str, Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"

class ClienteCriar(BaseModel):

    nome: str
    cpf: str
    email: EmailStr
    telefone: int
    status: StatusEnum
    
class ClienteAtualizar(BaseModel):
        
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[int] = None
    status: Optional[StatusEnum] = None

class ClienteResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    email: EmailStr
    telefone: int
    status: StatusEnum