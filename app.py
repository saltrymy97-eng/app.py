import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. CONFIGURATION & STYLING ---
st.set_page_config(page_title="FinDiagnostix | BTC AI CFO", page_icon="📈", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; border-left: 5px solid #f7931a; }
    .action-card { background-color: #1c2128; border-left: 5px solid #238636; padding: 20px; border-radius: 8px; margin: 10px 0; }
    .warning-card { background-color: #1c2128; border-left: 5px solid #da3633; padding: 20px; border-radius: 8px; }
    .shield-box { background-color: #0d1117; border: 1px dashed #f7931a; padding: 10px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR: DATA INPUT ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/5968/5968260.png", width=80)
st.sidebar.title("💳 Financial Ledger")

with st.sidebar:
    revenue = st.number_input("Monthly Revenue ($)", value=120000)
    cash = st.number_input("Current Cash ($)", value=18000)
    receivables = st.number_input("Accounts Receivable ($)", value=75000)
    payables = st.number_input("Accounts Payable ($)", value=55000)
    burn_rate = st.number_input("Monthly Expenses ($)", value=25000)
    
    st.write("---")
    # --- DATA SHIELD LOGIC ---
    reliability_score = 100
    shield_issues = []
    if burn_rate > revenue: 
        reliability_score -= 30
        shield_issues.append("Negative Cash Flow")
    if cash < (burn_rate * 0.5): 
        reliability_score -= 20
        shield_issues.append("Low Liquidity Buffer")
    
    st.markdown(f"""
    <div class="shield-box">
        <h4 style='color:#f7931a; margin:0;'>🛡️ DATA SHIELD</h4>
        <h2 style='margin:0;'>{reliability_score}%</h2>
        <p style='font-size:0.8em;'>Reliability Score</p>
    </div>
    """, unsafe_allow_html=True)
    for issue in shield_issues:
        st.caption(f"⚠️ {issue}")

# --- 3. CORE LOGIC ---
paper_profit_gap = receivables - payables
# حساب فترة البقاء بالشهور
runway_months = round(cash / burn_rate, 1) if burn_rate > 0 else 99
btc_stress_cash = cash * 0.7  # محاكاة هبوط البيتكوين 30%

# --- 4. MAIN INTERFACE ---
st.title("📈 FinDiagnostix: BTC Edition")
st.markdown("*Strategic AI Financial Diagnosis for BTC-Native SMEs*")
st.write("---")

# Metrics Row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Net Liquidity", f"${cash:,}", "-12%")
m2.metric("Survival Runway", f"{runway_months} Mo", "Critical" if runway_months < 1 else "Stable")
m3.metric("Paper Profit Gap", f"${paper_profit_gap:,}")
m4.metric("BTC Stress Cash", f"${btc_stress_cash:,.0f}", "-30% Risk")

# Visualizing the Gap
st.write("### 🧠 Diagnostic Visualization")
fig = go.Figure(data=[
    go.Bar(name='Available Cash', x=['Liquidity Status'], y=[cash], marker_color='#238636'),
    go.Bar(name='Receivables (Paper)', x=['Liquidity Status'], y=[receivables], marker_color='#58a6ff'),
    go.Bar(name='Payables (Debt)', x=['Liquidity Status'], y=[payables], marker_color='#da3633')
])
fig.update_layout(barmode='group', template="plotly_dark", height=300, margin=dict(l=20, r=20, t=20, b=20))
st.plotly_chart(fig, use_container_width=True)



# Analysis Results
if cash < payables:
    st.markdown(f"""
    <div class="warning-card">
        <h3 style='color:#da3633; margin:0;'>⚠️ CRITICAL: The Paper Profit Trap</h3>
        <p>Your revenue is <b>${revenue:,}</b>, but you cannot cover your <b>${payables:,}</b> debts with current cash. 
        You are legally profitable but operationally insolvent.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("#### 🎯 AI Strategic Recommendations")
    col_rec1, col_rec2 = st.columns(2)
    with col_rec1:
        st.markdown("""
        <div class="action-card">
            <b>1. BTC Liquidity (L402):</b> Use your BTC as collateral for a Lightning-fast loan of <b>$20,000</b> to bridge the payables gap.
        </div>
        """, unsafe_allow_html=True)
    with col_rec2:
        st.markdown("""
        <div class="action-card">
            <b>2. Receivables Hack:</b> Offer a 2% discount for payments made via <b>Bitcoin Lightning</b> to speed up collection by 40%.
        </div>
        """, unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("FinDiagnostix AI Engine | Developed by Salim Altrymy | v2.0 Stable")
