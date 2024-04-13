import os
from dotenv import load_dotenv
load_dotenv()

port = os.getenv("PORT")
debug_mode = os.getenv("DEBUG_MODE")
app_config = {"TESTING": False}
firebase_key_file = os.getenv("FIREBASE_API_KEY_FILE")
bucket = "back-hack-2024.appspot.com"
public_view_url = "https://firebasestorage.googleapis.com/v0/b/back-hack-2024.appspot.com/o"



