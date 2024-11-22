import streamlit as st
from resume_generator import generate_resume
from ai_helper import suggest_improvements

st.title("AI Resume Builder")

st.header("Personal Information")
name = st.text_input("Full Name")
contact = st.text_area("Contact Information (Email, Phone, LinkedIn)")

st.header("Education")
education = st.text_area("List your educational qualifications")
if st.button("Improve Education Section"):
    education = suggest_improvements("Education", education)
    st.text_area("Improved Education Section", value=education, height=150)

st.header("Work Experience")
experience = st.text_area("Describe your work experience")
if st.button("Improve Work Experience"):
    experience = suggest_improvements("Work Experience", experience)
    st.text_area("Improved Experience Section", value=experience, height=150)

st.header("Skills")
skills = st.text_area("List your skills")
if st.button("Improve Skills Section"):
    skills = suggest_improvements("Skills", skills)
    st.text_area("Improved Skills Section", value=skills, height=150)

st.header("Additional Information")
additional = st.text_area("Include certifications, hobbies, etc. (optional)")

if st.button("Generate Resume"):
    if name and contact and education and skills:
        file_path = generate_resume(name, contact, education, experience, skills, additional)
        st.success("Resume generated successfully!")
        with open(file_path, "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="resume.pdf",
                mime="application/pdf"
            )
    else:
        st.error("Please fill out all required fields.")
