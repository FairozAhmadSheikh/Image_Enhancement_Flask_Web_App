import cv2
import numpy as np
from PIL import Image
import torch
from torchvision.transforms import ToTensor, ToPILImage
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

def enhance_esrgan(input_path, output_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGANer(
        scale=4,
        model_path='weights/RealESRGAN_x4plus.pth',
        model=RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32),
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=True
    )
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)
    output, _ = model.enhance(img, outscale=4)
    cv2.imwrite(output_path, output)