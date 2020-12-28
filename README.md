# flask-rest-api

A simple REST API in Flask written for Task Manager webservice

`<img placeholder>`

A short project about REST APIs related to my [other project](https://github.com/msztylko/flask-task-manager). I decided to keep them separate for now, because my main goal is to explore more topics and tools related to API development rather than creating full Task Manager web application. I hope to use this project as a reference for future projects involving REST APIs with Flask.

## API description

| EndPoint | Functionality
|----------|--------------
| GET /tasks | List all tasks
| POST /tasks | Create a new task
| GET /tasks/<task_id> | Get single task with specific ID
| PUT /tasks/<task_id> | Update specific task
| DELETE /tasks/<task_id> | Delete a task

## INSTALL

If you want to try it yourself:

1. `git clone https://github.com/msztylko/flask-rest-api.git && cd flask-rest-api`
2. `python3 -m virtualenv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python initial_db.py`
6. `python api.py`

### Run with Docker

After cloning the repo:
1. `docker build -t flask-rest-api .`  
2. `docker run -p 5000:5000 flask-rest-api`

## Test 

Start application and from another terminal run `pytest`. You can also use simpler `test.sh` file which demonstrates basic usage with curl.
