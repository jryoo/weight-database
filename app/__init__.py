from flask import Flask

app = Flask(__name__)

# add this after app to avoid circular imports
from app import routes