curl 192.168.33.10:3000/boards/1/
curl 192.168.33.10:3000/boards/2/
curl 192.168.33.10:3000/boards/a/

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'ecport PATH="#PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo -e 'if command -v pyenv 1>dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc

pyenv install anaconda3-5.0.1
pyenv global anaconda3-5.0.1
python --version
pyenv versions

pip install pipenv
pipenv --version
pipenv --help

eval "$(pipenv --completion)"

pipenv

mkdir myproject
cd myproject
pipenv --python 3.6.4

pipenv shell
. /home/vagrant/.local/share/virtualenvs/myproject-j-SR1M6H/activate
python --version
pipenv run python --version
pipenv --venv

pip run pip list
cat Pipfile
pipenv install django==2.0.2
pipenv shell
pipenv run pip list
pipenv install --dev ipython==6.2.1
cat Pipfile
django-admin starproject myproject
python manage.py runserver

python manage.py runserver
python manager.py runserver 0:3000

django-admin startapp boards
python manage.py startapp boards

python manage.py makemigrations boards

python manage.py makemigrations boards

python manage.py makemigrations boards
python manage.py sqlmigrate boards 0001
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL UNIQUE, "description" varchar(100) NO T NULL);
CREATE INDEX "boards_post_created_by_id_xxx" ON "boards_post" ("created_by_id");
CREATE INDEX "boards_post_topic_id_xxx" ON "boards_post" ("topic_id");
CREATE INDEX "boards_post_updated_by_id_xxxx" ON "boards_post" ("updated_by_id");
COMMIT;

python manage.py migrate
sql3 db.sqlite3
.schema boards_board
.schmea boards_post
.schema boards_topic
python manage.py showmigrations










