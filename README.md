Employee App a web application which is designed to store employee data, uses rest api to get the employee data from a google sheet and post it to the employee model, uses rest api to show the employee data in the employee model, provide a page for a user to register
login and add employee data to the employee model.

USER MANUAL
1. Navigate to the 'employee_api' folder
2. Create a virtual environment; python -m venv env
3. Activate the virtual environment; env\Scripts\activate
4. Install the requirements.txt in the virtual environment; pip install -r requirements.txt
5. Set DATABASE_URL to a postgres database URL
6. Start Django app; python manage.py runserver
7. Open http://127.0.0.1:8000/ in a browser to access the user interface
8. Open http://127.0.0.1:8000/api/v1/ to view all data in the employee model
9. Open http://127.0.0.1:8000/api/v1/spreadsheet/13yyd8s008LlRn0tn6LC5moH1fcBELBkYw2THX6gjdHU/ to add data in the google spreadsheet

Routes: 
'' 
'api/v1/'
'api/v1/spreadsheet/<key>/'   where key is the google spreadshee id


Admin mamagement: the admin can visit the '/admin/' to view the models

Environmental variables used are:
- DATABASE_URL,

Aditional infomation: 
Run Django 'python manage.py createsuperuser' to create an admin account

Hosted Link: https://veek-employee-app.herokuapp.com/