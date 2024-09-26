import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# Initialize MongoDB connection
db = get_mongo_connection()

# Page header
st.title("Manage Collections")

# Section 1: Create a New Collection
st.header("Create a New Collection")

collection_name = st.text_input("Enter Collection Name")

if st.button("Create Collection"):
    if collection_name:
        db[collection_name].insert_one({"created": True})
        st.success(f"Collection '{collection_name}' created successfully!")
    else:
        st.error("Please provide a valid collection name.")

# Section 2: List and View Collections
st.header("View Collections")
collections = db.list_collection_names()

if collections:
    selected_collection = st.selectbox("Select a Collection", collections)
    
    st.subheader(f"Documents in {selected_collection}")
    collection = db[selected_collection]
    
    # Display the first few documents from the selected collection
    documents = list(collection.find().limit(10))  # Limit to 10 documents for display
    if documents:
        st.write(documents)
    else:
        st.write("No documents found in this collection.")
else:
    st.write("No collections available yet.")
