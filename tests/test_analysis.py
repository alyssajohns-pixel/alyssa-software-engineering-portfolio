from portfolio_api.analysis import analyze_python


def test_extracts_imports_and_debug_print():
    result = analyze_python(
        "app.py",
        "import os\nfrom pathlib import Path\nprint('debug')\n",
    )
    assert result.imports == ("os", "pathlib")
    assert result.has_debug_print
    assert result.syntax_error is None


def test_syntax_error_is_reported_not_raised():
    result = analyze_python("broken.py", "def broken(:\n    pass\n")
    assert result.syntax_error is not None
    assert result.imports == ()
