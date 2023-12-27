# Instalacja bibliotek Python
pip install -r requirements.txt

# Uruchomienie lokalnie backendu
uvicorn main:app --reload

# Baza danych
PostgreSQL

# Wykonywanie migracji bazy danych
alembic upgrade head