from flask import Flask, render_template
import os

from plot import parseURL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/teams')
def teams():
    return render_template('teams.html')
@app.route('/maps.js')
def mapsjs():
    return render_template('maps.js')
@app.route('/data')
def data():
    # urllib.request.urlretrieve("https://vignette.wikia.nocookie.net/supermarioglitchy4/images/f/f3/Big_chungus.png/revision/latest?cb=20200511041102", "./static/images/test.png")

    p = parseURL
    jsonizeCountry = p.countries()
    jsonizeState = p.states()

    IMG_FOLDER = os.path.join('static', 'images')
    app.config['UPLOAD_FOLDER'] = IMG_FOLDER
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test.png')

    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
