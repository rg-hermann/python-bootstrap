# 🐍 Python Bootstrap

Microserviço em **Python 3.12** utilizando **FastAPI**, parte do ecossistema GitOps Java/Python. 

## 🚀 Tecnologias
* **Linguagem:** Python 3.12
* **Framework:** FastAPI (Uvicorn)
* **Health Checks:** Compatíveis com Spring Actuator (`/actuator/health`)
* **Deploy:** ArgoCD + Helm (k8s-helm-templates)

## 🏗️ Integração GitOps
Este repositório fornece a imagem Docker que é consumida pelo repositório [python-bootstrap-infra](LINK_PARA_SEU_REPO_INFRA).

* **Porta Interna:** 8080 (Padronizada para o template Helm)
* **Imagem:** `ghcr.io/rg-hermann/python-bootstrap`

## 🛠️ Como executar localmente

### Pré-requisitos
- Python 3.12+
- pip/venv

### Passos

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/rg-hermann/python-bootstrap.git
   cd python-bootstrap
   ```

2. **Criar e ativar ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   .\venv\Scripts\activate   # Windows
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Rodar a aplicação:**
   ```bash
   python -m uvicorn app.main:app --host 0.0.0.0 --port 8081 --reload
   ```
   
   A app estará disponível em: `http://localhost:8081`

5. **Testar os endpoints:**
   ```bash
   # Endpoint raiz
   curl http://localhost:8081/
   
   # Liveness probe (Kubernetes)
   curl http://localhost:8081/actuator/health/liveness
   
   # Readiness probe (Kubernetes)
   curl http://localhost:8081/actuator/health/readiness
   
   # Health check customizado
   curl http://localhost:8081/health
   ```

   **Respostas esperadas:**
   ```json
   {"message": "Hello from Python running on GitOps!", "service": "python-bootstrap"}
   {"status": "UP"}
   ```

## 📚 Estrutura do Projeto

```
python-bootstrap/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Aplicação FastAPI
│   ├── api/
│   │   └── routes.py          # Rotas da API
│   └── config/
│       └── config.py          # Configurações (Pydantic)
├── tests/
├── Dockerfile
├── requirements.txt
└── README.MD
```

## 🐳 Docker

### Build local

```bash
docker build -t python-bootstrap:latest .
```

### Rodar container

```bash
docker run -p 8080:8080 python-bootstrap:latest
```

Acesse em: `http://localhost:8080`

## 🔗 Integração GitOps

Este repositório é consumido pelo [python-bootstrap-infra](https://github.com/rg-hermann/python-bootstrap-infra):

- **Imagem:** `ghcr.io/rg-hermann/python-bootstrap`
- **Porta:** 8080 (padrão do template Helm)
- **Deploy:** ArgoCD sincroniza automaticamente as mudanças

### Fluxo CI/CD
1. Código é commitado neste repo
2. GitHub Actions faz build da imagem Docker
3. Push para GHCR (`ghcr.io/rg-hermann/python-bootstrap`)
4. ArgoCD detecta nova imagem e sincroniza em K8s

## 🧪 Testes

```bash
python -m pytest tests/
```

## 📝 Variáveis de Ambiente

Configure via `.env`:
```ini
DEBUG=false
APP_NAME=Python Bootstrap Service
```

## 🚀 Deploy em Kubernetes

Veja instruções no repositório [python-bootstrap-infra](https://github.com/rg-hermann/python-bootstrap-infra).

## 📄 Licença

MIT