import requests

base_url = 'http://0.0.0.0:5000/'
def test_api():
    response = requests.get(base_url)
    assert response.status_code == 200
    
