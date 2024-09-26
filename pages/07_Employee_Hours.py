import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# MongoDB connection
db = get_mongo_connection()

# Collections accessed
employee_hours = db['employee_hours']

st.title("Employee Hours Tracker")

# Display employee work hours
st.subheader("Employee Hours")
employee_hours_list = list(employee_hours.find())

if employee_hours_list:
    for record in employee_hours_list:
        st.write(f"Employee ID: {record['employee_id']} | Hours Worked: {record['hours_worked']} | Date: {record['date']}")

# Add a new employee hours record
st.subheader("Add Work Hours")
employee_id = st.number_input("Employee ID", min_value=1)
hours_worked = st.number_input("Hours Worked", min_value=0.0)
if st.button("Add Hours"):
    new_hours_record = {
        "employee_id": employee_id,
        "hours_worked": hours_worked,
        "date": "2024-09-25"
    }
    employee_hours.insert_one(new_hours_record)
    st.success("Work hours added successfully!")
