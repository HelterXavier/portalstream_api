from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.usercorp import router as usercorp_router
from app.routes.implantation import router as implantation_router


app = FastAPI(title="Portal Steam API")

app.include_router(auth_router)
app.include_router(usercorp_router)
app.include_router(implantation_router)
