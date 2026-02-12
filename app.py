import streamlit as st
import pandas as pd
import google.generativeai as genai

st.set_page_config(page_title="FinDiagnostix AI", page_icon="📈")
st.title("📊 FinDiagnostix AI")

# Configure Gemini
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Changed to the most stable model name
    model = genai.GenerativeModel('gemini-pro') 
else:
    st.error("API Key missing!")

file = st.file_uploader("Upload Financial CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.success("File Loaded!")
    
    if st.button("🚀 Run AI Analysis"):
        with st.spinner("Connecting to Google Gemini..."):
            try:
                data_summary = df.head(30).to_string()
                prompt = f"Analyze these financial figures and provide a summary report in English:\n\n{data_summary}"
                
                # Using the standard content generation
                response = model.generate_content(prompt)
                
                st.markdown("### 🔍 AI Financial Report")
                st.write(response.text)
            except Exception as e:
                st.error(f"Analysis failed: {e}")

st.markdown("---")
st.caption("Developed by Salem | Powered by Google Gemini")
