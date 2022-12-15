# Flask Docker App

This is a simple Flask app that uses Docker to run the web app.

The goal of the app is to be able to run the Flask app on the local machine as well as the Docker container.

### Run Python File
```
python3 main.py
```

### Introduction to Docker
In order to successfully run the Flask app within the Docker container, first you need to create a `Dockerfile`.
Then after the file has been created, the next step is to create a Docker image.  After the image has been created you are now ready to run the flask app.

### Breaking Down The Dockerfile
The Dockerfile is important because it houses the instructions for building a Docker image along with which libraries and dependencies the Docker image needs.  This can be useful for complex applications that depend on configurations for a specific environment.

A Dockerfile enables the developer to build the Docker image locally on their machine and run the Docker app from any machine that has Docker installed.

The `Dockerfile` should be in the location in the project directory as the Flask file (in this case `main.py`).

**Dockerfile**
```
FROM tiangolo/uwsgi-nginx-flask

WORKDIR .

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]
```
- `FROM tiangolo/uwsgi-nginx-flask` is a public Docker image to tell Docker to use Flask dependencies.
- `WORKDIR .` tells Docker that the working directory is the current directory being used in Docker.
- `COPY . . ` copies the current content of the project directory into the Docker container.
- `EXPOSE 5000` this is signifying the port number the Docker app is going to run from (this has to be the same port mentioned in your Flask app).
- `CMD ["python3", "main.py"]` this is the command to execute the code in the Docker container. `CMD` is telling Docker you want to enter a command; `"python3"` signifies the language and `"main.py"` points to the name of the Flask app that will be deployed.  This command is no different to running the Flask app on the local machine with: `python3 main.py`.

## Building a Docker Image
Once the Dockerfile is complete, then we can create the Docker image for the Flask app.
Navigate to the terminal and enter the following: `docker build -t project_directory .`
```
docker build -t flask_docker:latest .  
```
We can also use the following command to **check if the Docker image build** was successfull or not: `docker image ls project_directory`
```
docker image ls flask_docker
```

## Run Flask App in Docker
Now with the `Dockerfile` and the image successfully built, we are ready to deploy the Flask app with the following line: `docker container run -p docker_port:your_port project_directory`
```
docker container run -p 5000:5000 flask_docker:latest
```