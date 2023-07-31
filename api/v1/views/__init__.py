#!/usr/bin/python3

""" Initialize Blueprint for the API """

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
'''The blueprint for the Airbnb API.'''

from api.v1.views.cities import *
from api.v1.views.index import *
from api.v1.views.states import *
