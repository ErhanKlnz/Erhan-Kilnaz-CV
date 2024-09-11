import streamlit as st

# Page configuration
st.set_page_config(page_title="Erhan Zeki KILNAZ - CV", layout="centered", initial_sidebar_state="auto")

# Custom CSS for structured layout, background image, and clean design
def add_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap');

        /* Background image for the page */
        body {
            background-image: url('https://sphero.com/cdn/shop/articles/coding_languages_1024x.png?v=1619126283'); /* Subtle background */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #333333;
            font-family: 'Nunito', sans-serif;
        }

        /* Style for headers */
        h1, h2, h3 {
            color: #2e3b4e;
            font-weight: 700;
        }

        /* Main content container */
        .container {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Button styling */
        .stButton>button {
            background-color: #3498db;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #2980b9;
        }

        /* Image styling */
        .stImage {
            border-radius: 50%;
            margin-bottom: 20px;
        }

        /* Contact button styling */
        .contact-buttons a {
            text-decoration: none;
            color: white;
        }

        .contact-buttons .linkedin {
            background-color: #0077b5;
            padding: 10px 20px;
            border-radius: 5px;
            margin-right: 10px;
            font-weight: bold;
        }

        .contact-buttons .github {
            background-color: #333333;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }

        /* Footer styling */
        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: #888;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

# Profile Image from URL
image_url = 'https://media.licdn.com/dms/image/v2/D4D03AQEnWYJMCjxpAg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1711629083587?e=1731542400&v=beta&t=IJuj0QE9YFo8ObWXaKCINgpl8sFuJzVRVROp2-NKHcw'
st.image(image_url, width=150)

# Main Container for CV content
st.markdown('<div class="container">', unsafe_allow_html=True)

# Title and Personal Information
st.title("Erhan Zeki KILNAZ")
st.subheader("Computer Engineer")
st.write("**Location:** Hendek/SAKARYA")
st.write("**Phone:** +90 536 735 65 65")
st.write("**E-mail:** [erhanzekikilnaz@hotmail.com](mailto:erhanzekikilnaz@hotmail.com)")

# Contact Links (LinkedIn & GitHub)
st.write("**Contact Me:**")
st.markdown(
    """
    <div class="contact-buttons">
        <a href="https://www.linkedin.com/in/erhan-zeki-k%C4%B1lnaz/" target="_blank" class="linkedin">LinkedIn</a>
        <a href="https://github.com/ErhanKlnz" target="_blank" class="github">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Personal Information Section
st.header("Personal Information")
st.write("**Date/Place of Birth:** Sakarya / 2001")
st.write("**Driving License:** B Class")

# About Me Section
st.header("About Me")
st.write("""
Hello, I am Erhan Zeki KILNAZ, a graduate of Computer Engineering from Düzce University. During my internship at Daikin, I worked on energy efficiency and environmental sustainability. Throughout my education, I developed projects on embedded systems, secure file management platforms, database systems, thermostat simulation, and machine learning classification models. With strong problem-solving skills and a passion for technology, I aim to provide innovative solutions to projects.
""")

# Education Section
st.header("Education")
st.write("**2020-2024:** Düzce University / Computer Engineering")

# Work Experience Section
st.header("Work Experience")
st.write("**01.07.2024-13.09.2024:** Daikin R&D / Intern")

# Projects Section
st.header("Projects")
st.write("- [CloudReli](https://github.com/ErhanKlnz/Cloud-Site): Cloud site project")
st.write("- [Yurt Otomasyonu](https://github.com/ErhanKlnz/Yurt-Otomasyonu): Dormitory automation project")
st.write("- [Bookmate](https://github.com/ErhanKlnz/Bookmate): Bookmate project")
st.write("- [Klima Bakım Takip Sistemi](https://github.com/ErhanKlnz/Air-Conditioning-Maintenance-Tracking-System-): Embedded systems project - Air Conditioning Maintenance Tracking System")
st.write("- [Daikin Çevresel Sürdürülebilirlik ve Enerji Verimliliği](#): Evaluation of Heat Pumps, Packaging Materials, and Smart Thermostats")
st.write("- [Termostat Simülasyon Platformu](https://github.com/ErhanKlnz/Thermostat-Simulation-Platform): Thermostat Simulation Platform")
st.write("- [Farklı Sınıflandırma Algoritmalarının Karşılaştırılması](https://github.com/ErhanKlnz/Data-Engineering-Classification): Comparison of Different Classification Algorithms")

# Skills Section
st.header("Skills")
st.write("- C++")
st.write("- C#")
st.write("- Python")
st.write("- SQL")
st.write("- Arduino IDE")
st.write("- MSSQL")
st.write("- PostgreSQL")
st.write("- Machine Learning")
st.write("- Data Analysis and Classification")

# Competencies Section
st.header("Competencies")
st.write("- English: B1 Level")
st.write("- Git")
st.write("- MS Office (Word, Excel, PowerPoint): Intermediate")

# References Section
st.header("References")
st.write("**Kübra Kılnaz:** Daikin Turkey Quality and Sustainability Department Manager")
st.write("**Asena CEYLAN:** R&D Senior Compliance Engineer, Daikin Türkiye Heating and Cooling Systems")

st.markdown('</div>', unsafe_allow_html=True)  # End of main container

# Footer
st.markdown("***")
st.markdown('<div class="footer">This CV was created using **Streamlit**.</div>', unsafe_allow_html=True)
