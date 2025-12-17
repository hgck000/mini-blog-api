from fastapi import FastAPI
import app.models  # noqa: F401

from app.api.posts import router as posts_router
from app.api.comments import router as comments_router

app = FastAPI(title="Mini Blog API")
app.include_router(posts_router)
app.include_router(comments_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
