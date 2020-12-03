from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import glob

app = Flask(__name__)

UPLOAD_FOLDER = 'upload_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

OUTPUT_FOLDER = 'output_images'
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def uploads_file():


@app.route('/upload_img/<filename>')    # アップロードされたファイルの処理
def uploaded_file(filename):
    return


if __name__ == '__main__':
    app.run()
