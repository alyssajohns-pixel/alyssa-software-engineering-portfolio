from fastapi import FastAPI

from .models import ChangeReport, ChangeRequest
from .service import analyze_change

app = FastAPI(
    title="Code Review Risk API",
    description="Deterministic code-change analysis for a software engineering portfolio.",
    version="1.0.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze", response_model=ChangeReport)
def analyze(request: ChangeRequest) -> ChangeReport:
    return analyze_change(request)
