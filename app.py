from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from models.esrgan import enhance_esrgan
from models.denoiser import denoise_image
from models.enhancer import contrast_enhance

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
