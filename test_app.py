from fastapi.testclient import TestClient
from main import app

# Créer un client de test pour l'application
client = TestClient(app)

# Écrire le test pour le point de terminaison /status
def test_status_endpoint():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
