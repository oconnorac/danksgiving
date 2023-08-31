# use an official Python runtime as the base image
FROM python:3.8

# set the working directory within the container
WORKDIR /app

# copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the entire contents of the app directory into the container at /app
COPY app /app/

# copy the run.py file into the container at /app
COPY run.py /app/

# make port 80 available to the world outside this container
EXPOSE 80

# define environment variable to run Flask in production mode
ENV FLASK_ENV=production

# run app.py when the container launches
CMD ["python", "run.py"]