# Social_app

Steps to setup

1. git clone
2. python3 -m venv env
3. .env/bin/activate
4. cd Social_app
5. pip install -r requirements.txt
6. docker run -d --name django-db -p 5432:5432 -e POSTGRES_PASSWORD=pass1234 -e POSTGRES_USER=admin -e POSTGRES_DB=djangodb postgres:13-alpine
7. python2 manage.py runserver
 if facing issue with 7th command, your docker container probably not running,
 run docker ps -a or sudo docker ps -a
 copy container_id,
 run sudo docker start <container_id>
 
 API URLS,
 1. api/userview - GET / POST
    POST KEYWORDS
      action = follow/ unfollow
      id = id of the user to follow/unfollow
 
 2. api/register - POST
      POST KEYWORDS
        username = str
        first_name = str
        last_name = str 
        email = email 
        birth_date = date_time 'YYYY-MM-DD' format
        password1 = Complex,[ validation applied ]
        password2 = retype password1
        
 3. api/status - GET / POST
      POST KEYWORDS
          status = str
