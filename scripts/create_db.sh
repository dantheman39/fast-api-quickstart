# Assumes that `docker-compose up db` is running
# Local .env
if [ -f .env ]; then
    # Load Environment Variables
    export $(cat .env | grep -v '#' | sed 's/\r$//' | awk '/=/ {print $1}' )
fi
docker-compose exec db psql -U "${DB_USER}" -d "${DB_NAME}" -f /root/scripts/create_db.sql
