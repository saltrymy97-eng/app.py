import streamlit as st
import pandas as pd
from groq import Groq

# Page Config
st.set_page_config(page_title="FinDiagnostix AI", page_icon="📈", layout="wide")

st.title("📊 FinDiagnostix AI (Powered by Groq)")
st.subheader("High-Speed Financial Diagnosis")

# API Configuration
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Missing GROQ_API_KEY in Secrets!")

uploaded_file = st.file_uploader("Upload Financial CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File Uploaded Successfully!")
    
    with st.expander("👁️ View Data Preview"):
        st.dataframe(df.head(10), use_container_width=True)

    if st.button("🚀 Run Instant AI Analysis"):
        with st.spinner("Groq AI is crunching the numbers..."):
            try:
                # Prepare data summary
                data_summary = df.head(50).to_string()
                
                # Groq API Call
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a professional financial analyst. Provide reports in English with Executive Summary, Risks, and Recommendations."
                        },
                        {
                            "role": "user",
                            "content": f"Analyze this financial data:\n\n{data_summary}",
                        }
                    ],
                    model="llama3-8b-8192", # One of the fastest models
                )
                
                st.markdown("---")
                st.header("🔍 AI Financial Report")
                st.write(chat_completion.choices[0].message.content)
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")

st.markdown("---")
st.caption("Developed by Salem | Powered by Groq Llama 3")
