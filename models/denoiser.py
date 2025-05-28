import cv2
import numpy as np
from keras.models import load_model
from utils.helpers import resize_image

model = load_model('weights/denoiser_model.h5')

def denoise_image(input_path, output_path):
    img = resize_image(input_path, (128, 128))
    img_input = img.astype('float32') / 255.0
    img_input = np.expand_dims(img_input, axis=0)

    denoised = model.predict(img_input)[0]
    denoised = (denoised * 255).astype(np.uint8)
    cv2.imwrite(output_path, cv2.resize(denoised, (img.shape[1], img.shape[0])))