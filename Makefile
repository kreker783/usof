dep_install:
	pip3 install -r requirements.txt

update_db:
	python3 manage.py makemigrations
	python3 manage.py migrate

run_server: dep_install update_db
	python3 manage.py runserver