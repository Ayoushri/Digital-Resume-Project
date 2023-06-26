from pathlib import Path
import pandas as pd
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assests" / "Ayoushri Basu Resume.pdf"
profile_pic = current_dir / "assests" / "Profile Picture.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "DIGITAL CV | AYOUSHRI BASU"
PAGE_ICON = "👩‍💻"
NAME = "Ayoushri Basu"
DESCRIPTION = """
An undergraduate computer science engineering student of UEM Kolkata
"""
EMAIL = "📧 basuayou06@gmail.com"
CONTACT = "📞 8697002168"
ADDRESS = "🏠 9/7/1, Kasundia 2nd bye lane, Howrah - 711104"
ACADEMIC_QUALIFICATION = {
    "Degree":['Graduation','Higher Secondary','Secondary'],
    "Discipline":['B.Tech in CSE','Science','General'],
    "Institute":['UEM Kolkata','B.E.College Model School',"Bidya Bharati Girls' High School"],
    "Year of Passing":[2024,2020,2018],
    "Aggregate Percentage or CGPA":[9.70,"92%","90%"]
}
PROJECTS = {
    "Organization Name":["UEM Kolkata"],
    "Project Title":["Jarvis"],
    "Duration":["6 weeks"]
}




st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

## st.title("Hello there!")

# ---LOAD CSS, PDF & PROFILE PIC ---
with open(css_file)  as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# -- HERO SECION --
col1, col2 = st.columns(2, gap="large")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "📁 Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )
    st.write(EMAIL)
    st.write(CONTACT)
    st.write(ADDRESS)

    #-- ACADEMIC QUALIFICATIONS --#
st.write("#")
st.subheader("Academic Qualification:")
st.dataframe(pd.DataFrame.from_dict(ACADEMIC_QUALIFICATION))
st.subheader("Projects:")
st.dataframe(pd.DataFrame.from_dict(PROJECTS))
st.subheader("Certifications:")
st.write(
        """
    - • HackerRank, Java(Basic)
    - • HackerRank ,Python(Basic)
    - • Coursera, Python Data Structures
    - • Great Learning, Java Programming
    - • Great Learning, Excel for Beginners
    """
    )
st.subheader("Achievements:")
st.write(
        """
    - ✅ Got Certificate of Participation in UEM-IEM CYCLOTHON’22
    - ✅ Got Certificate of Participation in Code Golf during URECKON 2022
    - ✅ Got the Certificate of Merit for being among the top 5% students in the Department of CSE for the
    academic year 2020 – 2021, University of Engineering and Management Kolkata
    """
    )
st.subheader("Subjects Of Interest:")
st.write(
    """
    - ➤ Data Base Management Systems
    - ➤ Data Structure And Algorithm
    - ➤ Operating Systems
    - ➤ Digital Logic
    """
    )
st.subheader("Programming Language Proficiency:")
st.write("""
    - • C
    - • Python
    - • Java 
    """)
st.subheader("Hobbies:")
st.write(""" 
    - ♔Playing Chess
    - 🚴Cycling
    """)

