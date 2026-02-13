import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Adiciona o diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app


@pytest.fixture
def client():
    """Fixture para cliente de teste"""
    return TestClient(app)


def test_read_root(client):
    """Teste endpoint raiz"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["service"] == "python-bootstrap"


def test_health(client):
    """Teste health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_liveness(client):
    """Teste liveness probe"""
    response = client.get("/actuator/health/liveness")
    assert response.status_code == 200
    assert response.json()["status"] == "UP"


def test_readiness(client):
    """Teste readiness probe"""
    response = client.get("/actuator/health/readiness")
    assert response.status_code == 200
    assert response.json()["status"] == "UP"


def test_info(client):
    """Teste endpoint de informações da app"""
    response = client.get("/api/info")
    assert response.status_code == 200
    data = response.json()
    assert "app_name" in data
    assert "version" in data
    assert "timestamp" in data
    assert data["service"] == "python-bootstrap"
    assert data["status"] == "running"
