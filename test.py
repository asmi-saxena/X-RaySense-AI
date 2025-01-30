import google.generativeai as genai
from PIL import Image
import streamlit as st
from fpdf import FPDF

# Configure the API key
genai.configure(api_key='AIzaSyBk5R8rRbz9qgZhquGxaK_BtAkyTCY_Zi0')

def analyze_xray(image, patient_age, patient_gender, patient_history):
    """
    Analyzes an X-ray image using the Gemini AI model.

    Parameters:
        image (PIL.Image.Image): X-ray image object.
        patient_age (str): Patient's age.
        patient_gender (str): Patient's gender.
        patient_history (str): Patient's medical history.

    Returns:
        str: AI-generated response or error message.
    """
    try:
        # Initialize the model
        model = genai.GenerativeModel(model_name='gemini-2.0-flash-exp')

        # Generate the response
        prompt = f"Explain this X-ray image. Patient age: {patient_age}, gender: {patient_gender}. History: {patient_history}."
        response = model.generate_content([prompt, image])
        return response.text  # Return the AI-generated response
    except Exception as e:
        return f"Error: {str(e)}"

def generate_pdf_report(patient_details, analysis_result):
    """
    Generates a PDF report containing patient details and AI analysis results.

    Parameters:
        patient_details (dict): Dictionary containing patient's age, gender, and history.
        analysis_result (str): The result of the AI analysis.

    Returns:
        str: Path to the generated PDF file.
    """
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add title
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="X-Ray Analysis Report", ln=True, align="C")

        # Add patient details
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt=f"Patient Age: {patient_details['age']}", ln=True)
        pdf.cell(0, 10, txt=f"Patient Gender: {patient_details['gender']}", ln=True)
        pdf.cell(0, 10, txt=f"Patient History: {patient_details['history']}", ln=True)

        # Add AI Analysis
        pdf.ln(10)
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(0, 10, txt="AI Analysis:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=analysis_result)

        # Save PDF
        file_path = "XRay_Analysis_Report.pdf"
        pdf.output(file_path)

        return file_path
    except Exception as e:
        return f"Error generating PDF: {str(e)}"

# Initialize session state for analysis result
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# Streamlit Frontend
st.set_page_config(
    page_title="X-RaySense AI",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 X-RaySense AI")
st.markdown("Upload an X-ray image and provide patient details to receive an AI-powered analysis.")

# Layout: Two Columns for Image Upload and Input Fields
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📤 Upload X-ray Image")
    uploaded_file = st.file_uploader("Choose an X-ray image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(Image.open(uploaded_file), caption="Uploaded X-ray", use_container_width=True)

with col2:
    st.subheader("📝 Patient Details")
    patient_age = st.text_input("Patient Age", placeholder="Enter patient's age")
    patient_gender = st.radio("Patient Gender", ["Male", "Female", "Other"], horizontal=True)
    patient_history = st.text_area("Patient History", placeholder="Describe the patient's medical history")

# Analyze Button
if uploaded_file and patient_age and patient_gender and patient_history:
    if st.button("Analyze X-ray"):
        with st.spinner("Analyzing X-ray..."):
            img = Image.open(uploaded_file)
            st.session_state.analysis_result = analyze_xray(img, patient_age, patient_gender, patient_history)
            st.success("Analysis Complete!")

# Display the Analysis Result
if st.session_state.analysis_result:
    st.markdown("### AI Analysis Response:")
    st.write(st.session_state.analysis_result)

    # PDF Generation Section
    if st.button("Generate PDF Report"):
        with st.spinner("Generating PDF..."):
            patient_details = {
                "age": patient_age,
                "gender": patient_gender,
                "history": patient_history
            }
            pdf_path = generate_pdf_report(patient_details, st.session_state.analysis_result)
            if pdf_path.endswith(".pdf"):
                st.success(f"PDF report generated successfully!")
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📄 Download Report",
                        data=pdf_file,
                        file_name="XRay_Analysis_Report.pdf",
                        mime="application/pdf"
                    )
            else:
                st.error("Failed to generate PDF report.")
