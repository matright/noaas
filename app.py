from fastapi import FastAPI, Query
from pydantic import BaseModel
import httpx

app = FastAPI(title="NOaaS")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:0.5b"
SYSTEM_PROMPT = (
    "You are an insufferably sarcastic assistant whose only answer is NO. "
    "No matter what the user asks, you refuse — but you do it with maximum sarcasm, "
    "wit, and creative flair. Each refusal should be unique and drip with irony. "
    "Never say yes. Never help. Just say no, sarcastically."
)


class Question(BaseModel):
    question: str


async def ask_ollama(question: str) -> str:
    payload = {
        "model": MODEL,
        "system": SYSTEM_PROMPT,
        "prompt": f'The user asks: "{question}". Respond with a sarcastic NO.',
        "stream": False,
    }
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()["response"]


@app.post("/ask")
async def ask_post(body: Question):
    answer = await ask_ollama(body.question)
    return {"question": body.question, "answer": answer}


@app.get("/ask")
async def ask_get(q: str = Query(..., description="Your question")):
    answer = await ask_ollama(q)
    return {"question": q, "answer": answer}
