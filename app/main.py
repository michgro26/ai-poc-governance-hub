from fastapi import FastAPI

from app.engine import evaluate_poc
from app.models import PocEvaluation, PocInput, PocRecord
from app.repository import repository

app = FastAPI(
    title="AI PoC Governance Hub",
    description="Demo API do oceny i koordynacji PoC AI / Big Data.",
    version="1.0.0",
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/pocs", response_model=list[PocRecord])
def list_pocs() -> list[PocRecord]:
    return repository.list_all()


@app.post("/pocs/evaluate", response_model=PocEvaluation)
def evaluate(payload: PocInput) -> PocEvaluation:
    return evaluate_poc(payload)


@app.post("/pocs", response_model=PocRecord)
def create_poc(payload: PocInput) -> PocRecord:
    return repository.add(payload)
