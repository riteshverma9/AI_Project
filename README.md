# AI_Project

## Project Overview

AI_Project is an AI-powered FastAPI application scaffolded by
`init_ai_project.py`. It ships with a chat-style web UI and a backend
integration for **NVIDIA**.

## Installation

```bash
git clone <your-repo-url>
cd AI_Project
```

## Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and fill in your API key:

```bash
cp .env.example .env
```

## Running

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000` in your browser.

## Docker

Build and run with Docker:

```bash
docker build -t ai_project .
docker run -p 8000:8000 --env-file .env ai_project
```

Or with Docker Compose:

```bash
docker-compose up --build
```

## Kubernetes

Deploy to a Kubernetes cluster:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
```

## Folder Structure

```
AI_Project/
+-- app/
|   +-- __init__.py
|   +-- ai.py
|   +-- config.py
|   +-- routes.py
|   +-- models.py
|   +-- logger.py
|   +-- utils.py
|   +-- services.py
+-- static/
+-- templates/
+-- tests/
+-- kubernetes/
+-- docs/
+-- logs/
+-- .env.example
+-- .gitignore
+-- requirements.txt
+-- README.md
+-- Dockerfile
+-- docker-compose.yml
+-- main.py
+-- LICENSE
+-- pyproject.toml
```

## API Documentation

Once running, interactive API docs are available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### `POST /api/chat`

Request body:

```json
{
  "message": "Hello, how are you?"
}
```

Response body:

```json
{
  "reply": "I'm doing great, thanks for asking!"
}
```

## Future Roadmap

- [ ] Add authentication (JWT / OAuth2)
- [ ] Add streaming responses
- [ ] Add conversation history persistence
- [ ] Add rate limiting
- [ ] Add CI/CD pipeline
- [ ] Add automated test coverage badge
