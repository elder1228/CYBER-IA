from fastapi.testclient import TestClient
from app.main import appclient = TestClient(app)def test_health_root():
 resp = client.get("/")
 assert resp.status_code == 200def test_docs_available():
 resp = client.get("/docs")
 assert resp.status_code == 200