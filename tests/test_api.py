import requests

base_url = 'http://0.0.0.0:5000/'
def test_api():
    response = requests.put(base_url + 'tasks/0', data={'data': 'Be awesome'})
    print(response.json()) 
