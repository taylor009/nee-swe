import flask_cors
from flask import Flask, request
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import csv
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = './csv'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    target = UPLOAD_FOLDER
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])

    # If cell check returns false there is a empty cell
    if not csv_cell_checker(filename):
        return 'There is an empty cell in the file'
    # If column and row check returns false the rows and columns do not match what's expected
    if not csv_col_row_check(filename):
        return 'CSV file dose not match format of 3 Columns and 10 Rows'

    file.save(destination)
    response = "File Uploaded Successfully"
    return response


# Helper function to check if there are any empty cells in the csv file.
def csv_cell_checker(file):
    with open(str(file), 'r') as csv_file:
        for row in csv.reader(csv_file):
            if '' in row:
                print('empty cell')
                return False
    return True


# Helper function check the number of columns and rows in the uploaded csv file
def csv_col_row_check(file):
    with open(str(file), 'r') as csv_file:
        columns = csv_file.readline()
        rows = sum(1 for line in csv_file) + 1
    if columns == 3 and rows == 10:
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

flask_cors.CORS(app, expose_headers='Authorization')
