# source: https://docker-curriculum.com/

# python3 as base image
FROM python:3

# copy project to container
WORKDIR /app
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# export port & run webserver
EXPOSE 5000
CMD ["python", "main.py"]
