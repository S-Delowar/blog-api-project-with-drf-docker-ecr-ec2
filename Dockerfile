# Pull a base image
FROM python:3.11-slim-bullseye

# Set environemnt variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHON UNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy object
COPY . .


# Collect static files (for production)
RUN python manage.py collectstatic --noinput

# Expose Gunicorn port (not needed in Nginx as Nginx will handle this)
EXPOSE 8000