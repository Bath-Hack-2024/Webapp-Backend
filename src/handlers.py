from flask import Flask, request, jsonify
import json
from firebase_interface import init_firebase
from firebase_admin import firestore

app, db = init_firebase()

def build_response(data, status_code, app: Flask):

    response = app.response_class(
        response=json.dumps(data),
        status=status_code,
        mimetype='application/json'
    )

    return response

def status_hadnler(app: Flask):
    return build_response({'status': 'ok'}, 200, app)

def register_station_handler(app: Flask):
    
    # Accessing parameters from the JSON body
    data = request.get_json()

    if not data:
        return build_response({'error': 'Request body is required'}, 400, app)

    email = data.get('email')
    station_name = data.get('station_name')

    if not email or not station_name:
        return build_response({'error': 'email and station_name are required'}, 400, app)

    user_collection_ref = db.collection('users')
    
    #if user does not exist, create user 
    user_ref = user_collection_ref.document(email)
    user = user_ref.get()

    #Add station to user. Stations are also objects with a field 'name' and field "data" and uid
    # Fire store generates a unique id for each station
    station_ref = user_ref.collection('stations').add({'name': station_name, 'data': []})

    station_code = station_ref[1].id


    return build_response({'station_id': station_code}, 200, app)