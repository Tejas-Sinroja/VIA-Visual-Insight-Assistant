import streamlit as st
from PIL import Image
from utils.preprocess import preprocess_image
from models.model import load_food_model, predict_food_item
from utils.insights import get_calories_info, get_protein_info
from templates.layout import footer

# Helper functions
def model_predict(img, model):
    processed_img = preprocess_image(img)
    return predict_food_item(processed_img, model)

def display_calories_info(food_item):
    calorie_level, suggestion = get_calories_info(food_item)
    st.write(f"**Food Item Selected:** {food_item}")
    st.info(f"**Calories Level:** {calorie_level}")
    st.write(f"**Suggestion:** {suggestion}")
    return calorie_level, suggestion

def display_protein_info(food_item):
    protein_level, protein_info = get_protein_info(food_item)
    st.write(f"**Food Item Selected:** {food_item}")
    st.info(f"**Protein per 100 gm:** {protein_level} g")
    st.write(f"**Protein Level:** {protein_info}")
    return protein_level, protein_info

MODEL_OPTIONS = {
    "CNN v1": "cnnv1.h5",
    "CNN v2": "cnnv2.h5",
    "CNN v3": "cnnv3.h5",
    "CNN v4 under maintenance": "cnnv4.h5",
    "Improved CNN v2": "improved_cnnv2.h5",
    "Improved CNN v21": "improved_cnnv21.h5",
    "Inception v3 under maintenance": "inceptionv3.h5",
}

st.title("Visual Insight Assistant")
st.header("Upload an image of food items and select a model")

selected_model_name = st.selectbox("Select a Model for Prediction", list(MODEL_OPTIONS.keys()))
selected_model_path = MODEL_OPTIONS[selected_model_name]

model = load_food_model(selected_model_path)
st.success(f"Loaded model: {selected_model_name}")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    food_prediction = None  

    if st.button("Predict"):
        food_prediction = model_predict(img, model)
        st.write(f"**Prediction:** Detected Food Item - *{food_prediction}*")
col1, col2 = st.columns(2)
with col1:
    if st.button("Calories"):
        prediction = model_predict(img, model)
        if uploaded_file is not None:
            calorie_level, suggestion = display_calories_info(prediction)
        else:
            st.warning("Please upload an image first.")

with col2:
    if st.button("Protein"):
        prediction = model_predict(img, model)
        if uploaded_file is not None:
            p_level, p = display_protein_info(prediction)
        else:
            st.warning("Please upload an image first.")

footer()

