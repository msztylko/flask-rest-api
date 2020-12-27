import pytest
import requests

base_url = 'http://0.0.0.0:5000/'

@pytest.mark.parametrize('task', ['be awesome', 'write great code', 'have fun', 'drink water'])
def test_post_tasks(task):
    response = requests.post(base_url + 'tasks', data={'task': task})
    assert response.status_code == 201

def test_get_tasks():
    response = requests.get(base_url + 'tasks')
    assert response.status_code == 200

def test_get_task_id():
    response = requests.get(base_url + 'tasks/3')
    assert response.status_code == 200

def test_put_task_id():
    response = requests.put(base_url + 'tasks/1',  data={'task': 'updated task'})
    assert response.status_code == 201

def test_delete_task_id():
    # Get ID of the last existing task to delete it
    to_delete = requests.get(base_url + 'tasks').json()[-1]['id']
    response = requests.delete(base_url + f'tasks/{to_delete}')
    assert response.status_code == 240

