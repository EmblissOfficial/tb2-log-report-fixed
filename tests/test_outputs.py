import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    return json.loads(REPORT.read_text())


def test_report_saved_as_valid_json():
    """Verifies instruction.md criterion 1: save a valid JSON file at /app/report.json."""
    assert REPORT.exists(), "report.json was not created at /app/report.json"
    assert isinstance(load_report(), dict), "report.json must contain a JSON object"


def test_total_requests():
    """Verifies instruction.md criterion 2: total_requests is the total number of non-empty log lines."""
    data = load_report()
    assert data.get("total_requests") == 6, "total_requests is incorrect"


def test_unique_ips():
    """Verifies instruction.md criterion 3: unique_ips is the number of distinct client IP addresses."""
    data = load_report()
    assert data.get("unique_ips") == 3, "unique_ips is incorrect"


def test_top_path():
    """Verifies instruction.md criterion 4: top_path is the most frequently requested path."""
    data = load_report()
    assert data.get("top_path") == "/index.html", "top_path is incorrect"
