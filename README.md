# Alyssa Johnson | Software Engineering Portfolio

Software engineering portfolio focused on Python, API development, automated testing, Docker, CI/CD, and AI code quality.

## Featured project: Code Review Risk API

This repository contains a compact, production-style Python service that analyzes a proposed multi-file code change and returns deterministic quality signals. It demonstrates layered application design without exposing proprietary or private work.

### Engineering highlights

- FastAPI HTTP service with validated Pydantic request/response models
- Python AST parsing for syntax-aware analysis
- Cross-file import/dependency inspection
- Deterministic change-risk scoring and structured findings
- Unit and API integration tests with pytest
- Docker containerization and Docker Compose
- GitHub Actions CI for tests and container builds
- Clear separation between API, domain models, analysis, and service logic

## Run locally

```bash
python -m venv .venv
pip install -e ".[dev]"
pytest
uvicorn portfolio_api.api:app --reload
```

Open `http://localhost:8000/docs` for the generated API documentation.

## Docker

```bash
docker compose up --build
```

## Example request

```json
{
  "change_id": "pr-104",
  "files": {
    "src/api.py": "from app.service import run\nprint('debug')\n",
    "src/service.py": "def run():\n    return True\n"
  }
}
```

The API reports file counts, dependency edges, syntax problems, debug statements, and a bounded risk score.

## About me

I work at the intersection of software engineering, AI code quality, technical analysis, and model evaluation. My professional work includes analyzing code changes across Python, TypeScript, JavaScript, C#, and C++; tracing dependencies and failure modes; validating technical claims against source evidence and tests; and producing clear developer-facing documentation.
