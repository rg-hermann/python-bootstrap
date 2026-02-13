from datetime import UTC, datetime

from fastapi import APIRouter

from app.config.config import settings

router = APIRouter(tags=["default"])


@router.get("/")
def read_root():
    """Endpoint raiz"""
    return {
        "message": "Hello from Python running on GitOps!",
        "service": "python-bootstrap",
    }


@router.get("/health")
def health():
    """Health check básico"""
    return {"status": "healthy", "service": "python-bootstrap"}


@router.get("/api/info")
def get_info():
    """Retorna informações sobre a aplicação (útil para testar deploy)"""
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "timestamp": datetime.now(UTC).isoformat(),
        "service": "python-bootstrap",
        "status": "running",
    }
