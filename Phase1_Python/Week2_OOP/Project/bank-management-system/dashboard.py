import streamlit as st
from datetime import datetime
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.database import get_all_customers, get_all_transactions, create_tables

create_tables()

customers          = get_all_customers()
transactions       = get_all_transactions()
total_customers    = len(customers)
total_transactions = len(transactions)
total_deposits     = sum(t[3] for t in transactions if t[2] == "deposit")
total_withdrawals  = sum(t[3] for t in transactions if t[2] == "withdraw")
net_balance        = total_deposits - total_withdrawals

# Main Content
st.title("Meridian Bank - Admin Dashboard")
st.markdown("---")

# Welcome Message
now = datetime.now()
greeting = "Good Morning"
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader(greeting)
    st.caption("Welcome to the banking management system")
with col2:
    st.metric("Current Time", now.strftime("%I:%M %p"))

st.markdown("")

# KPI Cards
st.subheader("Key Metrics")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        label="Total Customers",
        value=total_customers,
        delta=f"{total_customers} registered"
    )

with kpi2:
    st.metric(
        label="Total Deposits",
        value=f"Rs. {total_deposits:,.0f}",
        delta="Inflow"
    )

with kpi3:
    st.metric(
        label="Total Withdrawals",
        value=f"Rs. {total_withdrawals:,.0f}",
        delta="Outflow"
    )

with kpi4:
    st.metric(
        label="Total Transactions",
        value=total_transactions,
        delta="All time"
    )

st.markdown("")

# Quick Actions
st.subheader("Quick Actions")
act1, act2, act3, act4 = st.columns(4)

with act1:
    if st.button("Add Customer", use_container_width=True):
        st.info("Navigate to Customers page to add new customer")

with act2:
    if st.button("Open Account", use_container_width=True):
        st.info("Navigate to Accounts page to open new account")

with act3:
    if st.button("Deposit", use_container_width=True):
        st.info("Navigate to Transactions page to deposit funds")

with act4:
    if st.button("Transfer", use_container_width=True):
        st.info("Navigate to Transactions page to transfer funds")

st.markdown("")

# Content Section
st.subheader("Activity")
left_col, right_col = st.columns([2, 1])

# Recent Transactions
with left_col:
    st.subheader("Recent Transactions")
    if transactions:
        tx_data = []
        for tx in transactions[-10:][::-1]:
            tx_data.append({
                "Account": tx[1],
                "Type": tx[2].capitalize(),
                "Amount": f"Rs. {tx[3]:,.0f}",
                "Date & Time": tx[4]
            })
        df_tx = pd.DataFrame(tx_data)
        st.dataframe(df_tx, use_container_width=True, hide_index=True)
    else:
        st.info("No transactions recorded yet")

# Right Column - Account Summary and Customers
with right_col:
    st.subheader("Account Summary")
    st.metric("Net Balance", f"Rs. {net_balance:,.0f}")
    st.metric("Savings Accounts", "0")
    st.metric("Current Accounts", "0")

    st.markdown("")
    st.subheader("Recent Customers")
    if customers:
        cust_data = []
        for c in customers[-5:][::-1]:
            cust_data.append({
                "Name": c[1],
                "CNIC": c[2],
                "Phone": c[3],
                "Status": "Active"
            })
        df_cust = pd.DataFrame(cust_data)
        st.dataframe(df_cust, use_container_width=True, hide_index=True)
    else:
        st.info("No customers registered yet")

st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#64748b; font-size:13px;">Meridian Bank Management System | by Syed Muhammad Abdul Nafeah</div>',
    unsafe_allow_html=True,
)