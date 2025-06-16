from fastapi import APIRouter, Depends

from app.middleware.auth import authenticate_user
from app.schemas.docs_schema import Dto
from app.services.doc_service import (
    create_docs_services,
    delete_doc_by_id,
    load_doc_by_id,
    load_docs_services,
    update_doc_by_id,
)

router = APIRouter()


@router.post("/document")
async def create_docs(createDocs: Dto, token: str = Depends(authenticate_user)):
    return await create_docs_services(createDocs, token)


@router.get("/documents")
async def list_docs(token: str = Depends(authenticate_user)):
    return await load_docs_services(token)


@router.get("/document")
async def show_docs_by_id(_id: str, token: str = Depends(authenticate_user)):
    return await load_doc_by_id(_id, token)


@router.put("/document")
async def update_docs(_id: str, dto: Dto, token: str = Depends(authenticate_user)):
    return await update_doc_by_id(_id, dto, token)


@router.delete("/document")
async def delete_doc(_id: str, token: str = Depends(authenticate_user)):
    return await delete_doc_by_id(_id, token)
