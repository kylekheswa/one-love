# Django Project Installation Guide

This guide will walk you through the process of setting up and installing a Django project using a virtual environment (venv) and Docker.

## Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system.
- [Docker](https://docs.docker.com/get-docker/) installed on your system.

## Step 1: Clone the Repository

git clone https://github.com/kylekheswa/One-Love-Central.git
cd onelove

## Step 2: Set Up Virtual Environment

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Linux or macOS
source venv/bin/activate

## Step 3: Install Dependencies


pip install -r requirements.txt

## Step 4: Configure Django Settings

Copy the example settings file and update it with your configurations:


cp onelove/settings.example.py onelove/settings.py

## Step 5: Run Migrations


python manage.py migrate

## Step 6: Create a Superuser (Optional)


python manage.py createsuperuser

## Step 7: Run the Development Server


python manage.py runserver

## Using Docker (Optional)

### Step 8: Build and Run Docker Containers


# Build Docker image
docker build -t onelove .

# Run Docker container
docker run -p 8000:8000 onelove
