import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="FinDiagnostix | BTC AI CFO", page_icon="₿", layout="wide")

# --- 2. CUSTOM STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 1px solid #f7931a; padding: 15px; border-radius: 10px; border-left: 5px solid #f7931a; }
    .action-card { background-color: #1c2128; border-left: 5px solid #238636; padding: 20px; border-radius: 8px; margin: 10px 0; }
    .warning-card { background-color: #1c2128; border-left: 5px solid #da3633; padding: 20px; border-radius: 8px; }
    .shield-box { background-color: #0d1117; border: 1px dashed #f7931a; padding: 10px; border-radius: 10px; text-align: center; }
    .stButton>button { background-color: #f7931a; color: white; font-weight: bold; width: 100%; border-radius: 8px; border: none; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: DATA INPUT ---
st.sidebar.image("https://cryptologos.cc/logos/bitcoin-btc-logo.png", width=80)
st.sidebar.title("₿ BTCFi Treasury")

with st.sidebar:
    btc_price = 48000  # Global Price Ref
    rev_btc = st.number_input("Monthly Revenue (BTC)", value=2.50)
    cash_btc = st.number_input("Liquid BTC Holdings", value=0.45)
    receivables_btc = st.number_input("Receivables (BTC)", value=1.60)
    payables_btc = st.number_input("Payables (BTC)", value=1.20)
    burn_btc = st.number_input("Monthly Burn (BTC)", value=0.60)
    
    st.write("---")
    # DATA SHIELD LOGIC
    reliability = 100
    if burn_btc > rev_btc: reliability -= 30
    if cash_btc < (burn_btc * 0.5): reliability -= 20
    
    st.markdown(f'<div class="shield-box"><h4 style="color:#f7931a;margin:0;">🛡️ DATA SHIELD</h4><h2>{reliability}%</h2></div>', unsafe_allow_html=True)

# --- 4. CORE LOGIC ---
gap = receivables_btc - payables_btc
runway = round(cash_btc / (burn_btc / 30)) if burn_btc > 0 else 999
is_risky = cash_btc < payables_btc

# --- 5. MAIN INTERFACE ---
st.title("₿ FinDiagnostix: BTC Edition")
st.markdown("#### *AI-Powered Bitcoin Treasury & Liquidity Execution*")
st.write("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Net BTC Liquidity", f"₿ {cash_btc:.4f}", f"${(cash_btc*btc_price):,.0f} USD")
with col2:
    st.metric("BTC Runway", f"{runway} Days", "CRITICAL" if runway < 30 else "STABLE")
with col3:
    st.metric("Paper Profit Gap", f"₿ {gap:.4f}")

# Visualization
st.write("### 🧠 Diagnostic Visualization")
fig = go.Figure(data=[
    go.Bar(name='Cash', x=['Status'], y=[cash_btc], marker_color='#f7931a'),
    go.Bar(name='Receivables', x=['Status'], y=[receivables_btc], marker_color='#58a6ff'),
    go.Bar(name='Payables', x=['Status'], y=[payables_btc], marker_color='#da3633')
])
fig.update_layout(barmode='group', template="plotly_dark", height=300, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig, use_container_width=True)

# Action Layer
if is_risky:
    st.markdown('<div class="warning-card">⚠️ <b>Liquidity Gap:</b> You are in the "Paper Profit Trap".</div>', unsafe_allow_html=True)
    st.write("#### ⚡ BTCFi Execution Layer")
    if st.button("⚡ EXECUTE LIGHTNING NETWORK LOAN"):
        with st.spinner("Requesting L402 Liquidity..."):
            time.sleep(2)
            st.success(f"✅ SUCCESS: ₿ {round(receivables_btc*0.5, 3)} injected via Lightning Network.")
            st.balloons()
else:
    st.success("Treasury health is optimal. Accumulate more Sats.")

st.write("---")
st.caption("FinDiagnostix v3.0 | Bitcoin Accelerator Edition | Developed by Salim Altrymy")
    
