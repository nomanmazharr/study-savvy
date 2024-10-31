import streamlit as st
from gpt_model import generate_study_plan
from upload import upload_and_read_file

# Streamlit user interface
st.title("Personalized Study Assistant Chatbot")
st.write("I’m here to help you organize your study plan with tailored resources and tips. Let's get started!")

# User input for study details
study_topic = st.text_input("What is your study topic or exam?")
prep_days = st.number_input("How many days do you have to prepare?", min_value=1)
hours_per_day = st.number_input("How many hours can you dedicate per day?", min_value=1)

# Option to upload a document for specific content
st.write("Alternatively, you can upload a document with your study topics or descriptions.")
file_content = upload_and_read_file()  # Retrieve content from the uploaded file

if 'study_plan' not in st.session_state:
    st.session_state.study_plan = None

# Button to generate study plan
if st.button("Generate Study Plan"):
    # Use file content if available; otherwise, use manually entered topic
    if file_content:
        st.session_state.study_plan = generate_study_plan(file_content, prep_days, hours_per_day)
    else:
        st.session_state.study_plan = generate_study_plan(study_topic, prep_days, hours_per_day)

    # Display the generated study plan
    st.write("### Your Study Plan")
    st.write(st.session_state.study_plan)

if st.session_state.study_plan and st.button("Save Study Plan to Text File"):
    with open("study_plan.txt", "w") as file:
        file.write(st.session_state.study_plan)
    st.success("Study plan saved to study_plan.txt")