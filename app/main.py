from fastapi import FastAPI
from app.config.config import settings
from app.api.routes import router

# Criar aplicação FastAPI
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

# Incluir rotas
app.include_router(router)


# Health checks compatíveis com Kubernetes Probes
@app.get("/actuator/health/liveness")
def liveness():
    """Liveness probe: a app está em execução?"""
    return {"status": "UP"}


@app.get("/actuator/health/readiness")
def readiness():
    """Readiness probe: a app está pronta para receber tráfego?"""
    # Aqui você verificaria conexões com DB, Redis, etc.
    return {"status": "UP"}