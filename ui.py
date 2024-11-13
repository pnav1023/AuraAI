import streamlit as st
from openai_query import get_products

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = st.image(uploaded_file, caption='Uploaded Image.', use_container_width=True)

products = get_products(uploaded_file)
st.write(products)