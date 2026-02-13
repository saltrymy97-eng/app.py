import streamlit as st
import pandas as pd
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="FinDiagnostix AI", page_icon="📊", layout="wide")

# Header
st.title("📊 FinDiagnostix AI")
st.subheader("Next-Generation Financial Diagnostic Tool")
st.markdown("---")

# API Configuration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key not found! Please add GEMINI_API_KEY to Streamlit Secrets.")

# File Upload
uploaded_file = st.file_uploader("Upload your financial data (CSV format)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        
        with st.expander("👁️ Preview Raw Data"):
            st.dataframe(df.head(10), use_container_width=True)

        # Analysis Button
        if st.button("🚀 Run AI Diagnostic"):
            with st.spinner("Gemini AI is analyzing your data..."):
                try:
                    # Preparing data summary
                    data_summary = df.head(50).to_string()
                    
                    # Defining the prompt
                    prompt = f"""
                    Act as a professional financial analyst. 
                    Analyze the following data and provide a report in English:
                    1. Executive Summary
                    2. Key Findings & Metrics
                    3. Potential Risks
                    4. Strategic Recommendations
                    
                    Data:
                    {data_summary}
                    """
                    
                    # 💡 Using the model name as suggested by the system (with models/ prefix)
                    # We will try the most stable version 'gemini-1.5-flash'
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    
                    response = model.generate_content(prompt)
                    
                    st.markdown("---")
                    st.header("🔍 AI Financial Analysis Report")
                    st.markdown(response.text)
                    
                except Exception as e:
                    # Fallback to 'gemini-pro' if flash is not available
                    try:
                        model_pro = genai.GenerativeModel('models/gemini-pro')
                        response = model_pro.generate_content(prompt)
                        st.markdown("---")
                        st.header("🔍 AI Financial Analysis Report")
                        st.markdown(response.text)
                    except Exception as e2:
                        st.error(f"Analysis Failed: {str(e2)}")
                        st.info("Tip: Ensure your API key is active and your region is supported.")
                        
    except Exception as e:
        st.error(f"Error reading the file: {e}")

# Footer
st.markdown("---")
st.caption("Developed by Salem | Powered by Google Gemini AI")
                        
