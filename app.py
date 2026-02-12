import streamlit as st
import pandas as pd
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="FinDiagnostix AI", page_icon="📊")

st.title("📊 FinDiagnostix AI")
st.subheader("Next-Gen Financial Diagnostic Tool")

# Setup Gemini AI
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("API Key not found. Please check your Streamlit Secrets.")

# File Upload
uploaded_file = st.file_uploader("Upload your Financial Data (CSV or XLSX)", type=["csv", "xlsx"])

if uploaded_file:
    # Read the data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.success("File uploaded successfully!")
    st.dataframe(df.head(10)) # Show first 10 rows

    if st.button("🚀 Run AI Analysis"):
        with st.spinner("Gemini AI is analyzing your finances..."):
            try:
                # Convert data to string for AI
                data_summary = df.to_string()
                prompt = f"Act as a professional financial analyst. Analyze these financial figures and provide a clear report in English with: 1. Key Highlights, 2. Potential Risks, and 3. Recommendations for improvement:\n\n{data_summary}"
                
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.markdown("### 🔍 AI Financial Report")
                st.write(response.text)
            except Exception as e:
                st.error(f"Analysis failed: {e}")

st.markdown("---")
st.caption("Developed by Salem | Powered by Google Gemini AI (Free Tier)")
