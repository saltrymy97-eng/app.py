import streamlit as st
import pandas as pd
import google.generativeai as genai

st.set_page_config(page_title="FinDiagnostix AI", page_icon="📈", layout="wide")

st.title("📊 FinDiagnostix AI")
st.subheader("Next-Gen Financial Diagnostic Tool")
st.markdown("---")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # This specific naming convention bypasses the 404 v1beta error
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
else:
    st.error("Missing API Key!")

uploaded_file = st.file_uploader("Upload your financial dataset (CSV format)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data uploaded successfully!")
    
    with st.expander("👁️ Preview Raw Data"):
        st.dataframe(df.head(10), use_container_width=True)

    if st.button("🚀 Run AI Diagnostic"):
        with st.spinner("Gemini AI is processing..."):
            try:
                data_summary = df.head(50).to_string()
                prompt = f"Analyze these finances and provide a report in English (Summary, Risks, Tips):\n\n{data_summary}"
                
                response = model.generate_content(prompt)
                st.markdown("---")
                st.header("🔍 AI Financial Report")
                st.markdown(response.text)
                
            except Exception as e:
                # This helps us see exactly what's wrong if it fails again
                st.error(f"Analysis failed: {str(e)}")

st.markdown("---")
st.caption("Developed by Salem | Powered by Google Gemini AI")
                
