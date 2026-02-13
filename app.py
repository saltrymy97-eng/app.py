import streamlit as st
import pandas as pd
from groq import Groq

# Page Config: Professional Financial Identity
st.set_page_config(page_title="FinDiagnostix | AI Engine", page_icon="🛡️", layout="wide")

# Professional Dark Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #238636; color: white; font-weight: bold; border: none; }
    h1 { color: #58a6ff; text-align: center; }
    .report-box { padding: 20px; border: 1px solid #30363d; border-radius: 10px; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ FinDiagnostix: Financial Diagnosis Engine")
st.markdown("<h4 style='text-align: center;'>Strategic Audit Engine for BTC-Native SMEs</h4>", unsafe_allow_html=True)
st.markdown("---")

if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Missing API Key in Secrets.")

uploaded_file = st.file_uploader("Upload SME Ledger (CSV)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Data Shield Activated. Records Ingested.")
        
        with st.expander("👁️ View Input Data"):
            st.dataframe(df.head(10), use_container_width=True)

        if st.button("🚀 EXECUTE STRATEGIC AUDIT"):
            with st.spinner("Processing Financial Forensics..."):
                try:
                    data_context = df.head(50).to_string()
                    
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are the 'FinDiagnostix CFO Engine'. 
                                YOUR OUTPUT MUST BE IN CLEAN MARKDOWN TABLES.
                                
                                1. 🛡️ DATA RELIABILITY SHIELD:
                                   - State Confidence Score (%).
                                   - Bullet point on data integrity.

                                2. 🔍 EXECUTIVE DIAGNOSIS:
                                   - Table 1: Monthly Profit (Month | Revenue | Expenses | Net Profit).
                                   - Table 2: 30% BTC Stress Test (Month | New Revenue | New Profit).
                                   - Clearly state 'Survival Runway' in bold months.

                                3. 🎯 TOP 4 STRATEGIC RECOMMENDATIONS:
                                   - 1. Liquidity, 2. Risk, 3. Operations, 4. Strategic Management.

                                RULES:
                                - USE MARKDOWN TABLES. 
                                - NO broken symbols or weird text fragments.
                                - Clean professional English only."""
                            },
                            {
                                "role": "user",
                                "content": f"Audit this financial dataset and use tables: {data_context}"
                            }
                        ],
                        temperature=0.1,
                    )
                    
                    st.markdown("---")
                    st.subheader("📋 Executive Audit Report")
                    st.markdown(completion.choices[0].message.content)
                    st.divider()
                    st.warning("🛡️ **GOVERNANCE:** Multi-Sig approval required for execution.")
                    
                except Exception as e:
                    st.error(f"Audit Error: {str(e)}")
    except Exception as e:
        st.error(f"File Error: {str(e)}")

st.caption("FinDiagnostix AI | Developed by Salim Altrymy")
                         
