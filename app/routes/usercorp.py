from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.usercorp_service import getUsercorp

router = APIRouter()
bearer_scheme = HTTPBearer()


@router.get("/usercorp")
async def usercorp(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    return await getUsercorp(token)
