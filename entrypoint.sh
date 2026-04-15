#!/bin/bash
set -e

echo "Starting Ollama server..."
ollama serve &
OLLAMA_PID=$!

echo "Waiting for Ollama to be ready..."
until curl -sf http://localhost:11434/api/tags > /dev/null 2>&1; do
  sleep 5
done

echo "Pulling qwen2.5 model..."
ollama pull qwen2.5:0.5b

echo "Starting sarcastic NO API on port 8000..."
exec uvicorn app:app --host 0.0.0.0 --port 8000
