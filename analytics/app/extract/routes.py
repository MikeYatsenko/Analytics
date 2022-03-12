from flask_restful import Resource
from flask import jsonify
from app.extract import api
from app.extract.utils import analytics_run


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Analytics(Resource):
    def get(self):
        get_result = analytics_run()
        return jsonify(get_result)


api.add_resource(HelloWorld, '/')
api.add_resource(Analytics, '/analytics')
