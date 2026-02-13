import streamlit as st
import pandas as pd
import plotly.express as px
import random

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="FinDiagnostix BTCFi",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ FinDiagnostix: BTCFi Edition")
st.markdown("AI-Powered Bitcoin Treasury & Liquidity Engine")

# -----------------------------
# Helper Functions
# -----------------------------

def reliability_score(df):
    total_cells = df.size
    missing = df.isnull().sum().sum()
    score = 1 - (missing / total_cells)
    return round(score * 100, 2)

def detect_paper_profit(df):
    revenue = df["Revenue_BTC"].sum()
    expenses = df["Expenses_BTC"].sum()
    receivables = df["Receivables_BTC"].sum()
    cash = df["Cash_BTC"].sum()

    net_profit = revenue - expenses
    liquidity_ratio = cash / (expenses + 1e-6)

    fake_profit_flag = net_profit > 0 and liquidity_ratio < 0.5

    return {
        "net_profit": net_profit,
        "liquidity_ratio": liquidity_ratio,
        "fake_profit": fake_profit_flag,
        "cash": cash,
        "monthly_expenses": df["Expenses_BTC"].mean()
    }

def calculate_runway(cash, monthly_expenses):
    if monthly_expenses == 0:
        return float("inf")
    return cash / monthly_expenses

def btc_stress_test(cash_btc, price_drop_percent):
    return cash_btc * (1 - price_drop_percent / 100)

def simulate_lightning_loan(amount_needed):
    interest_rate = round(random.uniform(0.01, 0.05), 4)
    total_repayment = amount_needed * (1 + interest_rate)
    return {
        "loan_amount": round(amount_needed, 4),
        "interest_rate": interest_rate,
        "repayment": round(total_repayment, 4),
        "status": "SIMULATED"
    }

# -----------------------------
# File Upload
# -----------------------------

uploaded_file = st.file_uploader("Upload BTC Financial CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Financial Data")
    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # Reliability
    # -----------------------------
    score = reliability_score(df)
    st.metric("🔒 Data Reliability Score (%)", score)

    # -----------------------------
    # AI Diagnostics
    # -----------------------------
    diagnosis = detect_paper_profit(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Net Profit (BTC)", round(diagnosis["net_profit"], 4))
        st.metric("Liquidity Ratio", round(diagnosis["liquidity_ratio"], 4))

    with col2:
        runway = calculate_runway(
            diagnosis["cash"],
            diagnosis["monthly_expenses"]
        )
        st.metric("Cash Runway (Months)", round(runway, 2))

    if diagnosis["fake_profit"]:
        st.error("⚠️ Paper Profit Trap Detected!")
    else:
        st.success("✅ Healthy Financial Position")

    # -----------------------------
    # Visualization
    # -----------------------------
    st.subheader("📈 Revenue vs Expenses")

    chart_df = pd.DataFrame({
        "Category": ["Revenue", "Expenses"],
        "BTC": [
            df["Revenue_BTC"].sum(),
            df["Expenses_BTC"].sum()
        ]
    })

    fig = px.bar(chart_df, x="Category", y="BTC")
    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # BTC Stress Test
    # -----------------------------
    st.subheader("📉 BTC Volatility Simulator")

    drop = st.slider("Simulate BTC Price Drop (%)", 0, 80, 20)
    stressed_value = btc_stress_test(diagnosis["cash"], drop)

    st.write(
        f"Post-Drop Treasury Value: {round(stressed_value,4)} BTC"
    )

    # -----------------------------
    # Execution Layer
    # -----------------------------
    if diagnosis["fake_profit"]:

        st.subheader("⚡ Lightning Execution Command Center")

        amount_needed = abs(diagnosis["net_profit"]) + 0.1
        loan_offer = simulate_lightning_loan(amount_needed)

        st.write("Loan Offer (Simulated L402):")
        st.json(loan_offer)

        approval = st.text_input(
            "Enter Cryptographic Approval Code to Execute"
        )

        if approval == "APPROVE123":
            st.success("✅ Lightning Loan Executed (Simulated)")
        else:
            st.warning("Awaiting Human Authorization...")
