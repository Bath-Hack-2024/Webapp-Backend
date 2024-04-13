from flask import Flask
import json

def status_hadnler(app: Flask):
    responce_data = {
        "status": "OK"
    }

    response = app.response_class(
        response=json.dumps(responce_data),
        status=200,
        mimetype='application/json'
    )

    return response