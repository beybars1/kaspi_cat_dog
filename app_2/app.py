from predict import *
import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import warnings


app = Flask(__name__)
warnings.filterwarnings("ignore")

UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        json_file = open(filename)
        result = predict(json_file)
        json_file.close()

        return result


if __name__ == '__main__':
    app.run(port=5555, debug=True, host="0.0.0.0")
