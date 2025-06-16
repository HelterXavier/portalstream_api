from motor.motor_asyncio import AsyncIOMotorClient
from app.config.config import MONGODB_URI

client = AsyncIOMotorClient(MONGODB_URI)

db = client["db_portalstream"]

docs_collections = db["docs"]
