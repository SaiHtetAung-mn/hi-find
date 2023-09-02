# Hi-find

## Setup & Run Server
  - Clone the  project
  - Create the virtual environment for the django project in the clone folder using the following command
  - `python -m venv myvirtual`
  - Activate the virtural  environment using the following commands
  - `cd myvirtual`
  - `Scripts\Activate`
  - Install the required libraries with the following commands
  - `pip install -r requirements.txt`
  - Create database `lost_and_found`
  - Config your mysql credential in `lost_and_found > settings.py`
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - `python manage.py runserver`





