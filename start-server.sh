#!/bin/sh

# Wait for the database to be ready
echo "Waiting for database to be ready..."
while ! pg_isready -h db -U ${DB_USER} -d ${DB_NAME}; do
  sleep 2
done

# Make migrations
echo "Making migrations..."
python manage.py makemigrations

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Create roles if not already created
echo "Creating roles..."
python manage.py create_roles

# Create default superuser if it does not exist
echo "Creating default superuser..."
python manage.py default_super_user_creation

# Finally, run the Django development server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000