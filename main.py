
import streamlit as st
from PIL import Image
from predict import predict_disease

st.title("Plant Disease Classification")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Classify'):
        with st.spinner('Classifying...'):
            result = predict_disease(image)
        if result.startswith("Error"):
            st.error(result)
        else:
            st.success(f"The predicted disease is: {result}")