import os
from dotenv import load_dotenv
load_dotenv()

port = os.getenv("PORT")
debug_mode = os.getenv("DEBUG_MODE")
app_config = {"TESTING": False}
firebase_key_file = os.getenv("FIREBASE_API_KEY_FILE")



