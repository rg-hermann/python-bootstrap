# Guia de Contribuição

Obrigado por se interessar em contribuir! Este documento fornece diretrizes e instruções para contribuir com este projeto.

## 📋 Pré-requisitos

- Python 3.12+
- Git
- Virtual Environment

## 🚀 Como Contribuir

### 1. Fork e Clone

```bash
git clone https://github.com/rg-hermann/python-bootstrap.git
cd python-bootstrap
```

### 2. Criar Branch de Feature

```bash
git checkout -b feature/sua-feature
```

### 3. Setup Ambiente

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 4. Fazer Suas Mudanças

```bash
# Editar código...
```

### 5. Testes

```bash
# Rodar todos os testes
pytest tests/ -v

# Rodar com cobertura
pytest tests/ --cov=app --cov-report=html
```

### 6. Code Quality

```bash
# Format com Black
black app tests

# Sort imports com isort
isort app tests

# Lint com Flake8
flake8 app --max-line-length=120

# Type checking com mypy (opcional)
mypy app
```

Ou de uma vez:

```bash
./scripts/lint.sh  # Se disponível
```

### 7. Commit e Push

```bash
git add .
git commit -m "feat: descrição clara da mudança"
git push origin feature/sua-feature
```

### 8. Pull Request

- Abra um PR contra `main` ou `develop`
- Descreva claramente as mudanças
- Garanta que os testes passam
- Aguarde review

## 📝 Convenções de Commit

Utilizamos [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: Nova feature
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação (sem mudança de lógica)
- `refactor`: Refatoração de código
- `perf`: Melhoria de performance
- `test`: Adição/modificação de testes
- `chore`: Tarefas (deps, build, etc)

### Exemplos
```
feat(api): adicionar novo endpoint de health check
fix(config): corrigir carregamento de variáveis
docs: atualizar README com instruções de setup
chore(deps): atualizar FastAPI para 0.105.0
```

## 🧪 Padrões de Teste

- Testes devem estar em `tests/`
- Nomear arquivos como `test_*.py`
- Funções de teste começam com `test_`
- Usar fixtures do pytest

Exemplo:
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
```

## 🐛 Reportar Bugs

Use GitHub Issues com o template fornecido:

- Descreva o bug claramente
- Passos para reproduzir
- Comportamento esperado vs atual
- Ambiente (Python, SO, etc)

## 💡 Sugerir Features

Use GitHub Discussions ou Issues com o label `enhancement`.

## 📚 Documentação

- Docstrings em Python (Google style)
- README.md para instruções gerais
- Comentários para lógica complexa

Exemplo:
```python
def health_check() -> dict:
    """Verifica se a aplicação está saudável.
    
    Returns:
        dict: Status de saúde da aplicação
    """
    return {"status": "UP"}
```

## 🔒 Segurança

Se encontrar uma vulnerabilidade:
- **NÃO** abra issue pública
- Envie email para security@example.com
- Descreva a vulnerabilidade

## 📞 Dúvidas?

- Abra uma Discussion
- Envie um email
- Verifique o README.md

---

**Obrigado por contribuir!** 🎉
