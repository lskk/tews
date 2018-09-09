import json

from flask import Flask, jsonify, request

from mongoengine import *


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

connect('ecn')


# t1 = Earthquake(name='Just testing', usgs_depth=5.2)
# t1.save()

def earthquake_to_json(earthquake: Earthquake):
    return json.loads(earthquake.to_json())

@app.route('/')
def hello():
    return jsonify({'message': 'Check /earthquakes'})


@app.route('/earthquakes')
def earthquakes_list():
    earthquakes = Earthquake.objects()
    earthquakes_json = [earthquake_to_json(doc) for doc in earthquakes]
    return jsonify({'_embedded': {'earthquakes': earthquakes_json}})


@app.route('/earthquakes/<earthquake_id>')
def earthquakes_detail(earthquake_id: str):
    earthquake = Earthquake.objects(id=earthquake_id)
    earthquake_json = earthquake_to_json(earthquake)
    return jsonify(earthquake_json)
