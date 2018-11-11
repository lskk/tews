import json
import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from mongoengine import *

import tsunami_potential

class Earthquake(Document):
    name = StringField(db_field='name', required=True)
    usgs_id = StringField(db_field='usgsId')
    usgs_name = StringField(db_field='usgsName')
    origin_time = DateTimeField(db_field='originTime')
    usgs_origin_time = DateTimeField(db_field='usgsOriginTime')
    iris_origin_time = DateTimeField(db_field='irisOriginTime')
    noaa_location = StringField(db_field='noaaLocation')
    novianty_rupture_duration = FloatField(db_field='noviantyRuptureDuration')
    novianty_p_wave_dominant_period = FloatField(db_field='noviantyPWaveDominantPeriod')
    novianty_t0xtd = FloatField(db_field='noviantyT0xtd')
    novianty_mw = FloatField(db_field='noviantyMw')
    mw = FloatField(db_field='mw')
    usgs_mw = FloatField(db_field='usgsMw')
    iris_mw = FloatField(db_field='irisMw')
    noaa_tsunami = BooleanField(db_field='noaaTsunami')
    noaa_tsunami_id = IntField(db_field='noaaTsunamiId')
    unknown1 = IntField(db_field='unknown1')
    usgs_depth = FloatField(db_field='usgsDepth')
    collection_name = StringField(db_field='collectionName')
    collection_pos = IntField(db_field='collectionPos')
    epicenter = PointField(db_field='epicenter')
    usgs_epicenter = PointField(db_field='usgsEpicenter')

    meta = {
        'collection': 'earthquake'
    }


app = Flask(__name__)
CORS(app)

connect('ecn', host=os.getenv('MONGODB_URI', 'mongodb://localhost/ecn'))


# t1 = Earthquake(name='Just testing', usgs_depth=5.2)
# t1.save()

def earthquake_to_json(earthquake: Earthquake):
    json_obj = json.loads(earthquake.to_json())
    json_obj['id'] = str(earthquake.id)
    json_obj['originTime'] = earthquake.origin_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    json_obj['irisOriginTime'] = earthquake.iris_origin_time.strftime(
        '%Y-%m-%dT%H:%M:%SZ') if earthquake.iris_origin_time else None
    json_obj['usgsOriginTime'] = earthquake.usgs_origin_time.strftime(
        '%Y-%m-%dT%H:%M:%SZ') if earthquake.usgs_origin_time else None
    return json_obj


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Check /earthquakes'})


@app.route('/earthquakes', methods=['GET'])
def earthquakes_list():
    earthquakes = Earthquake.objects()
    earthquakes_json = [earthquake_to_json(doc) for doc in earthquakes]
    return jsonify({'_embedded': {'earthquakes': earthquakes_json}})


@app.route('/earthquakes/<earthquake_id>', methods=['GET'])
def earthquakes_detail(earthquake_id: str):
    earthquake = Earthquake.objects(id=earthquake_id).first()
    earthquake_json = earthquake_to_json(earthquake)
    return jsonify(earthquake_json)


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
