from fastapi import FastAPI
import requests

app = FastAPI()
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
def ask_ai(question):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": question}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

@app.get("/")
def home():
    return {"message": "Welcome to my AI API!"}

@app.post("/ask")
def ask(question: str):
    answer = ask_ai(question)
    return {"question": question, "answer": answer}