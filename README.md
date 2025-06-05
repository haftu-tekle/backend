
This is a backend REST API for managing tasks, built using Django and Django REST Framework.

# Features of the task_api

*Task Creation:** Add new tasks with a title and optional description.
*Task Listing:** Retrieve all tasks.
*Task Detail:** Retrieve a single task by its ID.
*Task Update:** Modify existing tasks 
*Task Deletion:** Remove tasks.

#Library and database

  *Python 3
  *Django
  *Django REST Framework
  *SQLite3
  
#Setup

# 1. Clone the Repository

First, clone the repository to your local machine:

###
git clone [https://github.com/haftu-tekle/backend.git](https://github.com/haftu-tekle/backend.git)
cd backend/kuraz_taskapi ###
# 2. Create venv
python -m venv kurvenv

# 3. Install requirements
pip install -r requirements.txt

# 4. DB migration
python manage.py makemigrations task_api
python manage.py migrate

# 5.Run  Django server
python manage.py runserver
