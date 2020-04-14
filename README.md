# coronamapping

4/15/2020 Updates:
added map
added Dockerfile

<strong>Instruction</strong><br>
Install the required packages listed in <i>requirements.txt</i>.</br>
To start the application, clone and move to this repository, then <br>
```
python app.py
```
Once successfully started, the application will run on the localhost -- check the command line for the right port. <br>

<strong>Docker</strong><br>
Install Docker daemon if you haven't. <br>
To build docker image, <br>
```
docker build -t coronamapping .
```
Once built, <br>
```
docker run -d -p 5000:5000 coronamapping
```
This will allow run the docker container in background. The application will be deployed on localhost:5000
