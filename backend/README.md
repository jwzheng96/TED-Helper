# Backend

```bash
# install backend dependencies
cd ./backend
pipenv install

# go to the virtual env of your computer
# method 1:
pipenv shell

# method 2:
python -m venv env
source env/bin/activate

# init DB
python manage.py db init

# migrate DB
python manage.py db migrate

# upgrade DB
python manage.py db upgrade 

# downgrade DB
python manage.py db downgrade
```


