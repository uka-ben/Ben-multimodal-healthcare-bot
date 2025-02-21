import streamlit as st
import os
import openai
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Multimodal Health Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)
  
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(1875deg,blue,pink,rgb(211, 163, 86), #f5f7fa, green);
    color: #333;
}
[data-testid="stSidebar"] {
    background: linear-gradient(skyblue, blue) !important;
    color: white;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: white;
}
footer {
    visibility: hidden;
}
header {
    visibility: hidden;
}
body {
    font-family: "Source Sans Pro", sans-serif;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    border-radius: 8px;
    padding: 10px 24px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #45a049;
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: #2c3e50;
}
.stMarkdown p {
    color: #333;
}
.stDataFrame {
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.stProgress > div > div > div {
    background-color: #4CAF50;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Set OpenAI API key
OPEN_API_KEY= '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'

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key= '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'
# Function to generate responses using GPT-4o
def generate_response(query):
    response = openai.Completion.create(
        model="gpt-4o",
        prompt=query,
        max_tokens=150
    )
    return response.choices[0].text.strip()



# Function for Symptom Checker with voice and video inputs
def symptom_checker():
    st.markdown('<div class="background-symptom-checker">', unsafe_allow_html=True)
    st.subheader("Symptom Checker")
    st.markdown("Please provide details about your symptoms:")

    # Text input
    symptom_input = st.text_area("Symptoms (Text)", "")

    # Voice input
    st.write("Symptoms (Voice):")
    voice_symptom = st.file_uploader("Upload voice recording (WAV format)", type=["wav"])

    # Video input
    st.write("Symptoms (Video):")
    video_symptom = st.file_uploader("Upload video recording (MP4 format)", type=["mp4"])

    if st.button("Check Symptoms"):
        query = "Symptom checker:"
        if symptom_input:
            query += f" Text: {symptom_input}"
        if voice_symptom:
            query += f" Voice: {voice_symptom.name}"
        if video_symptom:
            query += f" Video: {video_symptom.name}"

        if query != "Symptom checker:":
            response = generate_response(query)
            st.success(response)
        else:
            st.warning("Please provide symptoms.")
    st.markdown('</div>', unsafe_allow_html=True)

# Function for Medical Image Analysis
def image_analysis():
    st.markdown('<div class="background-medical-image">', unsafe_allow_html=True)
    st.subheader("Medical Image Analysis")
    uploaded_image = st.file_uploader("Upload Medical Image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    if st.button("Analyze Image"):
        if uploaded_image:
            # Process the uploaded image (You can add AI-powered analysis here)
            st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
        else:
            st.warning("Please upload a medical image.")
    st.markdown('</div>', unsafe_allow_html=True)

# Function for Consultation Summaries
def consultation_summaries():
    st.markdown('<div class="background-consultation">', unsafe_allow_html=True)
    st.subheader("Consultation Summaries")
    consultation_input = st.text_area("Enter consultation details:", "")
    if st.button("Generate Summary"):
        if consultation_input:
            query = f"Consultation summary: {consultation_input}"
            response = generate_response(query)
            st.success(response)
        else:
            st.warning("Please enter consultation details.")
    st.markdown('</div>', unsafe_allow_html=True)

# Function for Patient Support
def patient_support():
    st.markdown('<div class="background-patient-support">', unsafe_allow_html=True)
    st.subheader("Patient Support")
    question_input = st.text_area("Ask a question:", "")
    if st.button("Get Support"):
        if question_input:
            query = f"Patient support: {question_input}"
            response = generate_response(query)
            st.success(response)
        else:
            st.warning("Please ask a question.")
    st.markdown('</div>', unsafe_allow_html=True)

# Main function to run the application
def main():
    st.markdown('<div class="background">', unsafe_allow_html=True)
    image1 = Image.open("mypiclogo.png")
    st.image(image1)
    st.write("benjaminukaimo@gmail.com")
    st.write("+2347067193071")
    st.write("My name is Uka Benjamin. I'm a data scientist with good experiences")
    st.title("Ben's Healthcare Chatbot")
    st.write("This is a multimodal assistant")
    selected_option = st.radio("Select an Option", ["Symptom Checker", "Medical Image Analysis", "Consultation Summaries", "Patient Support"], horizontal=True)

    if selected_option == "Symptom Checker":
        symptom_checker()
    elif selected_option == "Medical Image Analysis":
        image_analysis()
    elif selected_option == "Consultation Summaries":
        consultation_summaries()
    elif selected_option == "Patient Support":
        patient_support()
    st.markdown('</div>', unsafe_allow_html=True)

# Execute the main function
if __name__ == "__main__":
    main()
