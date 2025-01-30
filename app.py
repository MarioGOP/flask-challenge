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

@app.route('/phase-change-diagram', methods=['GET'])
def get_diagram():
    pressure = request.args.get('pressure', default=10, type=float)
    specific_volume_liquid = (((pressure - 0.05)/4061.22)+0.00105) 
    specific_volume_vapor = (((pressure-10)/-0.3317)+0.0035)
    return jsonify({"specific_volume_liquid": specific_volume_liquid, "specific_volume_vapor": specific_volume_vapor}), 200
