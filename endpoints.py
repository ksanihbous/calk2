from flask import Flask, Response, request
from flask_restful import reqparse
from shows import available_shows

import json
import urllib
import logging

app = Flask(__name__)
app.debug = False

@app.route("/calculator/", methods=['GET'])
def get_sum():
    if(request.method== 'GET'):
        parser = reqparse.RequestParser()
        parser.add_argument('add')
        parser.add_argument('sub')
        args = parser.parse_args()
        if args['add'] is None:
            jsonresponse = {'Error': str('Missing Arguments')}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 404
        if args['sub'] is None:
            jsonresponse = {'Error': str('Missing Arguments')}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 404

        add = int(args['add'])
        sub = int(args['sub'])
        total = add-sub
        jsonresponse = {'Response': str(total)}
        return Response(json.dumps(jsonresponse), mimetype='application/json'), 400


@app.route("/shows/", methods=['GET'])
def get_available_shows():
    if(request.method == 'GET'):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('season')
        parser.add_argument('episode')
        args = parser.parse_args()
        if args['name'] is None:
            jsonresponse = {'Error': str('Missing argument name')}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 404
        if args['season'] is None:
            jsonresponse = {'Error': str('Missing argument season')}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 404

        try:
            show = args['name']
            season = args['season']
            episode = args['episode']
        except ValueError as ve:
            jsonresponse = {'Error': str(ve)}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 400
        except NotImplementedError as nie:
            jsonresponse = {'Error': str(nie)}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 501
        except FileNotFoundError as fnfe:
            jsonresponse = {'Error': str(fnfe)}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 404
        else:
            jsonresponse = {'Response': str(args)}
            return Response(json.dumps(jsonresponse), mimetype='application/json'), 400

@app.route("/shows/all", methods=['GET'])
def get_all_shows():
    response = available_shows.get_all_shows()
    jsonresponse = {'Response': str(response)}

    return Response(json.dumps(jsonresponse), mimetype='application/json'), 400