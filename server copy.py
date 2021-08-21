import threading
from flask import Flask, render_template, url_for, request

import Freiburg.collect_freiburg as cf

#app = Flask(__name__)
app = Flask('')
#app = Flask(__name__, static_folder='.', root_path='/home/runner')

@app.route('/')
@app.route('/home')
def home():
    if request.method == 'POST':
        value = request.form['input']
        return value
    if request.method == 'GET':
        data = cf.get_collected_data()
        return render_template('index.html', data=data, rows=len(data))

@app.route('/visualization')
def visualization():
    if request.method == 'POST':
        value = request.form['input']
        return value
    if request.method == 'GET':
        return render_template('visualization.html')

@app.route('/features')
def features():
    if request.method == 'POST':
        value = request.form['input']
        return value
    if request.method == 'GET':
        return render_template('features.html')

@app.route('/collection')
def collection():
    if request.method == 'POST':
        value = request.form['input']
        return value
    if request.method == 'GET':
        return render_template('collection.html')

@app.route('/analyse')
def analyse():
    if request.method == 'POST':
        value = request.form['input']
        return value
    if request.method == 'GET':
        return render_template('analysis.html')

@app.route('/datenschutz')
def datenschutz():
    if request.method == 'POST':
        value = request.form['input']
        return value
    if request.method == 'GET':
        return render_template('datenschutz.html')

@app.route('/impressum')
def impressum():
    if request.method == 'POST':
        value = request.form['input']
        return value
    if request.method == 'GET':
        return render_template('impressum.html')

def run():
    app.run(host="0.0.0.0", port=8080)

def start_server():
    thread = threading.Thread(target=run)
    thread.start()


if __name__ == '__main__':
    run()