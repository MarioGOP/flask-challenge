from flask import Flask, request, jsonify, render_template
from random import choice

app = Flask(__name__)

damaged_system = {
  "navigation": "NAV-01",
  "communications": "COM-02",
  "life_support": "LIFE-03",
  "engines": "ENG-04",
  "deflector_shield": "SHLD-05"
}
last_repaired = ""

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status', methods=['GET'])
def get_status():
    key = choice(list(damaged_system.keys()))
    global last_repaired
    last_repaired = damaged_system[key]
    return jsonify({"damaged_system": key}), 200

@app.route('/repair-bay', methods=['GET'])
def get_repair_bay():
    return render_template("repair.html", last_repaired=last_repaired)

@app.route('/teapot', methods=['POST'])
def post_teapot():
    return jsonify(), 418