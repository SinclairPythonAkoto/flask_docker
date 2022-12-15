FROM tiangolo/uwsgi-nginx-flask

WORKDIR .

COPY . .

EXPOSE 5001

CMD ["python3", "main.py"]