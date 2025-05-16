from fastapi import APIRouter, Depends
from app.services.implantation import getImplantationTreeById, getImplatationInfo, getImplatationStatic, getImplatationLubricants
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
bearer_scheme = HTTPBearer()


@router.get("/implantation/mobile/tree")
async def get_implantation_tree_by_id(site: int, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    return await getImplantationTreeById(token, site)


@router.get("/implantation/mobile/info")
async def get_implantation_info(site: int, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    return await getImplatationInfo(token, site)


@router.get("/implantation/mobile/static")
async def get_implantation_info(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    return await getImplatationStatic(token)


@router.get("/implantation/mobile/static/get_lubricants")
async def get_implantation_lubricants(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    return await getImplatationLubricants(token)
