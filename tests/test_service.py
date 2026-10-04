from portfolio_api.models import ChangeRequest
from portfolio_api.service import analyze_change


def test_change_report_is_deterministic():
    request = ChangeRequest(
        change_id="pr-1",
        files={
            "a.py": "import os\nprint('debug')\n",
            "b.py": "value = 1\n",
            "config.yml": "enabled: true\n",
        },
    )
    report = analyze_change(request)
    assert report.file_count == 3
    assert report.python_file_count == 2
    assert report.dependency_edges == 1
    assert report.risk_score == 28
    assert [finding.kind for finding in report.findings] == ["debug-print"]
