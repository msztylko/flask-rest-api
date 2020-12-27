from flask import Flask, request
from flask_restful import Api, Resource, fields, marshal_with, reqparse, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Database Models

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Task {self.id} created.'

# Create database
# Do it after defining your model
# db.create_all()


parser = reqparse.RequestParser()
parser.add_argument('task')

# Define how database object will be serialized
resource_fields = {
    'id': fields.Integer,
    'task': fields.String
}

class Task(Resource):

    @marshal_with(resource_fields)
    def get(self, task_id):
        result = TaskModel.query.filter_by(id=task_id).first()
        if not result:
            abort(404, message=f'Could not find task with if {task_id}')
        return result

    def delete(self, task_id):
        task = TaskModel.query.get(task_id)
        if not task:
            abort(404, message=f'No Task with id {task_id}')
        db.session.delete(task)
        db.session.commit()
        return '', 240

    @marshal_with(resource_fields)
    def put(self, task_id):
        args = parser.parse_args()
        task = TaskModel.query.filter_by(id=task_id).first()
        if not task:
            abort(409, message=f'Could not find task with ID {task_id}')
        task.task = args['task']
        db.session.add(task)
        db.session.commit()
        return task, 201
    
class TaskList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = TaskModel.query.all()
        if not result:
            abort(404, message=f'Could not get requests tasks')
        return result
    
    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        task = TaskModel(task=args['task'])
        db.session.add(task)
        db.session.commit()
        return task, 201

# SETUP API
api.add_resource(Task, '/tasks/<int:task_id>')
api.add_resource(TaskList, '/tasks')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
