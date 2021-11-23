#!/bin/bash

echo "Script for preparing the development environment"
echo "------------------------------------------------"

echo "Checking if config.ini exists in the current working dir -->"
if test -f "config.ini"; then
    echo "exists"
else
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying config.ini file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Checking if log_migrate_db.yaml exists in the current working dir -->"
if test -f "log_migrate_db.yaml"; then
    echo "exists"
else
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_migrate_db.yaml file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Getting python3 executable loc"
python_exec_loc=$(which python3)
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem getting python3 exec location"; exit 1; fi
echo "$python_exec_loc"
echo "------------------------------------------------"

echo "Running config tests"
$python_exec_loc test_config.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Configuration test FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "Running DB migrations"
$python_exec_loc migrate_db.py
if [ $? -eq 0 ]; then echo "OK"; else echo "DB migration FAILED"; exit 1; fi
echo "------------------------------------------------"
echo "ALL SET UP! YOU ARE READY TO CODE"