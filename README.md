# coronamapping

To have it fully function, create .env file in the same directory as app.py then put the following line: <br>
```
API_KEY = your_google_api_key
```
Your google api key has to have Geocoding API and Maps JavaScript API enabled. <br>

<strong>Instruction</strong><br>
Install the required packages listed in <i>requirements.txt</i>.</br>
To start the application, clone this repository and set it as the current directory, then run<br>
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
