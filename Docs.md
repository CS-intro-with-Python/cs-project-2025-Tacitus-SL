    # API & Page Documentation

This document describes all routes (endpoints) of the **Student Task Tracker** application.  
For each route you will find:
- What data the page shows  
- What actions the user can take  
- Which elements (forms, buttons) are present  

---

## 1. Main Page – All Tasks
**URL:** `/`  
**Method:** `GET`  
**Description:** Displays a list of all tasks.

### Shows to the user:
- Task title  
- Subject  
- Due date  
- Status: `in progress` / `completed`  

### User actions:
- Mark a task as completed  
- Open the edit page for a task  
- Delete a task  

### Elements on the page:
- **Add Task** button (links to `/task/add`)  
- **Edit** button next to each task  
- **Delete** button next to each task  
- **Mark as Completed** button (if the task is not completed)

---

## 2. Add Task Page
### GET request
**URL:** `/task/add`  
**Method:** `GET`  
**Description:** Shows an HTML form for creating a new task.

### Shows to the user:
- An empty creation form

### User actions:
- Fill out task data  
- Click **Create Task**

### Elements:
- Subject (text input)  
- Description (text input)  
- Due Date (date input)  
- Submit / Create Task button

---

### POST request
**URL:** `/task/add`  
**Method:** `POST`  
**Description:** Processes the submitted creation form and adds a new task.

### Shows to the user:
- Redirect to `/`  
or  
- Success message (depending on implementation)

### User actions:
- No action (form already submitted)

---

## 3. Edit Task Page
### GET request
**URL:** `/task/<id>/edit`  
**Method:** `GET`  
**Description:** Displays a form to edit an existing task.

### Shows to the user:
- A pre-filled form with the current task data

### User actions:
- Modify task information  
- Click **Save Changes**

### Elements:
- Subject  
- Description  
- Due Date  
- Status selector (dropdown or switch)  
- Save button  

---

### POST request
**URL:** `/task/<id>/edit`  
**Method:** `POST`  
**Description:** Processes the edit form and updates the selected task.

### Shows to the user:
- Redirect to `/` or task details

---

## 4. Delete Task
**URL:** `/task/<id>/delete`  
**Method:** `POST`  
**Description:** Deletes the selected task.

### Shows to the user:
- Redirect to the main task list

### User actions:
- Confirm deletion (if confirmation page exists)

### Elements (optional confirmation page):
- “Are you sure you want to delete this task?”  
- Delete button  
- Cancel button

---

## 5. Mark Task as Completed
**URL:** `/task/<id>/complete`  
**Method:** `POST`  
**Description:** Changes the task's status to `completed`.

### Shows to the user:
- Redirect to `/` with updated status

### User actions:
- Click **Mark Completed**

### Elements:
- **Complete** button

---


