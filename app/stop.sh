#!/bin/bash
if [ -f /home/duchi/Programming/DoAnTKHDT/runserver.pid ]; then
	kill $(cat /home/duchi/Programming/DoAnTKHDT/runserver.pid)
	rm /home/duchi/Programming/DoAnTKHDT/runserver.pid
fi

if [ -f /home/duchi//Programming/DoAnTKHDT/tailwind.pid ]; then
	kill $(cat /home/duchi/Programming/DoAnTKHDT/tailwind.pid)
	rm /home/duchi/Programming/DoAnTKHDT/tailwind.pid
fi
