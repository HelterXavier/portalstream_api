from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.auth_service import varify_token

bearer_scheme = HTTPBearer()


async def authenticate_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    token = credentials.credentials

    try:
        await varify_token(token)
        return token
    except HTTPException:
        raise HTTPException(
            status_code=401, detail="Token inválido ou expirado")
