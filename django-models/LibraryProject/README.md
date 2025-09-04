# Django Development Environment Setup and Project Creation

This guide will help you set up a Django development environment and create a basic Django project named **LibraryProject**. By following these steps, you'll gain familiarity with Django's workflow, including project creation, running the development server, and exploring the project's structure.

## Objective

Gain hands-on experience with Django by setting up your environment and creating a foundational project.

## Prerequisites

- Python (version 3.8 or higher)
- pip (Python package manager)
- Git (optional, for version control)

## Steps

### 1. Install Django

Ensure Python is installed on your system. Then, install Django using pip:

```bash
pip install django
```

### 2. Create a New Django Project

Create a new Django project named **LibraryProject**:

```bash
django-admin startproject LibraryProject
cd LibraryProject
```

### 3. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the default Django welcome page.

### 4. Explore the Project Structure

Familiarize yourself with the following key files:

- **settings.py**: Configuration for the Django project.
- **urls.py**: URL declarations for the project.
- **manage.py**: Command-line utility for interacting with the project.

### 5. Create a README File

Inside the `LibraryProject` directory, create a `README.md` file to document your setup and workflow.

## Repository Information

- **GitHub repository**: `Alx_DjangoLearnLab`
- **Directory**: `Introduction_to_Django`

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
