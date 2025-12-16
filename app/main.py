from fastapi import FastAPI

app = FastAPI(title="Mini Blog API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
