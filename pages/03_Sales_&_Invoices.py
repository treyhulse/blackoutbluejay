import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# MongoDB connection
db = get_mongo_connection()

# Collections accessed
sales_orders = db['sales_orders']
invoices = db['invoices']

st.title("Sales and Invoices Management")

# Display unpaid invoices
st.subheader("Unpaid Invoices")
unpaid_invoices = list(invoices.find({"status": "Unpaid"}))

if unpaid_invoices:
    for invoice in unpaid_invoices:
        st.write(f"Invoice {invoice['invoice_number']} | Amount: {invoice['amount']} | Due: {invoice['due_date']}")
else:
    st.write("No unpaid invoices")

# Add a new sales order (can be extended)
st.subheader("Add New Sales Order")
new_order_number = st.text_input("Order Number")
new_order_total = st.number_input("Total Amount", min_value=0.0)
if st.button("Add Sales Order"):
    new_order = {
        "order_number": new_order_number,
        "total_amount": new_order_total,
        "status": "Shipped",
        "date": "2024-09-25",
    }
    sales_orders.insert_one(new_order)
    st.success("Sales order added successfully!")
