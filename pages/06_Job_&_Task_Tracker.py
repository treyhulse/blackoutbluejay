import streamlit as st
from pymongo import MongoClient
from utils.mongo_connection import get_mongo_connection

# MongoDB connection
db = get_mongo_connection()

# Collections accessed
jobs = db['jobs']

st.title("Job and Task Tracker")

# Display all jobs
st.subheader("Job List")
job_list = list(jobs.find())

if job_list:
    for job in job_list:
        st.write(f"Job: {job['job_title']} | Location: {job['location']} | Status: {job['status']}")

# Add a new job
st.subheader("Add New Job")
new_job_title = st.text_input("Job Title")
new_job_location = st.text_input("Job Location")
if st.button("Add Job"):
    new_job = {
        "job_title": new_job_title,
        "location": new_job_location,
        "status": "Scheduled",
    }
    jobs.insert_one(new_job)
    st.success("Job added successfully!")
