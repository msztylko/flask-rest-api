# Basic tests

echo POST /tasks - Create a new task
curl http://0.0.0.0:5000/tasks -d "task=be awesome" -X POST
curl http://0.0.0.0:5000/tasks -d "task=write great code" -X POST
curl http://0.0.0.0:5000/tasks -d "task=have fun" -X POST
curl http://0.0.0.0:5000/tasks -d "task=drink water" -X POST
echo

echo GET /tasks - List all tasks
curl http://0.0.0.0:5000/tasks 
echo

echo GET single Task
curl http://0.0.0.0:5000/tasks/3
echo

echo PUT update task
curl http://0.0.0.0:5000/tasks/1 -d "task=updated task" -X PUT
echo

echo DELETE single Task
curl http://0.0.0.0:5000/tasks/2 -X DELETE
echo

