from __future__ import annotations

from .analysis import analyze_python
from .models import ChangeReport, ChangeRequest, Finding


def analyze_change(request: ChangeRequest) -> ChangeReport:
    findings: list[Finding] = []
    python_files = {
        path: source for path, source in request.files.items() if path.endswith(".py")
    }
    analyses = [analyze_python(path, source) for path, source in python_files.items()]
    dependency_edges = sum(len(item.imports) for item in analyses)

    for item in analyses:
        if item.syntax_error:
            findings.append(Finding(
                kind="syntax-error",
                path=item.path,
                message=item.syntax_error,
            ))
        if item.has_debug_print:
            findings.append(Finding(
                kind="debug-print",
                path=item.path,
                message="Python source contains a print() call.",
            ))

    risk = min(
        100,
        len(request.files) * 5
        + len(python_files) * 3
        + dependency_edges * 2
        + sum(20 if f.kind == "syntax-error" else 5 for f in findings),
    )

    return ChangeReport(
        change_id=request.change_id,
        file_count=len(request.files),
        python_file_count=len(python_files),
        dependency_edges=dependency_edges,
        risk_score=risk,
        findings=findings,
    )
