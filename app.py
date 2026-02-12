import streamlit as st
import pandas as pd
import google.generativeai as genai

# Page Settings
st.set_page_config(page_title="FinDiagnostix AI", page_icon="📈", layout="wide")

# Header
st.title("📊 FinDiagnostix AI")
st.subheader("Next-Gen Financial Diagnostic Tool")
st.markdown("---")

# API Configuration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Using the most compatible model name
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Missing API Key! Please add GEMINI_API_KEY to Streamlit Secrets.")

# File Upload Section
uploaded_file = st.file_uploader("Upload your financial dataset (CSV format)", type=["csv"])

if uploaded_file:
    # Load and preview data
    df = pd.read_csv(uploaded_file)
    st.success("Data uploaded successfully!")
    
    with st.expander("👁️ Preview Raw Data"):
        st.dataframe(df.head(10), use_container_width=True)

    # Analysis Button
    if st.button("🚀 Run AI Diagnostic"):
        with st.spinner("Gemini AI is processing your financial data..."):
            try:
                # Prepare data for the AI
                data_summary = df.head(50).to_string()
                
                prompt = f"""
                Analyze the following financial data and provide a professional report in English.
                Include these sections:
                1. Executive Summary: A high-level overview of the data.
                2. Key Performance Indicators (KPIs): Observations on the numbers.
                3. Risk Assessment: Identify any potential financial red flags.
                4. Strategic Recommendations: Practical steps for improvement.
                
                Financial Data:
                {data_summary}
                """
                
                response = model.generate_content(prompt)
                
                # Output the results
                st.markdown("---")
                st.header("🔍 AI Financial Report")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")

# Footer
st.markdown("---")
st.caption("Developed by Salem | Powered by Google Gemini AI")
                
