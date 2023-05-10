FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

RUN python amadeus_demo/manage.py collectstatic --noinput

ENTRYPOINT ["python", "amadeus_demo/manage.py"]

CMD ["runserver", "0.0.0.0:8000"]

EXPOSE 8000