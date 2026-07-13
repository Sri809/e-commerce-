import streamlit as st
import pickle
import pandas as pd

# Load files
products = pickle.load(open("products.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("🛒 E-Commerce Product Recommendation System")

product_name = st.text_input("Enter Product Name")

if st.button("Recommend"):

    if product_name in products["name"].values:

        index = products[products["name"] == product_name].index[0]

        distances = similarity[index]

        product_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        st.subheader("Recommended Products")

        for i in product_list:
            st.write(products.iloc[i[0]]["name"])

    else:
        st.error("Product not found!")