from conftest import client

def test_should_return_status_200(client):
    response = client.post('/register_station', json={'email': 'ggg@gmail.com', 'station_name': 'station1'}, content_type='application/json')
    assert response.status_code == 200

def test_should_return_status_400(client):
    response = client.post('/register_station', json={}, content_type='application/json')
    assert response.status_code == 400

    response = client.post('/register_station', json={'email': 'gg@gmail.com'}, content_type='application/json')
    assert response.status_code == 400

    response = client.post('/register_station', json={'station_name': 'station1'}, content_type='application/json')
    assert response.status_code == 400

    response = client.post('/register_station', content_type='application/json')
    assert response.status_code == 400
