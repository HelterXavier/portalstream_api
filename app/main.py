from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.usercorp import router as usercorp_router
from app.routes.implantation import router as implantation_router
from app.routes.docs import router as docs_router

from app.db.mongo import client

app = FastAPI(title="Portal Steam API")


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(usercorp_router)
app.include_router(implantation_router)
app.include_router(docs_router)


@app.on_event("startup")
async def start_event():
    try:
        await client.admin.command("ping")
        print("✅ Connect to database!")
    except Exception as err:
        pass
        print("❌ Fail to connect to database", err)


@app.on_event("shutdown")
async def shutdown_event():
    client.close()
    print("🔌 Connection with MongoDB closed.")
