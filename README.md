# coronamapping

restAPIs: https://api.covid19api.com/summary and https://covidtracking.com/api/states . Numbers used in this project are from these two sources. <br>

To have it fully function, create a .env file in the same directory as app.py then put the following line: <br>
```
API_KEY = your_google_api_key
```
Your google api key has to have Geocoding API and Maps JavaScript API enabled. <br>

<strong>Instruction</strong><br>
Install the required packages listed in <i>requirements.txt</i>.</br>
To start the application, clone this repository and go to flask directory, and run<br>
```
flask run
```
Once successfully started, the application will run on the localhost -- check the command line for the right port. <br>

<strong>Docker</strong><br>
Install Docker daemon first if you don't have it <br>
To build the docker image, run<br>
```
docker-compose build
```
Once the image is built, run the following command to start the container:<br>
```
docker-compose run
```
This will run the docker container in the background. The application will be deployed on localhost

<strong>Note</strong><br>
It might take 5-15 seconds to open each page.
