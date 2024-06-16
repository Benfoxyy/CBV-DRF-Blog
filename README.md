<h1 align="center">Django Blog</h1>
<h3 align="center">Class base view restframework with GenericView classes project</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="restframework" width="90" height="40"/> </a>
<a href="https://www.sqlite.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>
<a href="https://jwt.io/" target="_blank"> <img src="https://jwt.io/img/icon.svg" alt="jwt" width="40" height="40"/> </a>
</p>

### Project endpoints
![Screenshot 2024-06-09 121434](https://github.com/Benfoxyy/CBV-DRF-Blog/assets/146076866/e5615902-4584-41ec-b746-a1a5d3366bbe)

### Authentication method
- Jason Web Token ( JWT )

### General features
- Class Based View
- Django RestFramewok
- Generic View
- User Authentication

### Blog features
- Create
- Edit
- Delete

### Accounts features
- Registeraton
- Create JWT
- Refresh JWT
- Validate JWT
- Change Password
- Reset Password
- Validate Email

### Setup
To get the repository you need to run this command in git terminal
```bash
git clone https://github.com/Benfoxyy/CBV-DRF-Blog.git
```

### Getting ready
Create an environment for install all dependencies with this command
```bash
python -m venv venv
```

Install all project dependencies with this command
```bash
pip install -r rquirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and ru fallowing command
```bash
python manage.py makemigrations
```

This command will create all migrations file to database

Now, to apply this migrations run following command
```bash
python manage.py migrate
```

### Option
For editing or manage the database, you shulde be superuser and have superuser permission. So lets create superuser
```bash
python manage.py createsuperuser
```
- Email
- Password
- Password confirmation

### Run server
And finally lets start server and see and using the app
```bash
python manage.py runserver
```

Whene server is up and running, go to a browser and type http://127.0.0.1:8000

### See all apis
For see the all of apis and test you need to go to swagger page with this http://127.0.0.1:8000/swagger/

### Database shema
![drawSQL-image-export-2024-05-30](https://github.com/Benfoxyy/CBV-DRF-Blog/assets/146076866/66f0eb3c-c5cc-4ff8-93f7-1e962253c96d)

<hr>

<h3 align='center'>Thanks for visiting my app, if you have any opinions or seeing bugs; let me know 🙂</h3>