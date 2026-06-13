
import streamlit as st
import sys
import os
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.database import get_all_transactions, get_all_customers

# st.set_page_config(page_title="Analytics - Meridian Bank", layout="wide")


st.title("Analytics & Reports")
st.markdown("---")

# Get data
transactions = get_all_transactions()
customers = get_all_customers()

total_deposits = sum(t[3] for t in transactions if t[2] == "deposit")
total_withdrawals = sum(t[3] for t in transactions if t[2] == "withdraw")
total_transfers = sum(t[3] for t in transactions if t[2] == "transfer")

# Key Metrics
st.subheader("Summary Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", len(customers))

with col2:
    st.metric("Total Deposits", f"Rs. {total_deposits:,.0f}")

with col3:
    st.metric("Total Withdrawals", f"Rs. {total_withdrawals:,.0f}")

with col4:
    st.metric("Net Balance", f"Rs. {(total_deposits - total_withdrawals):,.0f}")

st.markdown("")

# Charts
col_chart1, col_chart2 = st.columns(2)

# Chart 1 - Transaction Type Distribution
with col_chart1:
    st.subheader("Transaction Types Distribution")
    
    if transactions:
        deposit_count = len([t for t in transactions if t[2] == "deposit"])
        withdraw_count = len([t for t in transactions if t[2] == "withdraw"])
        transfer_count = len([t for t in transactions if t[2] == "transfer"])
        
        fig1 = go.Figure(data=[
            go.Pie(
                labels=['Deposits', 'Withdrawals', 'Transfers'],
                values=[deposit_count, withdraw_count, transfer_count],
                marker=dict(colors=['#16a34a', '#dc2626', '#2563eb'])
            )
        ])
        fig1.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No transaction data available")

# Chart 2 - Amount Distribution
with col_chart2:
    st.subheader("Amount by Transaction Type")
    
    if transactions:
        fig2 = go.Figure(data=[
            go.Bar(
                x=['Deposits', 'Withdrawals', 'Transfers'],
                y=[total_deposits, total_withdrawals, total_transfers],
                marker=dict(color=['#16a34a', '#dc2626', '#2563eb'])
            )
        ])
        fig2.update_layout(height=400, xaxis_title="Transaction Type", yaxis_title="Amount (Rs.)")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No transaction data available")

st.markdown("")

# Transaction Timeline
st.subheader("Recent Transaction Timeline")

if transactions:
    tx_data = []
    for tx in transactions[-20:]:
        tx_data.append({
            "Date": tx[4],
            "Account": tx[1],
            "Type": tx[2].capitalize(),
            "Amount": tx[3]
        })
    
    df_tx = pd.DataFrame(tx_data)
    
    fig3 = px.bar(
        df_tx,
        x="Date",
        y="Amount",
        color="Type",
        title="Transaction Amount Over Time",
        color_discrete_map={"Deposit": "#16a34a", "Withdraw": "#dc2626", "Transfer": "#2563eb"}
    )
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("No transaction data available")

st.markdown("---")

# Summary Report
st.subheader("Summary Report")

summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:
    st.write("**Total Transactions:**", len(transactions))
    st.write("**Deposit Count:**", len([t for t in transactions if t[2] == "deposit"]))
    st.write("**Withdrawal Count:**", len([t for t in transactions if t[2] == "withdraw"]))

with summary_col2:
    avg_deposit = total_deposits / max(len([t for t in transactions if t[2] == "deposit"]), 1)
    avg_withdrawal = total_withdrawals / max(len([t for t in transactions if t[2] == "withdraw"]), 1)
    st.write("**Average Deposit:**", f"Rs. {avg_deposit:,.0f}")
    st.write("**Average Withdrawal:**", f"Rs. {avg_withdrawal:,.0f}")
    st.write("**Net Flow:**", f"Rs. {(total_deposits - total_withdrawals):,.0f}")

with summary_col3:
    st.write("**Active Customers:**", len(customers))
    deposit_ratio = (total_deposits / (total_deposits + total_withdrawals) * 100) if (total_deposits + total_withdrawals) > 0 else 0
    st.write("**Deposit Ratio:**", f"{deposit_ratio:.1f}%")
    st.write("**System Status:**", "Active ✓")

st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#64748b; font-size:13px;">Meridian Bank Analytics Dashboard</div>',
    unsafe_allow_html=True,
)