from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

tasks = {}


class TaskList(Resource):
    def get(self, task_id):
        return {task_id: tasks[task_id]}

    def put(self, task_id):
        # get data from the data field of put request
        tasks[task_id] = request.form['data']
        return {task_id: tasks[task_id]}

api.add_resource(TaskList, '/tasks/<string:task_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
