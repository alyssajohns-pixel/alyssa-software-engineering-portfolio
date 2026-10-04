from __future__ import annotations

import ast
from dataclasses import dataclass


@dataclass(frozen=True)
class FileAnalysis:
    path: str
    imports: tuple[str, ...]
    syntax_error: str | None
    has_debug_print: bool


def analyze_python(path: str, source: str) -> FileAnalysis:
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as exc:
        return FileAnalysis(
            path=path,
            imports=(),
            syntax_error=f"{exc.msg} at line {exc.lineno}",
            has_debug_print=False,
        )

    imports: set[str] = set()
    has_debug_print = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "print"
        ):
            has_debug_print = True

    return FileAnalysis(
        path=path,
        imports=tuple(sorted(imports)),
        syntax_error=None,
        has_debug_print=has_debug_print,
    )
