from connect import api
from connect.resources.raw import Raw
from connect.resources.trained import Trained

# resource for raw data set
api.add_resource(Raw, '/v1/raw')
# resource for trained data set
api.add_resource(Trained, '/v1/trained')
