import streamlit as st
import pandas as pd
from openai import OpenAI

# 1. Setup OpenAI Client using Streamlit Secrets
# Make sure to add OPENAI_API_KEY in your Streamlit Cloud Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page Configuration
st.set_page_config(page_title="FinDiagnostix AI", page_icon="📈", layout="centered")

# App Header
st.title("🧠 FinDiagnostix AI")
st.subheader("Next-Gen Financial Diagnostic Tool")
st.write("Upload your financial data and let AI handle the analysis.")

# 2. File Uploader Component
uploaded_file = st.file_uploader("Upload Trial Balance or Bank Statement (CSV/XLSX)", type=['csv', 'xlsx'])

if uploaded_file:
    # Read Data
    if uploaded_file.name.endswith('csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
        
    st.success("File uploaded successfully!")
    
    # Display Data Preview
    with st.expander("👁️ View Uploaded Data"):
        st.dataframe(df.head(10))

    # Convert data summary to string for AI context
    data_summary = df.describe().to_string()

    # 3. AI Analysis Section
    st.markdown("---")
    st.header("🔍 AI Financial Analysis")
    
    if st.button("🚀 Run Diagnostic"):
        with st.spinner('Analyzing financial patterns...'):
            try:
                # Prompt Engineering: Asking GPT to act as a Senior Auditor
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a Senior Chartered Accountant and Financial Analyst. Analyze the following data and provide: 1. A summary of financial health. 2. Three actionable insights to improve profit. 3. Detection of any anomalies or risks."},
                        {"role": "user", "content": f"Financial Data Summary: {data_summary}"}
                    ]
                )
                
                analysis_report = response.choices[0].message.content
                st.subheader("📝 Professional Analysis Report")
                st.info(analysis_report)
                
            except Exception as e:
                st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("FinDiagnostix v1.0 | Developed by Salem | Powered by OpenAI")
