# NOaaS — No as a Service

A joke API that responds to every question with a creative, sarcastic "NO". Powered by a local LLM via Ollama.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (recommended)
- Or: Python 3, [Ollama](https://ollama.ai), and `pip`

## Quick Start (Docker)

```bash
docker build -t noaas .
docker run -p 8000:8000 noaas
```

The container starts Ollama, pulls the model, and launches the API automatically.

## Local Setup (without Docker)

```bash
# 1. Install and start Ollama
ollama serve

# 2. Pull the model
ollama pull qwen2.5:0.5b

# 3. Install Python dependencies
pip install fastapi uvicorn httpx

# 4. Run the API
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Usage

Ask a question via GET or POST — the answer will always be no.

**GET**
```bash
curl "http://localhost:8000/ask?q=Can+you+help+me"
```

**POST**
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Will this ever say yes?"}'
```

**Response**
```json
{
  "question": "Will this ever say yes?",
  "answer": "Absolutely not. Not in this lifetime, not in any parallel universe..."
}
```

Interactive API docs are available at [http://localhost:8000/docs](http://localhost:8000/docs).

## Configuration

All configuration lives in `app.py`:

| Variable        | Default                                    | Description               |
|-----------------|--------------------------------------------|---------------------------|
| `OLLAMA_URL`    | `http://localhost:11434/api/generate`      | Ollama API endpoint       |
| `MODEL`         | `qwen2.5:0.5b`                             | LLM model to use          |
| `SYSTEM_PROMPT` | *(sarcasm instructions)*                   | Controls response tone    |

## Inspiration

Inspired by [no-as-a-service](https://github.com/hotheadhacker/no-as-a-service).

## Stack

- [FastAPI](https://fastapi.tiangolo.com/) — async REST API
- [Ollama](https://ollama.ai/) — local LLM inference
- [Qwen2.5 0.5b](https://ollama.com/library/qwen2.5) — lightweight language model
- [httpx](https://www.python-httpx.org/) — async HTTP client
