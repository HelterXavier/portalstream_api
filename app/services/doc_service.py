from fastapi import HTTPException, Response
from app.db.mongo import docs_collections
from bson import ObjectId


async def create_docs_services(dto, token: str):
    formData = dto.dict()

    try:
        await docs_collections.insert_one(formData)
        return {
            "message": "Document successfully created!",
        }
    except Exception as err:
        raise HTTPException(err)


async def load_docs_services(token: str):
    try:
        documents = docs_collections.find()
        res = await documents.to_list(length=100)
        for doc in res:
            doc["_id"] = str(doc["_id"])
        return res
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


async def load_doc_by_id(_id: str, token: str):
    if not ObjectId.is_valid(_id):
        raise HTTPException(status_code=400, detail="Document not found")

    try:
        doc = await docs_collections.find_one({"_id": ObjectId(_id)})
        doc["_id"] = str(doc["_id"])
        return doc
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(err)}")


async def update_doc_by_id(_id: str, dto, token: str):
    await load_doc_by_id(_id)
    try:
        formData = dto.dict()
        await docs_collections.update_one({"_id": ObjectId(_id)}, {"$set": formData})
        updateDoc = await load_doc_by_id(_id)
        return updateDoc
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(err)}")


async def delete_doc_by_id(_id: str, token: str):
    await load_doc_by_id(_id)

    try:
        await docs_collections.delete_one({"_id": ObjectId(_id)})
        return Response(status_code=200)
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(err)}")
