from bson import ObjectId
import streamlit as st
import pandas as pd
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# Initialize MongoDB connection
db = get_mongo_connection()

# Page header
st.title("Manage Collections with Editable Table")

# Section 1: Create a New Collection
st.header("Create a New Collection")

collection_name = st.text_input("Enter Collection Name")

if st.button("Create Collection"):
    if collection_name:
        db[collection_name].insert_one({"created": True})
        st.success(f"Collection '{collection_name}' created successfully!")
    else:
        st.error("Please provide a valid collection name.")

# Section 2: View, Edit, and Delete Collections
st.header("View, Edit, or Delete Collections")

collections = db.list_collection_names()

if collections:
    selected_collection = st.selectbox("Select a Collection", collections)
    
    # Display and edit documents in an interactive table
    st.subheader(f"Documents in {selected_collection}")
    collection = db[selected_collection]
    documents = list(collection.find())

    if documents:
        # Convert MongoDB documents to a format that can be displayed in a table
        for doc in documents:
            doc["_id"] = str(doc["_id"])  # Convert ObjectId to string for display
        
        # Convert documents to DataFrame
        documents_df = pd.DataFrame(documents)

        # Set up AgGrid for editable table
        gb = GridOptionsBuilder.from_dataframe(documents_df)
        gb.configure_pagination()
        gb.configure_default_column(editable=True)
        grid_options = gb.build()

        # Display the editable table
        grid_response = AgGrid(
            documents_df,
            gridOptions=grid_options,
            update_mode=GridUpdateMode.VALUE_CHANGED,
            fit_columns_on_grid_load=True,
        )

        updated_data = grid_response["data"]

        # Convert updated data back to list of dictionaries for comparison
        updated_data_list = updated_data.to_dict("records")

        # Check for changes and update the database
        if updated_data_list != documents:
            for new_row in updated_data_list:
                _id = new_row["_id"]
                del new_row["_id"]  # Remove the ID before updating the document
                
                # Update the document in MongoDB
                collection.update_one({"_id": ObjectId(_id)}, {"$set": new_row})
            st.success("Changes saved to the database!")
    else:
        st.write("No documents found in this collection.")

    # Section 3: Delete Collection
    st.subheader(f"Delete Collection '{selected_collection}'")

    if st.button("Delete Collection"):
        db.drop_collection(selected_collection)
        st.success(f"Collection '{selected_collection}' deleted successfully!")
else:
    st.write("No collections available yet.")
