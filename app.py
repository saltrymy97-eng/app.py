import streamlit as st
import pandas as pd
from groq import Groq

# 1. BTC-Centric UI Configuration
st.set_page_config(page_title="FinDiagnostix | BTC Strategic Engine", page_icon="₿", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #f7931a; color: white; font-weight: bold; border: none; font-size: 1.2em; }
    .stButton>button:hover { background-color: #e8820e; border: 1px solid #fff; }
    h1 { color: #f7931a; text-align: center; font-family: 'Inter', sans-serif; }
    .report-box { padding: 25px; border: 1px solid #f7931a; border-radius: 12px; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# 2. Bitcoin Branding Header
st.title("₿ FinDiagnostix: BTC Financial Diagnosis Engine")
st.markdown("<h4 style='text-align: center; color: #8b949e;'>AI Auditor for Bitcoin-Native SMEs & Lightning Network Enterprises</h4>", unsafe_allow_html=True)
st.markdown("---")

# 3. API Connection
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Authentication Error: API Key missing.")

# 4. Data Ingestion
uploaded_file = st.file_uploader("Upload Financial Ledger (CSV)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Bitcoin Data Shield Activated: Records Ingested Successfully.")
        
        with st.expander("👁️ Review SME Financial Stream"):
            st.dataframe(df, use_container_width=True)

        if st.button("🚀 EXECUTE BTC STRATEGIC AUDIT"):
            with st.spinner("Simulating BTC Price Volatility & Lightning Liquidity..."):
                try:
                    data_context = df.to_string()
                    
                    # 5. The BTC-Native Prompt
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are the 'FinDiagnostix BTC-CFO Engine'. 
                                You specialize in Bitcoin-Native finance and SME auditing.
                                
                                1. 🛡️ DATA RELIABILITY SHIELD:
                                   - Provide 'Confidence Score (%)'.

                                2. 🔍 BTC STRATEGIC DIAGNOSIS:
                                   - TABLE 1: 'Current Health' (| Month | Revenue | Expenses | Profit |).
                                   - TABLE 2: 'BTC Stress Test' (Simulate a 30% BTC price crash). Show New Revenue in USD and estimated Sats.
                                   - Boldly state the 'Bitcoin Survival Runway' in months.

                                3. 🎯 BTC STRATEGIC RECOMMENDATIONS:
                                   - RECOMMENDATION 1 (Liquidity): Advise on L402 Lightning Loans or BTC-backed credit.
                                   - RECOMMENDATION 2 (Treasury): BTC Hedging or Cold Storage shifts.
                                   - RECOMMENDATION 3 (Ops): Optimize burn rate to accumulate more Sats.
                                   - RECOMMENDATION 4 (Strategy): Shift to Circular BTC Economy (Paying suppliers via Lightning).

                                RULES:
                                - PROFESSIONAL ENGLISH ONLY.
                                - FOCUS ON BITCOIN TERMINOLOGY (Sats, Lightning, L402, Multi-Sig).
                                - USE MARKDOWN TABLES."""
                            },
                            {
                                "role": "user",
                                "content": f"Analyze this SME data from a Bitcoin-native perspective: {data_context}"
                            }
                        ],
                        temperature=0.1,
                    )
                    
                    # 6. Professional BTC Rendering
                    st.markdown("---")
                    st.subheader("📋 Bitcoin Executive Audit Report")
                    st.markdown(f'<div class="report-box">{completion.choices[0].message.content}</div>', unsafe_allow_html=True)
                    
                    st.divider()
                    st.warning("⚡ **LIGHTNING GOVERNANCE:** Execution of these BTC recommendations requires a 2-of-3 Multi-Sig approval.")
                    
                except Exception as e:
                    st.error(f"Audit Error: {str(e)}")
                    
    except Exception as e:
        st.error(f"File Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("FinDiagnostix AI | Bitcoin Strategic Auditor | Developed by Salim Altrymy")
    
