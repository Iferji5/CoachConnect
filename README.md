# CoachConnect
Plataforma Django para entrenador y alumnos.

## Requisitos
- Python 3.12, Django 5
- Crear `.env` con `DJANGO_SECRET_KEY=...`

## Desarrollo rápido
```bash
python -m venv .venv && .\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
