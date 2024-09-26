import streamlit as st
from utils.mongo_connection import get_collection

st.title("Fencing Company App")

# Fetch the collection
collection = get_collection("example_collection")

# Example: Get number of documents in the collection
st.write(f"Number of records in collection: {collection.count_documents({})}")
