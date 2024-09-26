import streamlit as st

# Set the title for the homepage
st.title("📊 Back-Office Business Management App")

# Introduction
st.subheader("Welcome to your streamlined business management solution!")
st.write("""
This app is designed to help small businesses efficiently manage their back-office operations. 
From tracking customers and sales, to managing inventory, monitoring employee hours, and tracking job progress—everything you need is at your fingertips!
""")

# Features Overview
st.header("Key Features")
st.write("""
- **📋 Customer Management**: Manage your customers’ details, track purchase history, and maintain updated contact information.
- **💰 Sales & Invoices**: Track sales orders and manage invoices with ease. View paid and unpaid invoices and ensure timely payments.
- **📦 Inventory Management**: Monitor your product inventory, manage suppliers, and get alerts when stock is running low.
- **💸 Expense Management**: Keep an eye on your business expenses. Easily track and categorize costs to ensure you're staying on budget.
- **📅 Job & Task Tracker**: Stay on top of your jobs and tasks. Track progress, assign tasks, and monitor ongoing jobs.
- **⏱️ Employee Hours Management**: Track employee hours worked and manage payroll with accurate timesheets.
""")

# Quick Links to Pages
st.header("Get Started")
st.write("Navigate to the key sections of the app:")
st.markdown("""
- [Go to Dashboard](01_Dashboard.py)
- [Manage Customers](02_Customer_Management.py)
- [Manage Sales & Invoices](03_Sales_&_Invoices.py)
- [Manage Inventory](04_Inventory_Management.py)
- [Track Expenses](05_Expense_Management.py)
- [Track Jobs & Tasks](06_Job_&_Task_Tracker.py)
- [Track Employee Hours](07_Employee_Hours.py)
""")

# Highlight your business use cases
st.header("Why Use This App?")
st.write("""
This app is built for small businesses who need an easy-to-use yet powerful tool for managing daily operations. 
By integrating key business processes, you'll be able to focus more on growing your business and less on administration.
""")

# Call to Action
st.write("🎯 **Start using this app today and simplify your business operations!**")

# Footer with Contact Info
st.write("---")
st.write("📧 For support or inquiries, reach out to us at [support@yourbusiness.com](mailto:support@yourbusiness.com)")
