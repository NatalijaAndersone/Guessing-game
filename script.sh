#!/bin/bash

echo "Script for checking the configuration files"
echo "------------------------------------------------"

echo "Checking if config.ini exists -->"
if test -f "C:\Users\natan\PycharmProjects\Guessing-game\config.ini"; then
    echo "exists"
else
	if [ $? -eq 0 ]; then echo "OK"; else echo "No config.ini file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Checking if log_migrate_db.yaml exists-->"
if test -f "C:\Users\natan\PycharmProjects\Guessing-game\log\log_migrate_db.yaml"; then
    echo "exists"
else
	if [ $? -eq 0 ]; then echo "OK"; else echo "No log_migrate_db.yaml file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "ALL SET UP!"