import threading
from flask import Flask, render_template, url_for

import Freiburg.collect_freiburg as cf

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    data = cf.get_collected_data()
    return render_template('index.html', data=data, rows=len(data))

@app.route('/features')
def features():
    pass

@app.route('/collection')
def collection():
    pass

@app.route('/analyse')
def analyse():
    pass

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

def run():
    app.run(host="0.0.0.0", port=8080)

def start_server():
    thread = threading.Thread(target=run)
    thread.start()


if __name__ == '__main__':
    run()