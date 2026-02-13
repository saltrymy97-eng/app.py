import streamlit as st
import pandas as pd
import google.generativeai as genai

st.set_page_config(page_title="FinDiagnostix AI", page_icon="📈", layout="wide")

st.title("📊 FinDiagnostix AI")
st.subheader("Next-Gen Financial Diagnostic Tool")

# 1. Configuration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Missing API Key in Secrets!")

uploaded_file = st.file_uploader("Upload Financial CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data Loaded Successfully!")
    
    with st.expander("Preview Data"):
        st.dataframe(df.head(10))

    if st.button("🚀 Run AI Analysis"):
        with st.spinner("AI is analyzing your data..."):
            try:
                # محاولة استخدام النموذج الأحدث
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                data_summary = df.head(30).to_string()
                prompt = f"Analyze these finances and give a professional report in English (Summary, Risks, Recommendations):\n\n{data_summary}"
                
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.header("🔍 AI Financial Report")
                st.markdown(response.text)
                
            except Exception as e:
                # محاولة بديلة في حال فشل النموذج الأول (Plan B)
                try:
                    model_backup = genai.GenerativeModel('gemini-pro')
                    response = model_backup.generate_content(prompt)
                    st.markdown("---")
                    st.header("🔍 AI Financial Report (Backup Model)")
                    st.markdown(response.text)
                except Exception as e2:
                    st.error(f"Analysis failed. Please check your API quota or region. Error: {str(e2)}")

st.markdown("---")
st.caption("Developed by Salem | Powered by Google Gemini AI")
