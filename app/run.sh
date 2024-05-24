#!/bin/bash
cd /home/duchi/Programming/DoAnTKHDT/

source .venv/bin/activate


cd /home/duchi/Programming/DoAnTKHDT/app

python manage.py runserver &

RUNSERVER_PID=$!
python manage.py tailwind start &

TAILWIND_PID=$!

# Save PIDs to a file for later use
echo $RUNSERVER_PID > runserver.pid
echo $TAILWIND_PID > tailwind.pid
# wait for both background process to finish
wait
