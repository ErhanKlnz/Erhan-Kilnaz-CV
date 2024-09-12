import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Personal Webpage", page_icon=":🔖:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_thermostat_sim = Image.open("images/yt_thermostat_sim.png")
img_cloud_rile = Image.open("images/yt_cloud_rile.png")
img_air_conditioning = Image.open("images/yt_air_conditioning_maintenance.jpg")
img_sql_yrt = Image.open("images/yt_sql_yrt.png")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Erhan :wave:")
    st.title("A Computer Engineer From Turkey")
    st.write(
        "Hello, I am Erhan Zeki KILNAZ, a graduate of Computer Engineering from Düzce University. During my internship at Daikin, I worked on energy efficiency and environmental sustainability. Throughout my education, I developed projects on embedded systems, secure file management platforms, database systems, thermostat simulation, and machine learning classification models. With strong problem-solving skills and a passion for technology, I aim to provide innovative solutions to projects."
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

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a Computer Engineering graduate with a strong foundation in software development, data analysis, and embedded systems. I have hands-on experience working on projects ranging from energy efficiency and environmental sustainability during my internship at Daikin, to building secure file management platforms, thermostat simulation systems, and machine learning classification models. 

            I am proficient in C++, C#, Python, and SQL, and have worked with database systems like MSSQL and PostgreSQL. My expertise also extends to machine learning and data analysis, where I have successfully applied these techniques in various projects. I have a keen interest in developing innovative solutions to real-world problems using my technical skills and passion for continuous learning.

            - **Programming Languages**: C++, C#, Python, SQL
            - **Tools & Technologies**: Arduino IDE, MSSQL, PostgreSQL, Machine Learning
            - **Key Projects**: Cloud site development, Dormitory automation system, Thermostat simulation platform

            """
        )
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 1))
    with image_column:
        st.image(img_cloud_rile)
    with text_column:
        st.subheader("🌩️ Cloud-Rile - Cloud Storage System With Pyhton")
        st.write(
            """
            Cloud-Rile is a cutting-edge cloud storage system designed to allow users to securely upload, store, and manage their files.🔐 User Registration and Login: Users can sign up and log in using their email and password.
            🔗 Login with Google and GitHub: Users can authenticate with their Google and GitHub accounts.
            📤 File Upload: Users can upload and store various types of files with ease.
            👁️ File Viewing: Users can view their uploaded files directly in the browser.
            📥 File Download: Users can download their files to local devices for offline access.
            📁 Folder Management: Users can create and manage folders to organize their files efficiently.
            🗑️ Trash Bin: Deleted files and folders are moved to the trash bin for potential recovery.
            📊 Quota Management: Users have a specific storage quota and can monitor their current usage.
            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 1))
    with image_column:
        st.image(img_thermostat_sim)
    with text_column:
        st.subheader("Thermostat Simulation")
        st.write(
            """
            This project is designed for researchers, engineers and enthusiasts who want to analyze the performances of different control algorithms. The application assists the user in understanding their impact on room temperature control. Performance evaluations reveal under which conditions each algorithm works better. This interactive application allows you to compare the performance of different control algorithms (On-Off, PID, Q-Learning, Decision Trees) to maintain the temperature in the room. The simulation works with outdoor temperature data and tests various algorithms used to regulate the room temperature according to user-specified parameters.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 1))
    with image_column:
        st.image(img_air_conditioning)
    with text_column:
        st.subheader("Air Conditioning Maintenance Tracking System With ESP32")
        st.write(
            """
This project aims to create an air conditioning maintenance tracking system using an ESP32 microcontroller and a GP2Y1010AU0F dust sensor. The system, built on a breadboard, monitors the cleanliness of the air filters in the air conditioner and provides maintenance alerts when necessary. The dust sensor measures air quality to detect filter clogging. The ESP32 analyzes the data from the sensor and sends status notifications to the user, issuing an alert when it's time for maintenance. This ensures that the air conditioning systems operate efficiently and healthily.            """
        )
with st.container():
    image_column, text_column = st.columns((1, 1))
    with image_column:
        st.image(img_sql_yrt)
    with text_column:
        st.subheader("Dormitory automation system")
        st.write(
            """
Realized a dormitory automation project using SQL and C#. In this project, digitalization and database management of processes such as student registration, rooms, payment tracking were provided. While data was stored, queried and reported with SQL, the user interface was created and data transactions were managed with C#. In this way, dormitory operations have become more efficient.            """
        )
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
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