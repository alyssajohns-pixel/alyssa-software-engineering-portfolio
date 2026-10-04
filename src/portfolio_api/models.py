from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class ChangeRequest(BaseModel):
    change_id: str = Field(min_length=1)
    files: dict[str, str]

    @field_validator("files")
    @classmethod
    def require_files(cls, value: dict[str, str]) -> dict[str, str]:
        if not value:
            raise ValueError("at least one file is required")
        return value


class Finding(BaseModel):
    kind: str
    path: str
    message: str


class ChangeReport(BaseModel):
    change_id: str
    file_count: int
    python_file_count: int
    dependency_edges: int
    risk_score: int = Field(ge=0, le=100)
    findings: list[Finding]
