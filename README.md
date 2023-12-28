# Backend
## Instalacja bibliotek Python
```
pip install -r requirements.txt
```

## Uruchomienie lokalnie backendu
```
uvicorn main:app --reload
```

## Baza danych
`PostgreSQL`
## Wykonywanie migracji bazy danych

Wygenerowanie migracji ze zmianami wprowadzonymi w models.py
```
alembic revision --autogenerate -m "Lorem Ipsum Dolor Sit Amet"
```

Uruchomienie ostatnich migracji na bazie danych
```
alembic upgrade head
```

## Troubleshooting

Komendy dotyczące backendu wywołujemy z poziomu folderu `backend/app`
