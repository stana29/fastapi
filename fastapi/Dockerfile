FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

COPY config_docker.ini config.ini

EXPOSE 8000

CMD ["python3", "main.py"]