
#!/bin/bash

# Read the PIDs from the files
RUNSERVER_PID=$(cat runserver.pid)
TAILWIND_PID=$(cat tailwind.pid)

# Kill the processes
kill $RUNSERVER_PID
kill $TAILWIND_PID

# Optionally, remove the PID files
rm runserver.pid tailwind.pid
