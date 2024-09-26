import streamlit as st
import pandas as pd
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# Initialize MongoDB connection
db = get_mongo_connection()

# Page header
st.title("Upload CSV Files to Insert Data into Collections")

# Section for uploading CSV file
st.header("Upload CSV for 'users', 'jobs', or 'customers'")

# Collection select box
collection_option = st.selectbox("Select Collection to Upload Data", ("users", "jobs", "customers"))

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Preview the data
    st.write("Data preview:")
    st.write(df)

    # Insert into the selected collection
    if st.button("Insert Data into MongoDB"):
        # Convert the DataFrame to a dictionary and insert into the selected collection
        db[collection_option].insert_many(df.to_dict("records"))
        st.success(f"Data successfully inserted into the '{collection_option}' collection!")
