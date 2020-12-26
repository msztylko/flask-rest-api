from flask import Flask, request
from flask_restful import Api, Resource, fields, marshal_with, reqparse, abort


app = Flask(__name__)
api = Api(app)

TASKS = {
    'task1': {'task': 'build an API'},
    'task2': {'task': '???????'},
    'task3': {'task': 'profit!'}
}

def abort_if_task_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(404, message=f'Task {task_id} doesnt exist')

parser = reqparse.RequestParser()
parser.add_argument('task')

class Task(Resource):
    def get(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        return TASKS[task_id]        

    def delete(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        del TASKS[task_id]
        return '', 204

    def put(self, task_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TASKS[task_id] = task
        return task, 201
    
class TaskList(Resource):
    def get(self):
        return TASKS

    def post(self):
        args = parser.parse_args()
        task_id = int(len(TASKS) + 1)
        task_id = f'task{task_id}'
        TASKS[task_id] = {'task': args['task']}
        return TASKS[task_id], 201

# SETUP API
api.add_resource(Task, '/tasks/<task_id>')
api.add_resource(TaskList, '/tasks')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
