import os

import flask_cors
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = './csv'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/upload', methods=['POST'])
def upload_file():
    target = UPLOAD_FOLDER
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    response="File Uploaded"
    return response



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

flask_cors.CORS(app, expose_headers='Authorization')
