Hello World Django Project

Overview
This is a basic Django project that displays "Hello, World!" on the homepage. It serves as a starting point for understanding how to set up a Django project and create a basic view.

Prerequisites
Python: 3.6 or later
Django: 4.0 or later (compatible with the Python version you use)

Getting Started
Follow these steps to get the project up and running on your local machine.
1. Create Virtual Environment:
-Enter command in command prompt: py -m venv myenv

2. Activate the env:
-Enter command in command prompt:cd myenv\Scripts\activate

3. Start deployment server:
-py manage.py runserver

4. View application:
-Open your web browser and go to http://127.0.0.1:8000/. You should see a page displaying "Hello, World!".

Project Structure
Here is a brief overview of the project structure:

hello_world_django/: The project directory.
hello_world_django/: Contains project settings and configuration.
__init__.py: Initializes the Django application.
settings.py: Contains settings for the Django project.
urls.py: URL declarations for the project.
wsgi.py: WSGI configuration for deploying the project.
manage.py: A command-line utility for managing the project.
