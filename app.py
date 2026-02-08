# app.py
"AI-Powered Bitcoin Treasury that solves the Paper Profit Trap via automated Lightning Network liquidity."
import streamlit as st
import pandas as pd
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="FinDiagnostix | Bitcoin AI CFO", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM STYLING (Bitcoin Orange Theme) ---
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #f7931a; padding: 15px; border-radius: 10px; }
    .action-card { background-color: #1c2128; border-left: 5px solid #f7931a; padding: 20px; border-radius: 8px; margin: 10px 0; }
    .stButton>button { background-color: #f7931a; color: white; border-radius: 5px; width: 100%; border: none; height: 3em; font-weight: bold; font-size: 1.1em; }
    .stButton>button:hover { background-color: #e88316; color: white; border: 1px solid white; }
    h1, h2, h3 { color: #f7931a; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: BTCFi DATA INPUT ---
st.sidebar.image("https://cryptologos.cc/logos/bitcoin-btc-logo.png", width=80)
st.sidebar.title("BTCFi Treasury Input")
st.sidebar.info("Simulate your Bitcoin-native company's financials.")

btc_price = 48000  # Global BTC/USD Price Reference
revenue_btc = st.sidebar.number_input("Monthly Revenue (BTC)", value=2.5)
cash_btc = st.sidebar.number_input("Current BTC Holdings", value=0.4)
receivables_btc = st.sidebar.number_input("Accounts Receivable (BTC)", value=1.6)
payables_btc = st.sidebar.number_input("Accounts Payable (BTC)", value=1.2)
burn_rate_btc = st.sidebar.number_input("Monthly Burn Rate (BTC)", value=0.5)

# --- LOGIC: BTCFi DIAGNOSTIC ENGINE ---
paper_profit_gap = receivables_btc - payables_btc
cash_runway = round(cash_btc / (burn_rate_btc / 30)) if burn_rate_btc > 0 else 999
is_risky = cash_btc < payables_btc

# --- MAIN INTERFACE ---
st.title("📊 FinDiagnostix [BTCFi Edition]")
st.markdown("#### *The Prescriptive AI Layer for Bitcoin-Native Treasuries*")
st.write("---")

# 1. THE PULSE (Key Metrics)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total BTC Liquidity", f"₿ {cash_btc:.4f}", delta=f"${(cash_btc * btc_price):,.0f} USD")
with col2:
    st.metric("BTC Cash Runway", f"{cash_runway} Days", delta="CRITICAL" if cash_runway < 30 else "STABLE", delta_color="inverse" if cash_runway < 30 else "normal")
with col3:
    st.metric("Paper Profit Gap", f"₿ {paper_profit_gap:.4f}", help="BTC earned on paper but not yet settled in your wallet.")

st.write("### 🧠 AI Diagnostic Lab")

if is_risky:
    st.error(f"🚨 Liquidity Alert: Bitcoin Cash-Flow Gap Detected!")
    st.markdown(f"""
    <div class="action-card">
        <h4>⚡ EXECUTION LAYER: BTC-Backed Liquidity Bridge</h4>
        <p>The system has detected a <b>'Paper Profit Trap'</b>. You have high receivables but low liquid cash. 
        <b>AI Recommendation:</b> Secure an instant <b>Lightning Network Loan</b> using your ₿ {receivables_btc} receivables as collateral via L402 protocol.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # --- THE EXECUTION TRIGGER ---
    if st.button("⚡ INITIATE L402 LIGHTNING LOAN"):
        with st.spinner("Broadcasting Request to Lightning Node..."):
            time.sleep(2.5) # Simulating handshake
            loan_impact = round(receivables_btc * 0.5, 4)
            st.success(f"✅ EXECUTION SUCCESS: ₿ {loan_impact} Liquidity injected into Treasury via Lightning Network.")
            st.balloons()
else:
    st.success("Treasury health is optimal. AI suggests rebalancing 15% of surplus into yield-generating BTCFi protocols.")

# 2. THE SIMULATOR (Sats-Efficiency)
st.write("---")
st.write("### 🧪 BTC Efficiency Simulator")
boost = st.slider("Optimize Settlement Speed via Lightning Network (%)", 0, 100, 30)
simulated_cash = cash_btc + (receivables_btc * (boost / 100))
st.info(f"By accelerating invoice settlements via Lightning, your liquid BTC position scales to: ₿ {simulated_cash:.4f}")

# 3. PITCH MODE (For Judges)
if st.checkbox("Show btc/acc Pitch Summary"):
    st.write("---")
    st.subheader("🎤 Pitching FinDiagnostix")
    st.markdown("""
    * **Problem:** SMEs in the Bitcoin ecosystem fail due to liquidity mismanagement, not just price volatility.
    * **Solution:** An AI CFO that monitors the 'Paper Profit Trap' and triggers BTCFi actions.
    * **Execution:** Moving from dashboards to **Active Execution Layers** using L402 and Lightning Network.
    """)

st.caption("FinDiagnostix Prototype - Built for btc/acc Global Hackathon 2026")
