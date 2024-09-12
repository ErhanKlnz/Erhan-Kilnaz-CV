import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Set page config
st.set_page_config(page_title="Personal Webpage", page_icon="🔖", layout="wide")


# Function to load Lottie animation from URL
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None


# Function to load local CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Please check the file path.")


# Load local CSS
local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")

# Handle image loading
try:
    img_thermostat_sim = Image.open("images/yt_thermostat_sim.png")
    img_cloud_rile = Image.open("images/yt_cloud_rile.png")
    img_air_conditioning = Image.open("images/yt_air_conditioning_maintenance.jpg")
    img_sql_yrt = Image.open("images/yt_sql_yrt.png")
except FileNotFoundError as e:
    st.error(f"Image not found: {e}")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Erhan :wave:")
    st.title("A Computer Engineer From Turkey")
    st.write(
        """
        Hello, I am Erhan Zeki KILNAZ, a graduate of Computer Engineering from Düzce University. 
        During my internship at Daikin, I worked on energy efficiency and environmental sustainability. 
        I developed projects on embedded systems, secure file management platforms, database systems, 
        thermostat simulation, and machine learning classification models. With strong problem-solving 
        skills and a passion for technology, I aim to provide innovative solutions to projects.
        """
    )
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

# ---- WHAT I DO SECTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            I am a Computer Engineering graduate with a strong foundation in software development, 
            data analysis, and embedded systems. I have hands-on experience working on projects 
            ranging from energy efficiency and environmental sustainability during my internship at Daikin, 
            to building secure file management platforms, thermostat simulation systems, and machine learning 
            classification models. 

            - **Programming Languages**: C, C++, C#, Python, SQL, Html, Css
            - **Tools & Technologies**: Arduino IDE, MSSQL, PostgreSQL, Machine Learning
            - **Key Projects**: Cloud site development, Dormitory automation system, Thermostat simulation platform
            """
        )
        
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.write("Lottie animation could not be loaded.")

# ---- PROJECTS SECTION ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    
    image_column, text_column = st.columns((1, 1))
    with image_column:
        if 'img_cloud_rile' in locals():
            st.image(img_cloud_rile)
    with text_column:
        st.subheader("🌩️ Cloud-Rile - Cloud Storage System With Python")
        st.write(
            """
            Cloud-Rile is a cloud storage system that allows users to securely upload, store, 
            and manage files. Features include:
            - 🔐 User Registration and Login
            - 🔗 Login with Google and GitHub
            - 📤 File Upload & 📥 Download
            - 👁️ File Viewing & 📁 Folder Management
            - 🗑️ Trash Bin and 📊 Quota Management
            """
        )
        
    image_column, text_column = st.columns((1, 1))
    with image_column:
        if 'img_thermostat_sim' in locals():
            st.image(img_thermostat_sim)
    with text_column:
        st.subheader("Thermostat Simulation")
        st.write(
            """
            This project compares the performance of different control algorithms 
            (On-Off, PID, Q-Learning, Decision Trees) to maintain room temperature. 
            The simulation works with outdoor temperature data to test these algorithms.
            """
        )
        
    image_column, text_column = st.columns((1, 1))
    with image_column:
        if 'img_air_conditioning' in locals():
            st.image(img_air_conditioning)
    with text_column:
        st.subheader("Air Conditioning Maintenance Tracking System With ESP32")
        st.write(
            """
            The project uses an ESP32 microcontroller and dust sensor to monitor air 
            conditioner filters and provide maintenance alerts when needed, 
            ensuring efficient and healthy operation.
            """
        )
        
    image_column, text_column = st.columns((1, 1))
    with image_column:
        if 'img_sql_yrt' in locals():
            st.image(img_sql_yrt)
    with text_column:
        st.subheader("Dormitory Automation System")
        st.write(
            """
            Developed a dormitory automation system using SQL and C#. The project 
            streamlines student registration, room allocation, and payment tracking.
            """
        )

# ---- CONTACT SECTION ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/erhanzekikilnaz@hotmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
