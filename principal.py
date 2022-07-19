from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os


def usuario():
	pass

def password():
	pass

EXTENSIONES = ["png", "jpg", "jpeg"]
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = './static/archivos'