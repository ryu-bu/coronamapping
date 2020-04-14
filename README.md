# coronamapping

4/15/2020 Updates:<br>
added map<br>
added Dockerfile<br>

<strong>Instruction</strong><br>
Install the required packages listed in <i>requirements.txt</i>.</br>
To start the application, clone and move to this repository, then run<br>
```
python app.py
```
Once successfully started, the application will run on the localhost -- check the command line for the right port. <br>

<strong>Docker</strong><br>
Install Docker daemon first if you don't have it <br>
To build the docker image, run<br>
```
docker build -t coronamapping .
```
Once the image is built, run the following command to start the container:<br>
```
docker run -d -p 5000:5000 coronamapping
```
This will run the docker container in the background. The application will be deployed on localhost:5000
