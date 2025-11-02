# app/main.py
from fastapi import FastAPI
from app.routes import text_verify
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Misinformation Detection Suite",
    description="API backend for detecting misinformation in text using Gemini 2.0 Flash-Lite.",
    version="1.0.0"
)

app.include_router(text_verify.router)

@app.get("/")
def root():
    return {"message": "Misinformation Detection API is running 🚀"}
