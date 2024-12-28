import streamlit as st
import pandas as pd
import os

# Set up the Streamlit app
st.title("Q&A Form")
st.write("Please fill out the form below and submit your responses.")

# Create a form
with st.form("qa_form"):
    # Add form fields
    name = st.text_input("What is your name?")
    email = st.text_input("What is your email?")
    question_1 = st.text_area("What is your favorite programming language?")
    question_2 = st.text_area("What motivates you to learn programming?")
    submit_button = st.form_submit_button("Submit")

# Handle form submission
if submit_button:
    # Collect the responses into a dictionary
    response = {
        "Name": name,
        "Email": email,
        "Favorite Programming Language": question_1,
        "Motivation": question_2,
    }
    
    # Define the CSV file path
    csv_file = "responses.csv"
    
    # Check if the file already exists
    if os.path.exists(csv_file):
        # Append new responses to the existing file
        existing_data = pd.read_csv(csv_file)
        new_data = pd.DataFrame([response])
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_csv(csv_file, index=False)
    else:
        # Create a new CSV file
        pd.DataFrame([response]).to_csv(csv_file, index=False)

    st.success("Your response has been recorded successfully!")
