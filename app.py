import streamlit as st
import pandas as pd
from groq import Groq

# Page Config
st.set_page_config(page_title="FinDiagnostix AI | Reality Check", page_icon="🏦", layout="wide")

# Header
st.title("🏦 FinDiagnostix: Strategic CFO Engine")
st.subheader("High-Precision Business Survival Analysis")
st.markdown("---")

# API Configuration
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Missing GROQ_API_KEY in Secrets!")

# File Upload Section
uploaded_file = st.file_uploader("Upload SME Financial Records (CSV)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Data successfully ingested for deep financial audit.")
        
        with st.expander("👁️ Review Ingested Financial Stream"):
            st.dataframe(df.head(10), use_container_width=True)

        if st.button("🚀 Run Realistic Financial Diagnosis"):
            with st.spinner("Analyzing Market Volatility & Liquidity Gaps..."):
                try:
                    data_context = df.head(50).to_string()
                    
                    # The Realistic CFO Prompt with 4 Strategic Recommendations
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are a Realistic Senior CFO & Strategic Consultant. 
                                Analyze the 'Paper Profit Trap' and 'What-if' (30% BTC drop).
                                Provide EXACTLY 4 STRATEGIC RECOMMENDATIONS:
                                1. Liquidity (e.g., L402 Loan).
                                2. Risk (e.g., BTC Hedging).
                                3. Operations (e.g., Expense control).
                                4. Strategy (Long-term business model shift).
                                
                                FORMAT: Use Bold Headers (###). Be Professional and Blunt."""
                            },
                            {
                                "role": "user",
                                "content": f"Audit this data and provide 4 recommendations: {data_context}"
                            }
                        ],
                        temperature=0.1,
                        max_tokens=800,
                    )
                    
                    # UI Output
                    st.markdown("---")
                    st.header("🎯 CFO Executive Summary")
                    st.markdown(completion.choices[0].message.content)
                    st.divider()
                    st.warning("🛡️ **Governance Protocol:** Human approval required for execution.")
                    
                except Exception as e:
                    st.error(f"Audit Error: {str(e)}")
                    
    except Exception as e:
        st.error(f"File Error: {str(e)}")

# Footer
st.caption("FinDiagnostix AI | Developed by Salim Altrymy")
                  
