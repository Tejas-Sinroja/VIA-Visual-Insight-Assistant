from tensorflow.keras.preprocessing import image
import numpy as np

from PIL import Image
import numpy as np
from keras.preprocessing import image

def preprocess_image(img):
    """Preprocess the uploaded image for prediction."""
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    img = img.resize((299, 299))  
    img_array = image.img_to_array(img) 
    img_array = img_array / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  
    return img_array