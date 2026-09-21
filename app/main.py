from fastapi import FastAPI
from fastapi import Depends
from app.routers import clientes
from app.dependencies.auth import verificar_token

app = FastAPI(dependencies=[Depends(verificar_token)])

app.include_router(clientes.router)