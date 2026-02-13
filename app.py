import streamlit as st
import pandas as pd
from groq import Groq

# Page Branding & Performance
st.set_page_config(page_title="FinDiagnostix | AI Strategic Auditor", page_icon="🛡️", layout="wide")

# Professional Clean Dark Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #238636; color: white; font-weight: bold; border: none; }
    h1 { color: #58a6ff; font-family: 'Inter', sans-serif; font-weight: 800; }
    .report-box { padding: 20px; border: 1px solid #30363d; border-radius: 10px; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# Main Interface
st.title("🛡️ FinDiagnostix: Financial Diagnosis Engine")
st.markdown("<h4 style='text-align: center; color: #8b949e;'>High-Precision AI Audit & Strategic BTCFi Shield</h4>", unsafe_allow_html=True)
st.markdown("---")

# API Setup
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Authentication Error: Please check your GROQ_API_KEY in Secrets.")

# Data Upload
uploaded_file = st.file_uploader("Upload SME Financial Ledger (CSV Format)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Data Shield Active: Records Ingested Successfully.")
        
        with st.expander("👁️ Raw Data Stream Preview"):
            st.dataframe(df.head(10), use_container_width=True)

        if st.button("🚀 EXECUTE STRATEGIC AUDIT"):
            with st.spinner("Processing Financial Forensics..."):
                try:
                    # Conversion of data to string for the AI context
                    data_context = df.head(50).to_string()
                    
                    # The Prompt: Focused on Realism, Precision, and 4 Recommendations
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are the 'FinDiagnostix CFO Engine'. Your output must be in professional English, blunt, and data-driven.
                                
                                STRICT OUTPUT STRUCTURE:
                                1. 🛡️ DATA RELIABILITY SHIELD: Provide a Confidence Score (%) and 1 sentence on data integrity.
                                
                                2. 🔍 EXECUTIVE DIAGNOSIS:
                                   - THE GAP: Calculate Total Revenue vs Total Expenses. State the Net Liquidity Gap in BOLD.
                                   - STRESS TEST: Simulate a 30% BTC drop. State the 'New Runway' in months.
                                
                                3. 🎯 TOP 4 STRATEGIC RECOMMENDATIONS:
                                   - RECOMMENDATION 1 (Liquidity): Specific L402 Loan amount based on the gap.
                                   - RECOMMENDATION 2 (Risk): Concrete BTC Hedging strategy.
                                   - RECOMMENDATION 3 (Operations): Target % for cost-reduction.
                                   - RECOMMENDATION 4 (Strategy): Long-term business model pivot.
                                
                                NO CONVERSATIONAL FILLERS. NO BROKEN TEXT. JUST THE FACTS."""
                            },
                            {
                                "role": "user",
                                "content": f"Audit this financial dataset: {data_context}"
                            }
                        ],
                        temperature=0.1, # Keep it precise and non-creative
                    )
                    
                    # Display the Report
                    st.markdown("---")
                    st.subheader("📋 Executive Audit Report")
                    st.markdown(f'<div class="report-box">{completion.choices[0].message.content}</div>', unsafe_allow_html=True)
                    
                    st.divider()
                    st.warning("🛡️ **GOVERNANCE PROTOCOL:** All recommended actions require Cryptographic Multi-Sig approval via the Lightning Network.")
                    
                except Exception as e:
                    st.error(f"Audit Failure: {str(e)}")
                    
    except Exception as e:
        st.error(f"File Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("FinDiagnostix AI v2.1 | Strategic Financial Auditor | Developed by Salim Altrymy")
