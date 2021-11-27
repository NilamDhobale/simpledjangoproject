FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /hellodjango
WORKDIR /hellodjango
ADD . /hellodjango
COPY requirements.txt /hellodjango/
RUN pip install -r requirements.txt
COPY . /hellodjango/
EXPOSE 5000
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
