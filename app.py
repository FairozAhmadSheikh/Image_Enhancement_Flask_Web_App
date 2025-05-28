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
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        img = request.files["image"]
        method = request.form["method"]

        filename = secure_filename(img.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(input_path)

        output_path = os.path.join(OUTPUT_FOLDER, f"output_{filename}")

        if method == "esrgan":
            enhance_esrgan(input_path, output_path)
        elif method == "denoise":
            denoise_image(input_path, output_path)
        elif method == "clahe":
            contrast_enhance(input_path, output_path)

        return render_template("index.html", input_img=input_path, output_img=output_path)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)