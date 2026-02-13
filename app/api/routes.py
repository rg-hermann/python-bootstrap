from fastapi import APIRouter

router = APIRouter(tags=["default"])


@router.get("/")
def read_root():
    """Endpoint raiz"""
    return {
        "message": "Hello from Python running on GitOps!",
        "service": "python-bootstrap"
    }


@router.get("/health")
def health():
    """Health check básico"""
    return {
        "status": "healthy",
        "service": "python-bootstrap"
    }
