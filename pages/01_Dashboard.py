import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# MongoDB connection
db = get_mongo_connection()

# Collections accessed
invoices = db['invoices']
expenses = db['expenses']
jobs = db['jobs']

st.title("Dashboard")

# Key Metrics
total_revenue = invoices.aggregate([{"$group": {"_id": None, "total": {"$sum": "$amount"}}}])
total_expenses = expenses.aggregate([{"$group": {"_id": None, "total": {"$sum": "$amount"}}}])

st.metric("Total Revenue", f"${list(total_revenue)[0]['total']}")
st.metric("Total Expenses", f"${list(total_expenses)[0]['total']}")
