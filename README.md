[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)
# CS_2025_project 
# Student Task Tracker

## Description

**Student Task Tracker** is a simple web application for students to manage their academic tasks.  
Users can create, edit, and delete tasks, link them to specific subjects and deadlines, and mark their completion status.  
The app helps students stay organized and never miss important deadlines.

## Setup

### Run with Docker
1. Clone the repository:
```
   ```bash
   git clone https://github.com/Tacitus-SL/student-task-tracker.git
   cd student-task-tracker
```
2. Build and start the containers:
```
docker-compose up --build
```
3. The app will be available at:
http://localhost:5000


## Requirements

Python 3.11
Flask
Docker
...

## Features

* Create, edit, and delete tasks
* Assign subject, description, and due date
* Mark task status: “in progress” or “completed”
* Filter and view tasks by date or subject
* Simple browser-based client interface

## Git

Specify which branch will store the latest stable version of the application

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
