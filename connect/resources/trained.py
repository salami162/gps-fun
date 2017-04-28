import csv
from flask.ext.restful import Resource

from connect import settings
from connect.utils import jsonify_fast as jsonify
from connect.utils.geojsonify import visualize_as_geojson


class Trained(Resource):
    """Trained data set Resource"""

    def get(self):
        """Return trained data set
        """
        locations = []

        with open('./data/{}.csv'.format(settings.DATA_SET_OUTPUT)) as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                loc = [
                    row['lat'],
                    row['lng']
                ]
                locations.append(loc)

        geojson = visualize_as_geojson(locations, sample_scale=1)
        return jsonify(geojson)
