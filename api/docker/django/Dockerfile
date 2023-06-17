FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ../.. /code/

RUN python3 manage.py migrate
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model();  \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')  \
    if not User.objects.filter(username='admin').exists() else 0;" | python3 manage.py shell

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]