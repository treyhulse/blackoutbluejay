import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# MongoDB connection
db = get_mongo_connection()

# Collections accessed
expenses = db['expenses']

st.title("Expense Management")

# Display all expenses
st.subheader("Expense List")
expense_list = list(expenses.find())

if expense_list:
    for expense in expense_list:
        st.write(f"Description: {expense['description']} | Amount: {expense['amount']} | Status: {expense['status']}")

# Add a new expense
st.subheader("Add New Expense")
new_expense_desc = st.text_input("Expense Description")
new_expense_amount = st.number_input("Amount", min_value=0.0)
if st.button("Add Expense"):
    new_expense = {
        "description": new_expense_desc,
        "amount": new_expense_amount,
        "status": "Unpaid",
    }
    expenses.insert_one(new_expense)
    st.success("Expense added successfully!")
