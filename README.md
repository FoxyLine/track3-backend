python3 -m venv venv
source venv/bin/activate
pip3 install -r reqs.txt

создать файл db.sqlite

alembic upgrade head 

uvicorn main:app --reload
