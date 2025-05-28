# 🔍 Deep Learning Image Enhancement Web App

This project is a **Flask-based web application** for enhancing low-quality images using various **deep learning** and **image processing** techniques. It supports multiple enhancement methods such as:

-  ESRGAN (Enhanced Super-Resolution GAN)
-  Image Denoising (e.g., Gaussian, median)
-  Contrast Enhancement (CLAHE)
-  Multimodal combinations

---

##  Features

- Upload and enhance images directly via web UI
- Choose from different enhancement algorithms
- Unique filename generation to avoid collisions
- Auto-cleanup of old files to save disk space
- Extensible architecture (ESRGAN, Denoisers, Enhancers)

---

---

## 🧠 Technologies Used

- **Flask** – Web framework
- **OpenCV** – Image processing
- **PyTorch** – Deep learning models
- **BasicSR** – Super-resolution backbone
- **ESRGAN / GFPGAN / FaceXLib** – Pretrained models (optional)
- **NumPy, Scikit-image** – Image utils

---

## ⚙️ Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/FairozAhmadSheikh/Image_Enhancement_Flask_Web_App
cd image-enhancer-app
```
### Step 2: Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

```
### Step 3: Install requirements
```bash
pip install -r requirements.txt
```
### Step 4: Running the App
```bash
python app.py
```
Then go to: http://localhost:5000

### Sample Use
1 Upload an image.

2 Select the enhancement method:
     ESRGAN – Super-resolution
     Denoise – Noise reduction
     CLAHE – Contrast enhancement
3 View the enhanced image side-by-side.

### Future Ideas
    Add face restoration (GFPGAN)
    Add cartoonization or artistic filters
    Support batch image enhancement
    Add REST API and JWT authentication

### Contributing
Pull requests are welcome! For major changes, open an issue first.

### Author
Fairoz Ahmad Sheikh
AI Researcher | MTech @ IUST Pulwama | Cybersecurity & ML Enthusiast
