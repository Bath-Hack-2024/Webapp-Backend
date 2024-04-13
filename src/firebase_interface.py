import firebase_admin
from firebase_admin import credentials, App
from firebase_admin import firestore

import config as cfg

def init_firebase():
    cred = credentials.Certificate(cfg.firebase_key_file)
    app = firebase_admin.initialize_app(cred, {'storageBucket': cfg.bucket})
    db = firestore.client()
    return app, db
