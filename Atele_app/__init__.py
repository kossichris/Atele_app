# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.ClientController import api as client_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API ATELE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(client_ns, path='/client')