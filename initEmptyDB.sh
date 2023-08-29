#!/bin/bash 

# Create DB table in 'demo-db' docker container
docker exec -it demo-db psql -U postgres -c "CREATE DATABASE joda;"
docker exec -it demo-db psql -U postgres -d joda -c "CREATE TABLE IF NOT EXISTS user_sentiment (name varchar(255), sentiment varchar(255));"


