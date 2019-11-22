# Demo API Usage

The application contains sample code for API using python, created image using docker and can be deployed using ansible playbook.

The docker image is available at [docker hub](https://hub.docker.com/repository/docker/lakh0009/demo-api)
and the deployed API is available at [here](http://52.187.255.36/)

This api does contains the *POST* and *GET* method implementation. The required params are `width` and `length`.

For running it you can create virtual environment or use the regular environment.

## For running it locally

Install required libraries using `pip install -r requirements.txt` and afterwards for starting webserver use `python app.py`.

## For running it as a docker image

Build the image using `docker build -t demo-api:latest .` from the project folder directory and start it using `docker run -d -p 80:8080 test-api:latest`

## For deploying it using ansible

Set the appropriate host name in the ***hosts*** file and copy public keys on the server for auth.
Afterwards run the ***playbook.yaml*** using following command `ansible-playbook -i hosts playbook.yaml` which will deploy it to the VM.

NOTE: here the ubuntu dist is used on the remote host and assumed that the PORT 80 is available.
