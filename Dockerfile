# Build multi-stage para manter a imagem leve
FROM python:3.12-slim

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Expõe a porta que o seu template Helm já monitora
EXPOSE 8080

# Comando para rodar a app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]