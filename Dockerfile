# Using a small version of python for small final image size
FROM python:3.7-slim

# Working inside the /app directory
RUN mkdir /app
WORKDIR /app

# Install libgomp1 (needed by xgboost)

RUN apt-get clean && apt-get update && apt-get install -y libgomp1

# Copying only the requirements file and then installing them
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copying all of your code
ADD . /app

# Exposing port so that --publish-all can work
EXPOSE 80

# This is the command that will be executed to run your code into a docker container
CMD ["uvicorn", "app:app", "--port", "80", "--host", "0.0.0.0"]
