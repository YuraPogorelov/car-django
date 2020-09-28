# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /home/car

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \ && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /home/car/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
#COPY ./entrypoint.sh /home/car/entrypoint.sh

# copy project
COPY . /home/car
COPY ./entrypoint.sh /home/car/entrypoint.sh

RUN ["chmod", "+x", "/home/car/entrypoint.sh"]

# run entrypoint.sh
ENTRYPOINT ["/home/car/entrypoint.sh"]