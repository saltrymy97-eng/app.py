import streamlit as st
import pandas as pd
from groq import Groq

# Page Config: Global Standard Financial Identity
st.set_page_config(page_title="FinDiagnostix | Financial Diagnosis Engine", page_icon="🛡️", layout="wide")

# Custom CSS for a sleek, "Bloomberg-style" dark financial interface
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #238636; color: white; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #2ea043; border: 1px solid #fff; }
    h1 { color: #58a6ff; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    h3 { color: #58a6ff; }
    .stDataFrame { border: 1px solid #30363d; border-radius: 10px; }
    div[data-testid="stExpander"] { border: 1px solid #30363d; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# Main Branding
st.title("🛡️ FinDiagnostix: Financial Diagnosis Engine")
st.markdown("<h4 style='text-align: center; color: #8b949e;'>Strategic AI Auditor with High-Precision Data Shield for BTC-SMEs</h4>", unsafe_allow_html=True)
st.markdown("---")

# API Configuration
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Authentication Error: GROQ_API_KEY not found in Secrets.")

# File Upload Section
uploaded_file = st.file_uploader("Upload SME Financial Records (CSV Format)", type=["csv"])

if uploaded_file:
    try:
        # Initial data ingestion
        df = pd.read_csv(uploaded_file)
        st.success("Data Shield Activated: Records successfully ingested for auditing.")
        
        with st.expander("👁️ Data Stream Preview"):
            st.dataframe(df.head(10), use_container_width=True)

        # Trigger Audit
        if st.button("🚀 EXECUTE STRATEGIC DIAGNOSIS"):
            with st.spinner("Analyzing data integrity and running stress test simulations..."):
                try:
                    data_context = df.head(50).to_string()
                    
                    # The Ultimate Realistic CFO Prompt (Shield + Diagnosis + 4 Recommendations)
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are the 'FinDiagnostix High-Precision Engine'. Your purpose is to provide a realistic financial audit for SMEs.
                                
                                1. DATA RELIABILITY SHIELD: Analyze the provided data for consistency. Assign a 'Data Reliability Score (%)' based on how clean the data is.
                                2. EXECUTIVE DIAGNOSIS: 
                                   - Analyze the 'Paper Profit Trap' (Accounting records vs Liquid reality).
                                   - Perform a '30% BTC Drop Stress Test' and calculate the new survival runway.
                                3. TOP 4 STRATEGIC RECOMMENDATIONS:
                                   - Recommendation 1 (Liquidity): Immediate cash-flow fix (e.g., L402 Loan).
                                   - Recommendation 2 (Risk Management): Technical BTC protection (e.g., Hedging).
                                   - Recommendation 3 (Operations): Cost-cutting or burn-rate optimization.
                                   - Recommendation 4 (Strategic Management): Long-term model shift (e.g., pricing or payment terms).
                                
                                FORMATTING:
                                - Use Markdown headers (###).
                                - Use BOLD English for all numbers and key insights.
                                - Be professional, blunt, and direct."""
                            },
                            {
                                "role": "user",
                                "content": f"Audit this financial dataset and provide the High-Precision Shield report: {data_context}"
                            }
                        ],
                        temperature=0.1,
                    )
                    
                    # Audit Results Output
                    st.markdown("---")
                    st.header("📋 Executive Audit Report")
                    
                    audit_response = completion.choices[0].message.content
                    st.markdown(audit_response)
                    
                    # Governance & BTC Protocol
                    st.divider()
                    st.warning("🛡️ **SECURITY PROTOCOL:** Any execution of the recommendations above requires Cryptographic Multi-Sig approval via the Lightning Network.")
                    
                except Exception as e:
                    st.error(f"Engine Audit Error: {str(e)}")
                    
    except Exception as e:
        st.error(f"Data Processing Error: {str(e)}")

# Professional Footer
st.markdown("---")
st.caption("FinDiagnostix AI | High-Precision Financial Diagnosis Engine | Developed by Salim Altrymy")
            
