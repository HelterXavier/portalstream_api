import httpx
from app.config.config import URL_BASE
from fastapi import HTTPException


async def getImplantationTreeById(access: str, site: int):
    url = f"{URL_BASE}/implantation/mobile/tree"
    headers = {
        "Authorization": f"Bearer {access}"
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, params={"site": site}, headers=headers)
            res.raise_for_status()
            return res.json()
    except Exception as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.json()
        )


async def getImplatationInfo(access: str, site: int):
    url = f"{URL_BASE}/implantation/mobile/info"
    headers = {
        "Authorization": f"Bearer {access}"
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, params={"site": site}, headers=headers)
            res.raise_for_status()
            return res.json()
    except Exception as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.json()
        )


async def getImplatationStatic(access: str):
    url = f"{URL_BASE}/implantation/mobile/static"
    headers = {
        "Authorization": f"Bearer {access}"
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, headers=headers)
            res.raise_for_status()
            return res.json()
    except Exception as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.json()
        )


async def getImplatationLubricants(access: str):
    url = f"{URL_BASE}/implantation/mobile/static"
    headers = {
        "Authorization": f"Bearer {access}"
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, headers=headers)
            res.raise_for_status()
            return res.json()
    except Exception as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.json()
        )
