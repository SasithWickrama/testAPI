import random
import requests
#from log import Logger
from flask import Flask, request, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

#logger = Logger('server_requests', 'logs/server_requests')

def random_ref(length):
    sample_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join((random.choice(sample_string)) for x in range(length))


class SuspendResume(Resource):
    def post(self):
        ref = random_ref(15)
        data = request.get_json()
        #logger.info(ref + " - " + str(data))

        if data['action'] == 'suspend':
            return {'msg' : 'Success'}
        if data['action'] == 'resume':
            return {'msg' : 'Error'}

api.add_resource(SuspendResume, '/sltdevops/apiv1/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7500)