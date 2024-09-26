import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# MongoDB connection
db = get_mongo_connection()

# Collections accessed
inventory = db['inventory']

st.title("Inventory Management")

# Display current inventory
st.subheader("Current Inventory")
inventory_list = list(inventory.find())

if inventory_list:
    for item in inventory_list:
        st.write(f"Product: {item['product_name']} | Quantity: {item['quantity']} | Status: {item['status']}")

# Low stock alert
st.subheader("Low Stock Alerts")
low_stock_items = inventory.find({"status": "Low Stock"})
if low_stock_items:
    for item in low_stock_items:
        st.write(f"Low stock for {item['product_name']} - Only {item['quantity']} left!")
