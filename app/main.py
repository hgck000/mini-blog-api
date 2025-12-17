from fastapi import FastAPI
from app.api.posts import router as posts_router

app = FastAPI(title="Mini Blog API")

app.include_router(posts_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
