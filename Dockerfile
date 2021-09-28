FROM django
FROM python:3
ADD . /hellodjango

WORKDIR /hellodjango

#RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]