#Using lightweight alpine image
FROM python:3.10-alpine

#Install packages from pipenv
RUN apk update
RUN pip install --no-cache-dir pipenv

#Defining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY cashman ./cashman

#Install API dependencies
RUN pipenv install --system --deploy

#Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]