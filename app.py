import streamlit as st
import pandas as pd
from groq import Groq

# Page Config: Professional Financial Identity
st.set_page_config(page_title="FinDiagnostix | Financial Diagnosis Engine", page_icon="📈", layout="wide")

# Custom CSS for a sleek, high-end financial dashboard look
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #238636; color: white; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #2ea043; border: 1px solid #fff; }
    h1 { color: #58a6ff; text-align: center; font-family: 'Helvetica Neue', sans-serif; }
    h3 { color: #58a6ff; }
    .stDataFrame { border: 1px solid #30363d; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Main Title
st.title("📈 FinDiagnostix: Financial Diagnosis Engine")
st.markdown("<h4 style='text-align: center; color: #8b949e;'>Strategic AI Auditor for BTC-Native SMEs</h4>", unsafe_allow_html=True)
st.markdown("---")

# API Configuration
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Error: GROQ_API_KEY not found in Secrets.")

# File Upload Section
uploaded_file = st.file_uploader("Upload SME Financial Records (CSV)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Financial data ingested successfully. Data Shield Activated.")
        
        with st.expander("👁️ Review Input Data Stream"):
            st.dataframe(df.head(10), use_container_width=True)

        # Execution Button
        if st.button("🚀 RUN STRATEGIC AUDIT"):
            with st.spinner("Activating Data Shield & Running Diagnosis..."):
                try:
                    data_context = df.head(50).to_string()
                    
                    # The Ultimate Realistic CFO Prompt with Integrated Data Shield
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are the 'FinDiagnostix High-Precision Engine'. Your mission is to audit SME health with brutal realism.

                                1. 🛡️ DATA RELIABILITY SHIELD:
                                   - Scan the data for inconsistencies, missing values, or outliers.
                                   - Assign a 'Data Reliability Score (%)'.
                                   - Provide a 1-sentence assessment of data integrity.

                                2. 🔍 THE DIAGNOSIS: 
                                   - Diagnose the 'Paper Profit Trap' (Accounting Profit vs. Actual Liquid Cash).
                                   - Run a 'Stress Test' (Survival runway in months if BTC price drops 30%).
                                
                                3. 🎯 TOP 4 STRATEGIC RECOMMENDATIONS:
                                   - Recommendation 1 (Liquidity): Immediate cash-flow action (e.g., L402 Lightning Loan).
                                   - Recommendation 2 (Risk): BTC Volatility protection (e.g., Automated Hedging).
                                   - Recommendation 3 (Operations): Direct advice on burn rate or expense reduction.
                                   - Recommendation 4 (Strategic Management): Long-term business model shift or diversification.
                                
                                RULES:
                                - Use BOLD English for all insights and numbers.
                                - Use Markdown headers (###).
                                - Be professional, blunt, and strictly data-driven.
                                - DO NOT use conversational fillers."""
                            },
                            {
                                "role": "user",
                                "content": f"Apply the High-Precision Shield and Audit this financial dataset: {data_context}"
                            }
                        ],
                        temperature=0.1,
                        max_tokens=1000,
                    )
                    
                    # Display Results
                    st.markdown("---")
                    st.header("📋 Executive Audit Summary")
                    
                    output = completion.choices[0].message.content
                    st.markdown(output)
                    
                    # Governance & Security Protocol
                    st.divider()
                    st.warning("🛡️ **GOVERNANCE PROTOCOL:** Execution of these recommendations requires Cryptographic Multi-Sig approval via the Lightning Network.")
                    
                except Exception as e:
                    st.error(f"Audit Failure: {str(e)}")
                    
    except Exception as e:
        st.error(f"Data Processing Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("FinDiagnostix AI | Financial Diagnosis Engine | Powered by Groq & Llama 3.3 | Developed by Salim Altrymy")
                    
