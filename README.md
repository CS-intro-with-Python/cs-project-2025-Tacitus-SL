# CS_2025 Project: Student Task Tracker

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)

## Description

**Student Task Tracker** is a simple web application for students to manage their academic tasks.  
Users can create, edit, and delete tasks, assign them to specific subjects and deadlines, and mark their completion status.  
The app helps students stay organized and ensures they never miss important deadlines.

## Features

- Create, edit, and delete tasks  
- Assign subject, description, and due date  
- Mark task status as “in progress” or “completed”  
- Filter and view tasks by date or subject  
- Simple browser-based interface
- Data storage using SQLite

## Requirements

- Python 3.11  
- Flask  
- Docker  

## Setup

1. Clone the repository:  
```bash
git clone https://github.com/CS-intro-with-Python/cs-project-2025-Tacitus-SL
cd cs-project-2025-Tacitus-SL
```

2. Create a virtual environment and install dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Build and start the container:
```
docker-compose up --build
```

4. Start the server:
```
python3 server.py
```

5. The app will be available at:
http://localhost:5000

## Testing
Run unit tests with pytest:
```
pytest unit_tests.py
```

## Success Criteria

The project will be considered successful if:

* The application runs in Docker and is accessible locally or online.
* Users can perform CRUD operations (Create, Read, Update, Delete) on tasks.
* Tests and CI are configured and working.
* A clear and complete README file is provided.

## Deployed Application
The Student Task Tracker is deployed online and can be accessed via the following link:

https://cs-project-2025-tacitus-sl-production.up.railway.app/

This deployment allows you to:
* Access the app from any browser without installing anything locally.
* Test all features, including creating, editing, and deleting tasks.
* Explore the live interface and verify that all functionalities work as intended.

## CI/CD Pipeline

This project uses **GitHub Actions** together with **Railway** for continuous integration and deployment.

### GitHub Actions

The workflow runs automatically on every push to the repository and includes the following checks:

1. **Docker Build** – verifies that the Docker image builds successfully.
2. **Container Run** – ensures that the container starts and the application runs.
3. **Route Check** – uses a Python client with the `requests` library to verify that the main route (`/`) is accessible and responds correctly.

All workflow runs are visible in the **Actions** tab of the GitHub repository, and must pass for the project to be considered fully functional.

### Deployment with Railway

The Docker image is deployed to **Railway.app**, making the application accessible online.  
Railway automatically updates the deployment whenever new changes are pushed to the main branch, ensuring that the online version always reflects the latest stable code.

