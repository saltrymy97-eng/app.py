import streamlit as st
import pandas as pd
from groq import Groq

# Page Layout
st.set_page_config(page_title="FinDiagnostix AI", page_icon="📈", layout="wide")

# Header
st.title("📊 FinDiagnostix AI")
st.subheader("High-Speed Financial Diagnosis Engine")
st.markdown("---")

# Initialize Groq Client
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("API Key missing! Please add GROQ_API_KEY to Streamlit Secrets.")

# File Upload
uploaded_file = st.file_uploader("Upload Financial CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Data loaded successfully!")
        
        with st.expander("👁️ Data Preview"):
            st.dataframe(df.head(10), use_container_width=True)

        if st.button("🚀 Run AI Analysis"):
            with st.spinner("Groq AI is analyzing your data..."):
                try:
                    # Formatting data for the AI
                    data_summary = df.head(50).to_string()
                    
                    # API Call to Groq (Using the NEW supported Llama model)
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile", # Updated model name
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a senior financial consultant. Provide a professional report in English with: 1. Executive Summary, 2. Key Insights, 3. Potential Risks, 4. Strategic Recommendations."
                            },
                            {
                                "role": "user",
                                "content": f"Analyze this financial data and provide a detailed report:\n\n{data_summary}"
                            }
                        ],
                        temperature=0.5,
                        max_tokens=1024,
                    )
                    
                    st.markdown("---")
                    st.header("🔍 AI Financial Report")
                    st.markdown(completion.choices[0].message.content)
                    
                except Exception as e:
                    st.error(f"Analysis Error: {str(e)}")
    except Exception as e:
        st.error(f"File Error: {str(e)}")

st.markdown("---")
st.caption("Developed by Salem | Powered by Groq Llama 3.3")
                    
