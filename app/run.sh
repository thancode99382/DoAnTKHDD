#!/bin/bash

# Function to start the services
start_services() {
	cd /home/duchi/Programming/DoAnTKHDT/

	source .venv/bin/activate

	cd /home/duchi/Programming/DoAnTKHDT/app

	python manage.py runserver &
	RUNSERVER_PID=$!
	python manage.py tailwind start &
	TAILWIND_PID=$!

	# Save PIDs to a file for later use
	echo $RUNSERVER_PID >/home/duchi/Programming/DoAnTKHDT/runserver.pid
	echo $TAILWIND_PID >/home/duchi/Programming/DoAnTKHDT/tailwind.pid
}

# Function to stop the services
stop_services() {
	if [ -f /home/duchi/Programming/DoAnTKHDT/runserver.pid ]; then
		kill $(cat /home/duchi/Programming/DoAnTKHDT/runserver.pid)
		rm /home/duchi/Programming/DoAnTKHDT/runserver.pid
	fi

	if [ -f /home/duchi//Programming/DoAnTKHDT/tailwind.pid ]; then
		kill $(cat /home/duchi/Programming/DoAnTKHDT/tailwind.pid)
		rm /home/duchi/Programming/DoAnTKHDT/tailwind.pid
	fi
}

# Start the services initially
start_services

# Watch for file creation in the specified directory
inotifywait -m -e create --format '%w%f' /home/duchi/Programming/DoAnTKHDT/app | while read NEWFILE; do
	echo "New file created: $NEWFILE"
	# Restart the services
	stop_services
	start_services
done
