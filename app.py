import streamlit as st
import pandas as pd
from groq import Groq

# Page Config: Creating a professional financial look
st.set_page_config(page_title="FinDiagnostix AI | BTCFi", page_icon="⚡", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("📈 FinDiagnostix: BTCFi Edition")
st.subheader("AI-Driven CFO for Bitcoin-Native SMEs")
st.markdown("---")

# API Configuration from Streamlit Secrets
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Missing GROQ_API_KEY! Please check your Streamlit Secrets.")

# File Upload Section
uploaded_file = st.file_uploader("Upload SME Financial Records (CSV)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Data Ingested Successfully. Ready for Diagnostic Analysis.")
        
        # Data Preview
        with st.expander("👁️ Review Ingested Data Stream"):
            st.dataframe(df.head(10), use_container_width=True)

        # Execution Button
        if st.button("🚀 Run Precision Diagnosis"):
            with st.spinner("Processing Layers: Diagnostic -> What-if -> Execution..."):
                try:
                    # Serializing data for AI context (First 50 rows for precision)
                    data_context = df.head(50).to_string()
                    
                    # High-Precision BTCFi Prompt
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are a High-Precision BTCFi CFO. 
                                Your goal is to detect the 'Paper Profit Trap' and provide a 4-layered clinical diagnosis:
                                
                                1. 🔍 THE GAP: Precisely identify accounting profit vs. actual liquidity deficit.
                                2. 📉 WHAT-IF SCENARIO: Simulate a 30% BTC price drop or fee spike. How many days of runway remain?
                                3. ⚠️ THE RISK: The single most dangerous threat found in this specific data.
                                4. ⚡ ACTION COMMAND: A direct BTCFi/Lightning Network execution (e.g., L402 Loan, Automated Hedging).
                                
                                FORMAT: Use Bold Headers, Bullet points, and be extremely concise. Focus on NUMBERS from the data."""
                            },
                            {
                                "role": "user",
                                "content": f"Financial Data Input: {data_context}"
                            }
                        ],
                        temperature=0.1, # Lowest temperature for maximum accuracy
                        max_tokens=400,
                    )
                    
                    # Display Results
                    st.markdown("---")
                    st.header("🎯 AI Diagnostic Output")
                    
                    # Output in a clean box
                    st.info(completion.choices[0].message.content)
                    
                    # Governance Layer
                    st.warning("🛡️ **Human-in-the-Loop Governance:** Cryptographic approval required to trigger the suggested Lightning Network action.")
                    
                except Exception as e:
                    st.error(f"Diagnostic Engine Error: {str(e)}")
                    
    except Exception as e:
        st.error(f"File Parsing Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("FinDiagnostix AI | Built by Salim Altrymy | Powered by Groq Llama 3.3 & Lightning Network Protocol")
        
