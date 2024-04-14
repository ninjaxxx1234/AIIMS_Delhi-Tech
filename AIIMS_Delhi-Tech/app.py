import json
from flask import Flask, send_file, send_from_directory, jsonify
import cv2



app = Flask(__name__)


@app.route('/rr')
def get_rrfile():
    filename = open('RR.txt', "r")
    values = filename.read()
    return values


@app.route('/vte')
def get_vtefile():
    filename = open('VTe.txt', "r")
    file = open('time.txt', 'r')
    value = file.read
    values = filename.read()
    return values


@app.route('/peep')
def get_peepfile():
    filename = open('PEEP.txt', "r")
    values = filename.read()
    return values


@app.route('/pip')
def get_pipfile():
    filename = open('PIP.txt', "r")
    values = filename.read()
    return values


@app.route('/fio2')
def get_fio2file():
    filename = open('FiO2.txt', "r")
    values = filename.read()
    return values


@app.route('/sp')
def get_spfile():
    filename = open('SP.txt', "r")
    values = filename.read()
    return values

@app.route('/tinsp')
def get_tinspfile():
    filename = open('Tinsp.txt', "r")
    values = filename.read()
    return values

@app.route('/rrf')
def get_rrftestfile():
    filename = open('RR_final.txt', "r")
    file = open('time.txt', 'r')
    value = file.read()
    values = filename.read()
    return value, values


@app.route('/vtef')
def get_vteftestfile():
    filename = open('VTe_final.txt', "r")
    file = open('time.txt', 'r')
    value = file.read()
    values = filename.read()
    return value, values


@app.route('/peepf')
def get_peepftestfile():
    filename = open('PEEP_final.txt', "r")
    file = open('time.txt', 'r')
    value = file.read()
    values = filename.read()
    return value, values


@app.route('/pipf')
def get_pipftestfile():
    filename = open('PIP_final.txt', "r")
    file = open('time.txt', 'r')
    value = file.read()
    values = filename.read()
    return value, values


@app.route('/fio2f')
def get_fio2ftestfile():
    filename = open('FiO2_final.txt', "r")
    file = open('time.txt', 'r')
    value = file.read()
    values = filename.read()
    return value, values


@app.route('/spf')
def get_spftestfile():
    filename = open('SP_final.txt', "r")
    file = open('time.txt', 'r')
    value = file.read()
    values = filename.read()
    return value, values


@app.route('/data')
def get_json_data():
    with open("json.txt", "r") as file:
        json_data = json.load(file)
    return jsonify(json_data)




@app.route('/img/threshold.png')
def get_img():
    image_path = 'threshold.png'
    return send_file(image_path, mimetype='image/jpeg')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
