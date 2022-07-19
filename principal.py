from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os


def comprueba_fondo():
	pass

DOCUMENTOS = ["doc", "docx"]

EXTENSIONES = ["png", "jpg", "jpeg"]
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = './static/archivos'