from fastapi import HTTPException
import httpx
from app.config.config import URL_BASE


async def getUsercorp(access: str):
    url = f"{URL_BASE}/usercorp"
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

