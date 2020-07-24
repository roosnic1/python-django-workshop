# Python / Django Workshop 

[Presentation](https://docs.google.com/presentation/d/1Ajh-sdFcTWu0pmPWEP3PohCnFd5iyIXWDjG8e3JS0_k/edit?usp=sharing)

## Setup Django Project
1. Create or activate pyenv virtualenv `pyenv activate workshop`
1. Cd into the techface directory `cd techface`
1. Install all the python requirements `pip install -r requirements.txt`
1. Execute the database migrations `python manage.py migrate`
1. Create a super user `python manage.py createsuperuser`
1. Run the development server `python manage.py runserver`
1. Open the browser at `http://localhost:8000/app/` and create some questions in the admin `http://localhost:8000/admin/`