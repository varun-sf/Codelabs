FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "codelabs.wsgi:application"]
