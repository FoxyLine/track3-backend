## linux 
python3 -m venv venv

source venv/bin/activate

pip3 install -r reqs.txt

## widnows
py (или путь к питону)  -m venv venv

venv/Scripts/activate.bat - выполнить
pip intall -r reqs.txt



создать файл db.sqlite

alembic upgrade head 

uvicorn main:app --reload
