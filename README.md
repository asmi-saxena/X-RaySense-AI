# X-RaySense AI

## Overview
X-RaySense AI is an AI-powered medical imaging analysis system designed to assist radiologists and healthcare professionals in diagnosing conditions from X-ray images. The application leverages **Google's Gemini AI model** to generate intelligent insights based on patient details and uploaded X-ray scans.

## Features
- **AI-Powered X-ray Analysis**: Uses the Gemini AI model to interpret and provide insights on X-ray images.
- **User-Friendly Interface**: Developed with **Streamlit** for an intuitive and responsive experience.
- **Secure Patient Data Handling**: Accepts patient age, gender, and medical history for personalized results.
- **Automated Report Generation**: Generates **downloadable PDF reports** containing AI-driven analysis.
- **Cloud-Based & Scalable**: Can be integrated into existing hospital and telemedicine platforms.

## Technologies Used
- **Python**: Core programming language for AI model interaction and backend logic.
- **Streamlit**: Frontend framework for a seamless web-based UI.
- **Google Gemini AI**: Used for medical image interpretation and response generation.
- **Pillow (PIL)**: For handling and processing image files.
- **ReportLab**: For generating PDF reports.

## Installation & Setup
### Prerequisites
Make sure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Virtual environment** (optional but recommended)

### Clone the Repository
```sh
 git clone https://github.com/asmi-saxena/X-RaySense-AI.git
 cd X-RaySense-AI
```

### Install Dependencies
```sh
 pip install -r requirements.txt
```

### Run the Application
```sh
 streamlit run app.py
```

## Usage
1. **Upload an X-ray Image**: Select an image file (JPG, PNG, JPEG).
2. **Enter Patient Details**: Provide patient age, gender, and medical history.
3. **Analyze the X-ray**: Click the 'Analyze X-ray' button to get AI-generated insights.
4. **Download Report**: Generate and download a PDF containing the analysis results.

## Sample Output
Once an X-ray is analyzed, the AI provides:
- **Medical condition predictions** (e.g., Pneumonia detection, bone fractures, etc.).
- **Insights based on patient history**.
- **Recommendations for further medical evaluation**.



✨ **X-RaySense AI - Enhancing Medical Diagnostics with AI** ✨

