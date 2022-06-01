# assumes pods are running
docker-compose -f docker-compose.yml -f docker-compose.test.yml exec server pytest
