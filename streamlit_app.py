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
- [Go to Dashboard](https://fencing-app-023485acfd15.herokuapp.com/Dashboard)
- [Manage Customers](https://fencing-app-023485acfd15.herokuapp.com/Customer_Management)
- [Manage Sales & Invoices](https://fencing-app-023485acfd15.herokuapp.com/Sales_&_Invoices)
- [Manage Inventory](https://fencing-app-023485acfd15.herokuapp.com/Inventory_Management)
- [Track Expenses](https://fencing-app-023485acfd15.herokuapp.com/Expense_Management)
- [Track Jobs & Tasks](https://fencing-app-023485acfd15.herokuapp.com/Job_&_Task_Tracker)
- [Track Employee Hours](https://fencing-app-023485acfd15.herokuapp.com/Employee_Hours)
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
st.write("📧 For support or inquiries, reach out to us at [treyhulse3@gmail.com](mailto:treyhulse3@gmail.com)")
