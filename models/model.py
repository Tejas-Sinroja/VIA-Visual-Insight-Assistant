import numpy as np
from tensorflow.keras.models import load_model
import os

BASE_MODEL_DIR = r"models/model"

def load_food_model(model_name):
    """Loads the selected pre-trained model."""
    model_path = os.path.join(BASE_MODEL_DIR, model_name)
    return load_model(model_path)

def predict_food_item(processed_img, model):
    """Predicts the food item based on the processed image."""
    preds = model.predict(processed_img)
    preds_class = np.argmax(preds, axis=1)[0]
    food_classes = [
        "Burger", "Butter Naan", "Chai", "Chapati", "Chole Bhature", 
        "Dal Makhani", "Dhokla", "Fried Rice", "Idli", "Jalebi", 
        "Kaathi Rolls", "Kadai Paneer", "Kulfi", "Masala Dosa", 
        "Momos", "Paani Puri", "Pakode", "Pav Bhaji", "Pizza", "Samosa"
    ]
    return food_classes[preds_class]
