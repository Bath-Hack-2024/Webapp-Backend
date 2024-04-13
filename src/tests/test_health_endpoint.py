from conftest import client

def test_should_return_status_200(client):
    response = client.get('/health')
    assert response.status_code == 200