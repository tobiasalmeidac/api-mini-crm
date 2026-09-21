from pydantic import BaseModel, EmailStr, ConfigDict, Field, field_validator
from typing import Optional
from enum import Enum
import uuid

TAMANHO_TELEFONE = 11
TAMANHO_CPF = 11
TAMANHO_CNPJ = 14

class TipoDocumento(str, Enum):
    CPF = "CPF"
    CNPJ = "CNPJ"

class StatusEnum(str, Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"

class ClienteCriar(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
        json_schema_extra={
            "exemplo"={
                "nome": "João da silva"
                "cpf": "11122233345"
                "email": "exemplo@email.com"
                "telefone": 5511911111111
                "status": "ATIVO"
            }
        }
    )

    nome: str = Field(
        min_length=1,
        max_length=200,
        description="nome do cliente"
    )
    documento: str = Field(
        description="Documento do cliente, CPF ou CNPJ, apenas números ou pontuação"
    )

    tipoDocumento: TipoDocumento = Field(
        description="Tipo do documento"
    )


    email: EmailStr
    # telefone: int
    # status: StatusEnum

    @field_validator("cpf", mode="before")
    @classmethod
    def organizar_cpf(cls, Value: str) -> str:
        if not isinstance(Value, str):
            raise ValueError("CPF deve ser enviado como texto.")
        
        CpfApenasDigitos = "".join(c for c in Value if c.isdigit())

        if len(CpfApenasDigitos) != TAMANHO_CPF:
            raise ValueError (f"CPF deve conter {TAMANHO_CPF} digitos.")

        return CpfApenasDigitos

    

    
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