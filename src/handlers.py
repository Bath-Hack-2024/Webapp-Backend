from flask import Flask, request, jsonify
import json
from firebase_interface import init_firebase
from firebase_admin import firestore
from firebase_admin import storage  
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from data_schemas import weather_station_upload_schema
from datetime import datetime
import config as cfg

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

    # Add user_created to user documetn
    if not user.exists:
        user_ref.set({'user_created': datetime.now()})


    #Add station to user. Stations are also objects with a field 'name' and field "data" and uid
    # Fire store generates a unique id for each station
    station_ref = user_ref.collection('stations').add({'name': station_name, 'data': []})

    station_code = station_ref[1].id


    return build_response({'station_id': station_code}, 200, app)

def upload_data_handler(app: Flask):
    data = request.get_json()

    # Validate the data
    if not data:
        return build_response({'error': 'Request body is required'}, 400, app)
    
    try:
        validate(data, weather_station_upload_schema)
    
    except ValidationError as e:
        return build_response({'error': e.message}, 400, app)
        
    station_id = data.get('station_id').strip()
    lat = data.get('lat')
    lon = data.get('lon')
    elevation = data.get('elevation')
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    barometric_pressure = data.get('barometric_pressure')
    img_url = data.get('img_url')

    # Get search each user in users collection for a station in a station collection for the station_id
    user_collection_ref = db.collection('users')
    users = user_collection_ref.stream()

    for user in users:
        stations = user.reference.collection('stations').stream()

        for station in stations:
            if station.id == station_id:
                station.reference.update({
                    'data': firestore.ArrayUnion([{
                        'lat': lat,
                        'lon': lon,
                        'elevation': elevation,
                        'temperature': temperature,
                        'humidity': humidity,
                        'barometric_pressure': barometric_pressure,
                        'timestamp': datetime.now(),
                        'img_url': img_url
                    }])
                })

                return build_response({'status': 'ok'}, 200, app)


    return build_response({'error': 'Station not found'}, 404, app)

def upload_image_handler(app: Flask):
    if 'file' not in request.files:
        return build_response({'error': 'No file part'}, 400, app)
    
    file = request.files['file']
    
    if file.filename == '':
        return build_response({'error': 'No selected file'}, 400, app)
    
    if not file.filename.endswith('.jpg') :
        return build_response({'error': 'Invalid file type (only jpg)'}, 400, app)
    
    # Upload file to firebase storage
    bucket = storage.bucket()
    blob = bucket.blob(file.filename)
    blob.upload_from_string(file.read(), content_type='image/jpg')

    resource_path = f"{cfg.public_view_url}/{blob.name}?alt=media"



    #retunr file path
    return build_response({'file_path': resource_path }, 200, app)
    