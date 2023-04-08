import os
from flask import (Flask, render_template, request)
from utils import file_loading, data_manipulation

app = Flask(__name__)
app.config['DATA_FOLDER'] = os.path.join(app.root_path, 'raw-data')

@app.route("/", methods=['GET', 'POST'])
def welcome_page():
    fileName = file_loading.get_files(app.config['DATA_FOLDER'])

    return render_template('file-list.html', fileName=fileName)

@app.route("/selected-file", methods=['GET', 'POST'])
def load_selected_file():
    fileName = request.form.get('Filename')
    values = data_manipulation.parse_file(
        file_loading.load_file(app.config['DATA_FOLDER'], fileName))

    return render_template('graph-template.html',time=values.time,
                           voltage=values.voltage, capacity=values.capacity,
                           power=values.power, tempBattery=values.tempBattery,
                           tempRadiator=values.tempRadiator)