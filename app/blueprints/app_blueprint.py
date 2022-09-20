from flask import Blueprint, current_app, jsonify, render_template, url_for
import json

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/', methods=['GET'])
@app_blueprint.route('/', defaults={'path': ''})
@app_blueprint.route('/<path:path>')
def app(path):
  jsonFile = current_app.open_resource('static/manifest.json')
  data = json.load(jsonFile)  # Read the JSON into the buffer
  jsonFile.close()  # Close the JSON file
  return render_template('index.html', data=data)