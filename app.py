import streamlit as st
from tax_calculator.slabs_new_regime import calculate_tax_new_regime
from tax_calculator.utils import format_inr
import plotly.graph_objects as go

st.set_page_config(page_title="Smart Tax Estimator", layout="centered")

st.title("🧾 Smart Tax Estimator (New Regime - FY 2025-26)")
st.caption("Built for Indian salaried, freelancers & investors")

st.markdown("### 💼 Income Input")
st.markdown("Enter your estimated yearly income from each source:")

# --- Income Inputs ---
salary = st.slider("Annual Salary (₹)", 0, 50_00_000, step=10000, value=12_00_000)
freelance = st.slider("Freelance/Side Income (₹)", 0, 20_00_000, step=10000, value=2_00_000)
capital_gains = st.slider("Capital Gains (Equity/Crypto/Other)", 0, 10_00_000, step=10000, value=1_00_000)
interest_income = st.slider("Interest from Savings/FDs (₹)", 0, 5_00_000, step=5000, value=50_000)

total_income = salary + freelance + capital_gains + interest_income

# --- Tax Calculation ---
total_tax, breakdown = calculate_tax_new_regime(total_income)

# --- Output ---
st.markdown("### 📊 Estimated Tax Summary")
st.metric("🪙 Total Tax Payable", format_inr(total_tax))
st.metric("📉 Effective Tax Rate", f"{(total_tax/total_income)*100:.2f}%" if total_income > 0 else "0%")

# --- Graph ---
fig = go.Figure(data=[
    go.Bar(name='Taxed Amount', x=[f"{k}"], y=[v]) for k, v in breakdown.items()
])
fig.update_layout(title="Slab-wise Tax Contribution", yaxis_title="₹", xaxis_title="Slab")
st.plotly_chart(fig, use_container_width=True)
