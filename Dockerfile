FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "server.wsgi"]
