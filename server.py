import threading
from flask import Flask, render_template, url_for, request

import Freiburg.collect_freiburg as cf

#app = Flask(__name__)
app = Flask('')
#app = Flask(__name__, static_folder='.', root_path='/home/runner')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Submit':
            cf.update_data_viz(request.form['color'], request.form['bg_color'])
            data = cf.get_collected_data()
            return render_template('index.html', data=data, rows=len(data)-2)
        else:
            data = cf.get_collected_data()
            return render_template('index.html', data=data, rows=len(data)-2)
    elif request.method == 'GET':
        data = cf.get_collected_data()
        return render_template('index.html', data=data, rows=len(data)-2) # last line and first line

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/collection')
def collection():
    return render_template('collection.html')

@app.route('/analyse')
def analyse():
    return render_template('analysis.html')

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
