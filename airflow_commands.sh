#!/usr/bin/env bash

# Initiliase the metastore
airflow db init

# Run the scheduler in background
airflow scheduler &> /dev/null &

# Create user
airflow users create -u azurelib -p azurelib -r Admin -e admin@azurelib.com -f Jayaadityan -l Manmathan

# Run the web server in foreground (for docker logs)
exec airflow webserver
