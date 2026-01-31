from fastapi import FastAPI
from transformers import pipeline

app = FastAPI( title="FastAPI - mlops-llmops", description="API de ejemplo", version="1.0")

sentiment_pipeline = pipeline("sentiment-analysis")
summarization_pipeline = pipeline("summarization")

@app.get("/saluda")
def saluda():
    return {"mensaje": "Hola desde FastAPI"}

@app.get("/despido")
def despido():
    return {"mensaje": "Adiós desde FastAPI"}

@app.get("/status")
def status():
    return {"status": "ok"}


@app.get("/sentiment")
def sentiment(texto: str):
    result = sentiment_pipeline(texto)
    return {"resultado": result}

@app.get("/summarize")
def summarize(texto: str):
    result = summarization_pipeline(texto,max_length=50,min_length=25,do_sample=False)
    return {"resumen": result}
