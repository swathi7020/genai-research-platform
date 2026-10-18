from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, File, Form, UploadFile
from pydantic import BaseModel

from app.research.engine import ResearchEngine
from app.agents.crew import create_research_crew


router = APIRouter(
    prefix="/research",
    tags=["Research"]
)


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_PDF_PATH = (
    PROJECT_ROOT / "data" / "research_paper.pdf"
)

UPLOAD_DIR = (
    PROJECT_ROOT / "data" / "uploads"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ---------------------------------------------------------
# Existing Research Engine
# ---------------------------------------------------------

research_engine = ResearchEngine(
    pdf_path=str(DEFAULT_PDF_PATH)
)


# ---------------------------------------------------------
# Request models
# ---------------------------------------------------------

class ResearchQuery(BaseModel):

    question: str

    top_k: int = 3

    web_results: int = 3


class AgentResearchQuery(BaseModel):

    question: str


# ---------------------------------------------------------
# Existing RAG + Tavily endpoint
# ---------------------------------------------------------

@router.post("/ask")
def ask_research_question(
    request: ResearchQuery
):

    result = research_engine.research(
        question=request.question,
        top_k=request.top_k,
        web_results=request.web_results
    )

    return {
        "question": result["question"],

        "answer": result["answer"],

        "document_sources": [
            {
                "distance": source["distance"],
                "content": source["document"]
            }
            for source in result["document_sources"]
        ],

        "web_sources": [
            {
                "title": source["title"],
                "url": source["url"],
                "content": source["content"],
                "score": source["score"]
            }
            for source in result["web_sources"]
        ]
    }


# ---------------------------------------------------------
# Existing CrewAI endpoint
# ---------------------------------------------------------

@router.post("/agents")
def agent_research(
    request: AgentResearchQuery
):

    crew = create_research_crew(
        question=request.question,
        pdf_path=str(DEFAULT_PDF_PATH)
    )

    result = crew.kickoff()

    return {
        "question": request.question,
        "answer": str(result)
    }


# ---------------------------------------------------------
# NEW:
# Upload PDF + Multi-Agent Research
# ---------------------------------------------------------

@router.post("/upload-and-ask")
def upload_and_ask(
    question: str = Form(...),
    file: UploadFile = File(...)
):

    # -----------------------------------------------------
    # Validate file
    # -----------------------------------------------------

    if not file.filename:
        raise ValueError(
            "No file was provided."
        )

    original_filename = Path(
        file.filename
    ).name

    if not original_filename.lower().endswith(".pdf"):
        raise ValueError(
            "Only PDF files are supported."
        )

    # -----------------------------------------------------
    # Create unique filename
    # -----------------------------------------------------

    unique_filename = (
        f"{uuid.uuid4().hex}_{original_filename}"
    )

    saved_path = UPLOAD_DIR / unique_filename

    # -----------------------------------------------------
    # Save uploaded PDF
    # -----------------------------------------------------

    with saved_path.open("wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # -----------------------------------------------------
    # Run CrewAI
    # -----------------------------------------------------

    crew = create_research_crew(
        question=question,
        pdf_path=str(saved_path)
    )

    result = crew.kickoff()

    # -----------------------------------------------------
    # Return result
    # -----------------------------------------------------

    return {
        "question": question,

        "filename": original_filename,

        "answer": str(result)
    }