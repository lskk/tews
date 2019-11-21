import json
import os

from flask import Flask, jsonify, request
from flask_cors import CORS

import tsunami_potential

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)
# t1 = Earthquake(name='Just testing', usgs_depth=5.2)
# t1.save()


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'POST to /tsunamiPotential/predict'})


@app.route('/tsunamiPotential/predict', methods=['POST'])
def tsunami_potential_predict():
    """
    Predict tsunami potential.

    Request body is JSON with {t0, td, mw}

    :param t0: Unnormalized rupture duration variable
    :param td: Unnormalized P-wave dominant period variable
    :param mw: Unnormalized moment magnitude (M_w)
    """
    content = request.get_json()
    t0: float = content['t0']
    td: float = content['td']
    mw: float = content['mw']
    potential = tsunami_potential.predict(t0, td, mw)
    print('Potential: %s' % (potential,))
    return jsonify(potential)
