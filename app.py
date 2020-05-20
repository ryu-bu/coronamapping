from flask import Flask, render_template

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
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
