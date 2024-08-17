"""
This function creates a PDF resume using the FPDF library.

Parameters:
- name (str): The name of the person.
- contact_info (str): The contact information of the person.
- education (str): The education details of the person.
- experience (str): The work experience details of the person.
- skills (str): The skills of the person.
- projects (str): The projects of the person.

Returns:
- pdf (FPDF object): The generated PDF resume.
"""
import streamlit as st
from fpdf import FPDF

def create_pdf(name, contact_info, email_address, linkedIn_profile, language_proficiencies, education, experience, skills, projects, achievement):
    pdf = FPDF()
    pdf.add_page()
    
    # Adding title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=name, ln=True, align='C')
    
    # Contact Info
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=contact_info, ln=True, align='C')

    # Email Address
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=email_address, ln=True, align='C')

    # LinkedIn Profile
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=linkedIn_profile, ln=True, align='C')

    # Language proficiencies
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Language Proficiency", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, language_proficiencies)

    # Education Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, education)
    
    # Experience Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, experience)
    
    # Skills Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, skills)
    
    # Projects Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Projects", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, projects)

    # Achievement Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Achievements", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, achievement)

    return pdf

# Streamlit App
st.title("Resume Builder Application")

# Collecting personal information
name = st.text_input("Name")
contact_info = st.text_input("Contact Information")
email_address = st.text_input("Email Address")
linkedIn_profile = st.text_input("LinkedIn Profile")
st.header("Language Proficiency")
language_proficiencies = st.text_area("Enter known languages and their proficiency")

# Education Section
st.header("Education")
education = st.text_area("Enter your education details (e.g., school, degree, dates)")

# Experience Section
st.header("Work Experience")
experience = st.text_area("Enter your work experience (e.g., company, role, dates, description)")

# Skills Section
st.header("Skills")
skills = st.text_area("Enter your skills (comma-separated)")

# Projects Section
st.header("Projects")
projects = st.text_area("Enter your projects (e.g., title, description)")

# Achievements Section
st.header("Achievements")
achievement = st.text_area("Enter your achievements (e.g., certificates, medals, awards)")

# Button to download resume as PDF
if st.button("Download Resume as PDF"):
    if name and contact_info and email_address and linkedIn_profile and language_proficiencies and education and experience and skills and projects and achievement:
        # Generate the PDF
        pdf = create_pdf(name, contact_info, email_address, linkedIn_profile, language_proficiencies, education, experience, skills, projects, achievement)
        
        # Create a downloadable link
        pdf_output = pdf.output(dest='S').encode('latin1')
        st.download_button("Download Resume", data=pdf_output, file_name="resume.pdf", mime="application/pdf")
    else:
        st.error("Please fill in all the fields.")