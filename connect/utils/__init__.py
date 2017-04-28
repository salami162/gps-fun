import ujson
from flask import Response
import csv
from connect.models.location import Location

# Result of haversine((lat+1, lng), (lat, lng)) for all combinations of lat, lng
KILOMETERS_PER_DEGREE_LATITUDE = 111.1338401207391

def read_lat_lng_list_from_file():
    locations = []
    with open('./data/wwc_conf_dataset_tiny.csv') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            loc = Location(
                lat=row['dropoff_lat'],
                lng=row['dropoff_lng']
            )
            locations.append(loc)
    return locations

def jsonify_fast(*args, **kwargs):
    return Response(
        ujson.dumps(dict(*args, **kwargs)),
        mimetype='application/json'
    )

