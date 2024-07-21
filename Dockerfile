# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

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

# Run the Django development server
ENTRYPOINT "./usr/src/app/django-entrypoint.sh"