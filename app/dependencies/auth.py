import os
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from fastapi import HTTPException

load_dotenv()
segurança = HTTPBearer()

def verificar_token(credenciais: HTTPBearer = Depends(segurança)):
                    
    if credenciais.credentials != os.getenv("TOKEN"):
        raise HTTPException(status_code=401, detail="acesso não autorizado")