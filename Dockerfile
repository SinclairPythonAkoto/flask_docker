FROM tiangolo/uwsgi-nginx-flask

WORKDIR .

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]