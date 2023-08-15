# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt
# RUN python manage.py makemigrations 
# RUN python manage.py migrate

# Copy the entire Django project to the container
COPY . .

# Expose the port that the Django development server will run on
EXPOSE 8000

# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]