from fastapi import HTTPException
import httpx
from app.config.config import URL_BASE


async def authentication(username: str, password: str):
    url = f"{URL_BASE}/token"
    data = {
        "username": username,
        "password": password
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(url, json=data)
            res.raise_for_status()
            return res.json()
    except Exception as err:
        raise HTTPException(
            status_code=err.response.status_code,
            detail=err.response.json()
        )


async def varify_token(access: str):
    url = f"{URL_BASE}/token/verify"
    data = {
        "token": access,
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(url, json=data)
            res.raise_for_status()
            return res.json()
    except Exception as err:
        raise HTTPException(
            status_code=err.response.status_code,
            detail=err.response.json()
        )


async def refresh_token(refresh: str):
    url = f"{URL_BASE}/token/refresh"
    data = {
        "refresh": refresh,
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(url, json=data)
            res.raise_for_status()
            return res.json()
    except Exception as err:
        raise HTTPException(
            status_code=err.response.status_code,
            detail=err.response.json()
        )
