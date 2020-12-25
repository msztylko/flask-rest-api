from flask_restful import abort, Resource, reqparse

TASKS = {
    'task1': {'task': 'Build api'},
    'task2': {'task': '??????'},
    'task3': {'task': 'profit!'}
}

def abort_if_task_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(404, message=f'Task {task_id} not found')

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

    def post(self, task_id):
        args = parser.parse_args()
        task_id = len(TASKS) + 1
        task_id = f'task_id{task_id}'
        TASKS[task_id] = {'task': args['task']}
        return TASKS[task_id], 201
