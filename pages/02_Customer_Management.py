import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# MongoDB connection
db = get_mongo_connection()

# Collections accessed
customers = db['customers']

st.title("Customer Management")

# Display existing customers
st.subheader("Customer List")
customer_list = list(customers.find())

if customer_list:
    for customer in customer_list:
        st.write(f"Name: {customer['customer_name']} | Email: {customer['email']} | Phone: {customer['phone']}")

# Add a new customer
st.subheader("Add New Customer")
new_customer_name = st.text_input("Customer Name")
new_customer_email = st.text_input("Email")
new_customer_phone = st.text_input("Phone")

if st.button("Add Customer"):
    new_customer = {
        "customer_name": new_customer_name,
        "email": new_customer_email,
        "phone": new_customer_phone,
    }
    customers.insert_one(new_customer)
    st.success("Customer added successfully!")
