import json
from pathlib import Path


def test_safe_registry_fixture():
    path = Path(__file__).resolve().parents[1] / "registry" / "sources.v1.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    sources = data["sources"]
    assert len({s["id"] for s in sources}) == len(sources)
    assert all(s["url"].startswith("https://") for s in sources)
    assert all(s["outreach_allowed"] is False for s in sources)
