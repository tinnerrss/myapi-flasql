from models import app
from flask import jsonify

@app.route('/')
def home():
  return jsonify(message='welcome home!')