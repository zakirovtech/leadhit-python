import json
import os

from tinydb import TinyDB, Query

from config import settings


db = TinyDB(os.path.join(settings.BASE_DIR, "models/data/db.json"))

if not db.all():
    with open(os.path.join(settings.BASE_DIR, "models/data/init.json"), "r") as f:  # Initialize test db 
        data = json.load(f)

    db.insert_multiple(data)

form_pattern = Query()