# Assumes that `docker-compose up db` is running
docker-compose exec db psql -U daniel -d recordings -f /root/scripts/create_db.sql
