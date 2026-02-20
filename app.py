from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI running on Azure WebApp 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}
