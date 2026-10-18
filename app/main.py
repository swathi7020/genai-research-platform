from fastapi import FastAPI

from app.api.users import router as users_router
from app.api.research import router as research_router


app = FastAPI(
    title="GenAI Research Intelligence Platform",
    description=(
        "Multi-agent RAG platform for intelligent "
        "research and document analysis"
    ),
    version="1.0.0"
)


app.include_router(users_router)

app.include_router(research_router)


@app.get("/")
def root():

    return {
        "message": "GenAI Research Intelligence Platform is running!"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }