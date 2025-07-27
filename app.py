import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tax Estimator 2025-26", layout="wide")

st.title("📊 Smart Tax Estimator (New Regime 2025–26)")

st.markdown("Enter your income details below to estimate your total tax liability under the **new regime**.")

# --- INCOME INPUTS ---
st.header("💼 Income Sources")

col1, col2 = st.columns(2)

with col1:
    salary = st.slider("Salary Income (₹)", 0, 3000000, 900000, step=10000)
    freelance = st.slider("Freelance / Side Income (₹)", 0, 2000000, 200000, step=10000)

with col2:
    capital_gains = st.slider("Capital Gains (₹)", 0, 2000000, 150000, step=10000)
    interest = st.slider("Interest Income (₹)", 0, 1000000, 50000, step=5000)

# --- DATA AGGREGATION ---
income_sources = {
    "Salary": salary,
    "Freelance": freelance,
    "Capital Gains": capital_gains,
    "Interest": interest,
}

total_income = sum(income_sources.values())

# --- PIE CHART ---
st.subheader("💡 Income Source Breakdown")

fig, ax = plt.subplots()
ax.pie(income_sources.values(), labels=income_sources.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# --- TAX FORECASTING (NEW REGIME) ---
st.header("📉 Estimated Tax")

def calculate_tax_new_regime(income):
    tax = 0
    slabs = [
        (0, 300000, 0.0),
        (300001, 600000, 0.05),
        (600001, 900000, 0.10),
        (900001, 1200000, 0.15),
        (1200001, 1500000, 0.20),
        (1500001, float('inf'), 0.30),
    ]
    for slab in slabs:
        lower, upper, rate = slab
        if income > lower:
            taxed_amount = min(upper, income) - lower
            tax += taxed_amount * rate
    return tax

tax_payable = calculate_tax_new_regime(total_income)

st.success(f"✅ **Total Income:** ₹{total_income:,.0f}")
st.error(f"💰 **Estimated Tax Payable:** ₹{tax_payable:,.0f}")

