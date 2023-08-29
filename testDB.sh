#! /bin/bash

docker exec -it demo-db psql -U postgres -d joda -c "SELECT * FROM user_sentiment;"