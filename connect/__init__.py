from flask import Flask, render_template
from flask.ext import restful
from flask_cors import CORS

from connect import settings


app = Flask(__name__)
app.config.from_object(settings)
CORS(app)
api = restful.Api(app)


@app.route('/healthcheck')
def healthcheck():
    # The healthcheck returns status code 200
    return 'OK'


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Limin'}  # fake user
    return render_template('index.html', user=user)


from connect import resources  # noqa
