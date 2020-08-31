from http import HTTPStatus
import urllib.parse

def test_index(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
