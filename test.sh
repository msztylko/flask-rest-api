# GET TaskList
curl http://0.0.0.0:5000/tasks -v

# POST new task
curl http://0.0.0.0:5000/tasks -d "task=be awesome" -X POST -v

# GET single Task
curl http://0.0.0.0:5000/tasks/task2

# DELETE single Task
curl http://0.0.0.0:5000/tasks/task5 -X DELETE -v

# PUT update task
curl http://0.0.0.0:5000/tasks/task3 -d "task=write great code" -X PUT
