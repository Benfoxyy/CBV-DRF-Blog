<h1 align="center">Django Blog With Rest Framework</h1>
<h3 align="center">You can post an article to blog and other people can see and put comment under your post</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="restframework" width="90" height="40"/> </a>
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>
<a href="https://jwt.io/" target="_blank"> <img src="https://jwt.io/img/icon.svg" alt="jwt" width="40" height="40"/> </a>
<a href="https://swagger.io/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354420/swagger.svg" alt="swagger" width="40" height="40"/> </a>
<a href="https://www.gunicorn.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gunicorn/gunicorn-icon.svg" alt="gunicorn" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/nginx/nginx-icon.svg" alt="nginx" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg" alt="nginx" width="40" height="40"/> </a>

</p>

### Project endpoints
![accounts](https://github.com/Benfoxyy/CBV-DRF-Blog/assets/146076866/b4da6a0e-f936-43aa-948e-a2943a3e669f)

<hr>

![blog](https://github.com/Benfoxyy/CBV-DRF-Blog/assets/146076866/6a0725e6-2ef6-486b-9593-7c11f30af2ed)

### General features
- Class Based View
- Django RestFramewok
- Generic View
- User Authentication
- Test processing
- Dockrized
- Faker

### Accounts features
- Registeraton
- Create JWT
- Refresh JWT
- Validate JWT
- Change Password
- Reset Password
- Email Validations

### Blog features
- List
- Create
- Retrieve
- Edit
- Delete

### Commenting features
- List
- Create

### Authentication method
- Jason Web Token ( JWT )

### DB
PostgreSQL

### Web serving methods
- Gunicorn
- Nginx

### Test method
Pytest

### Reformatting method
- flake8
- black

### Setup
To get the repository you need to run this command in git terminal
```bash
git clone https://github.com/Benfoxyy/CBV-DRF-Blog.git
```

### Getting ready

The project is base on docker so lets start <a href='https://docs.docker.com/engine/install/'>docker</a> and using the app
```bash
docker-compose -f docker-compose.stage.yml up -d
```

Once you have installed django and other packages, go to the cloned repo directory and ru fallowing command
```bash
docker-compose -f docker-compose.stage.yml exec sh -c "python manage.py makemigrations"
```

This command will create all migrations file to database

Now, to apply this migrations run following command
```bash
docker-compose -f docker-compose.stage.yml exec sh -c "python manage.py migrate"
```

Now you can go to a browser and type http://127.0.0.1:80 and see the resault!

<hr>

### Access to admin panel
For editing or manage the database, you shulde be superuser and have superuser permission. So lets create superuser
```bash
docker-compose -f docker-compose.stage.yml exec sh -c "python manage.py createsuperuser"
```
- Email
- Password
- Password confirmation

Thene you can now go in admin panel with http://127.0.0.1:80/admin/

### See all endpoints
For see the all of apis and test you need to go to swagger page with this http://127.0.0.1:80/swagger/

### Create random post ( for development )
For creating some random posts/categorys/comments for make the develop easier use this
```bash
docker-compose -f docker-compose.stage.yml exec sh -c "python manage.py random_data"
```

### Test your project
For testing your project with pytest type this in command line
```bash
docker-compose -f docker-compose.stage.yml exec sh -c "pytest"
```

### Database shema
![drawSQL-image-export-2024-06-29 (1)](https://github.com/Benfoxyy/CBV-DRF-Blog/assets/146076866/968caa8c-8e0b-417d-8403-106d68329766)

<hr>

<h3 align='center'>Thanks for visiting my app, if you have any opinions or seeing bugs; let me know 🙂</h3>
