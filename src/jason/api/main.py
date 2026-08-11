from fastapi import FastAPI

from jason.api.routers.root import router as root_router
from jason.api.routers.clientes import router as clientes_router

app = FastAPI(
    title="Jason Barber API",
    version="0.1.0",
    description="Primeira API do Projeto Jason"
)

app.include_router(root_router)
app.include_router(clientes_router)

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
