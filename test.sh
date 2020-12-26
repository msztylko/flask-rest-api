echo GET TaskList
curl http://0.0.0.0:5000/tasks 
echo

echo POST new task
curl http://0.0.0.0:5000/tasks -d "task=be awesome" -X POST
echo

echo GET single Task
curl http://0.0.0.0:5000/tasks/task2
echo

echo DELETE single Task
curl http://0.0.0.0:5000/tasks/task4 -X DELETE
echo

echo PUT update task
curl http://0.0.0.0:5000/tasks/task3 -d "task=write great code" -X PUT
echo
