from fastapi import APIRouter
from app.services.auth_service import authentication, refresh_token, varify_token
from app.schemas.auth import Credential, AuthToken, RefreshToken, AccessToken, VerifyToken

router = APIRouter()


@router.post("/token", response_model=AuthToken)
async def login(credential: Credential):
    return await authentication(credential.username, credential.password)


@router.post("/token/verify")
async def verify(verifyToken: VerifyToken):
    await varify_token(verifyToken.token)
    return {}


@router.post("/token/refresh", response_model=AccessToken)
async def refresh_token_endpoint(refreshToken: RefreshToken):
    return await refresh_token(refreshToken.refresh)
