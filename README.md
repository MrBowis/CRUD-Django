# CRUD-Django

## Description
This is a simple CRUD application using Django. It allows you to create, read, update and delete records from a database.

## Recomentations
Use a virtual environment to install the dependencies.
You can use the following command to create a virtual environment:
```bash
python -m venv venv
```
Then you can activate the virtual environment using the following command:

Linux/Mac:
```bash
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```
After activating the virtual environment you can install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone the repository
2. Install the required packages using the command
```bash
pip install -r requirements.txt
```
3. Run the server using the command
```bash
python manage.py runserver`
```

## Usage
1. Go to the URL `http://localhost:8000/`

## Explanation
This project is a simple CRUD application using Django. It allows you to create, read, update and delete records from a database. The application has a two models called `Task` and `Comments` with the following fields:
- Task
    - Title
    - Description
    - Completed
    - Created Date
- Comments
    - Task
    - Body
    - Created Date

The application has the following views:
- Task List View: This view displays a list of all the tasks in the database. It also allows you to create a new task.
- Task Detail View: This view displays the details of a specific task. It also allows you to update or delete the task.

The application also has a REST API that allows you to perform CRUD operations on the tasks and comments. The API has the following endpoints:

- `/api/tasks/`
    - GET: Get a list of all tasks
    - POST: Create a new task
- `/api/tasks/{id}/`
    - GET: Get the details of a specific task
    - PUT: Update a specific task
    - DELETE: Delete a specific task
- `/api/comments/`
    - GET: Get a list of all comments
    - POST: Create a new comment
- `/api/comments/{id}/`
    - GET: Get the details of a specific comment
    - PUT: Update a specific comment
    - DELETE: Delete a specific comment

The application also has a simple user authentication system that allows you to create an account, login and logout.

## Technologies
- Python
- Django
- Django REST Framework
- SQLite

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Author
- [Alejandro Andrade](https://github.com/MrBowis)
- [Allan Panchi](https://github.com/AllanPanchi)
