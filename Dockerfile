FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "amadeus_demo/manage.py"]

CMD ["runserver", "0.0.0.0:8080"]

EXPOSE 8080
