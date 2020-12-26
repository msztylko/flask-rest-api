# Change id to integers

echo GET TaskList
curl http://0.0.0.0:5000/tasks 
echo
# 
# echo POST new task
# curl http://0.0.0.0:5000/tasks -d "task=be awesome" -X POST
# echo

echo PUT update task
curl http://0.0.0.0:5000/tasks/42 -d "task=I want to see you" -X PUT
echo

echo GET single Task
curl http://0.0.0.0:5000/tasks/42
echo

echo DELETE single Task
curl http://0.0.0.0:5000/tasks/42 -X DELETE
echo

