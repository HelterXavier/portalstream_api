from dotenv import load_dotenv
import os

load_dotenv()

URL_BASE = os.getenv("URL_BASE")
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("Environment variable MONGODB_URI has not been defined")
