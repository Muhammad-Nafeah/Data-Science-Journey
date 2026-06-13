import streamlit as st
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.database import save_account, get_all_customers, get_all_accounts, delete_account, save_transaction
from models.savings_account import SavingAccount
from models.current_account import CurrentAccount


st.title("Account Management")
st.markdown("---")

# Tabs
tab1, tab2 = st.tabs(["Open New Account", "View Accounts"])

# TAB 1 - Open New Account
with tab1:
    st.subheader("Open New Bank Account")
    
    customers = get_all_customers()
    
    if not customers:
        st.warning("No customers found. Please register a customer first.")
    else:
        with st.form("open_account_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                # Customer selection
                customer_names = [c[1] for c in customers]
                customer_cnics = {c[1]: c[2] for c in customers}
                selected_customer = st.selectbox("Select Customer", customer_names)
                customer_cnic = customer_cnics[selected_customer]
                
                account_number = st.text_input("Account Number", placeholder="PKR-001", value=f"PKR-{len(customers)+1:03d}")
            
            with col2:
                account_type = st.selectbox("Account Type", ["Savings", "Current"])
                initial_balance = st.number_input("Initial Balance", min_value=0.0, step=1000.0)
            
            # Account-specific fields
            if account_type == "Savings":
                interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
            else:
                overdraft_limit = st.number_input("Overdraft Limit", min_value=0.0, step=1000.0, value=10000.0)
            
            submitted = st.form_submit_button("Open Account", use_container_width=True)
            
            if submitted:
                if account_number and initial_balance >= 0:
                    try:
                        save_account(account_number, account_type, initial_balance, customer_cnic)
                        if initial_balance > 0:
                            save_transaction(account_number, "deposit", initial_balance)
                        st.success(f"Account '{account_number}' opened successfully for {selected_customer}!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                else:
                    st.warning("Please fill all required fields")

# TAB 2 - View Accounts
with tab2:
    st.subheader("All Bank Accounts")

    accounts = get_all_accounts()

    col1, col2 = st.columns([3, 1])

    with col1:
        if accounts:
            acc_data = []
            for a in accounts:
                acc_data.append({
                    "Account Number": a[1],
                    "Type": a[2],
                    "Balance": f"Rs. {a[3]:,.0f}",
                    "Customer CNIC": a[4],
                })
            df_acc = pd.DataFrame(acc_data)
            st.dataframe(df_acc, use_container_width=True, hide_index=True)
        else:
            st.info("No accounts found. Open an account from the 'Open New Account' tab.")

    with col2:
        total_accounts = len(accounts)
        savings_count = sum(1 for a in accounts if a[2] == "Savings")
        current_count = sum(1 for a in accounts if a[2] == "Current")

        st.metric("Total Accounts", total_accounts)
        st.metric("Savings", savings_count)
        st.metric("Current", current_count)

    st.markdown("---")
    st.subheader("Delete Account")

    if accounts:
        acc_numbers = [a[1] for a in accounts]
        acc_balances = {a[1]: a[3] for a in accounts}

        acc_to_delete = st.selectbox("Select Account to Delete", acc_numbers)
        balance = acc_balances[acc_to_delete]

        if balance > 0:
            st.warning(
                f"Account '{acc_to_delete}' has a remaining balance of Rs. {balance:,.0f}. "
                "Withdraw or transfer all funds before deleting this account."
            )
        else:
            confirm = st.checkbox(f"I confirm I want to permanently delete account '{acc_to_delete}'")

            if st.button("Delete Account", type="primary", disabled=not confirm):
                delete_account(acc_to_delete)
                st.success(f"Account '{acc_to_delete}' deleted successfully!")
                st.rerun()
    else:
        st.info("No accounts available to delete.")

st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#64748b; font-size:13px;">Meridian Bank Account Management System</div>',
    unsafe_allow_html=True,
)