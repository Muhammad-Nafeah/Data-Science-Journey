import streamlit as st
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.database import (
    save_transaction,
    get_all_transactions,
    get_account_by_number,
    update_account_balance,
)


st.title("Transaction Management")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Deposit", "Withdraw", "Transfer", "History"])

# TAB 1 - Deposit
with tab1:
    st.subheader("Deposit Funds")
    
    with st.form("deposit_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            account_number = st.text_input("Account Number", placeholder="PKR-001")
        
        with col2:
            amount = st.number_input("Amount (Rs.)", min_value=0.0, step=100.0)
        
        submitted = st.form_submit_button("Deposit", use_container_width=True)
        
        if submitted:
            if account_number and amount > 0:
                account = get_account_by_number(account_number)
                if not account:
                    st.error(f"Account '{account_number}' not found")
                else:
                    try:
                        new_balance = account[3] + amount
                        update_account_balance(account_number, new_balance)
                        save_transaction(account_number, "deposit", amount)
                        st.success(f"Deposit of Rs. {amount:,.0f} successful! New balance: Rs. {new_balance:,.0f}")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter valid account number and amount")

# TAB 2 - Withdraw
with tab2:
    st.subheader("Withdraw Funds")
    
    with st.form("withdraw_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            account_number = st.text_input("Account Number", placeholder="PKR-001", key="withdraw_acc")
        
        with col2:
            amount = st.number_input("Amount (Rs.)", min_value=0.0, step=100.0, key="withdraw_amt")
        
        submitted = st.form_submit_button("Withdraw", use_container_width=True)
        
        if submitted:
            if account_number and amount > 0:
                account = get_account_by_number(account_number)
                if not account:
                    st.error(f"Account '{account_number}' not found")
                elif amount > account[3]:
                    st.error(f"Insufficient balance. Available: Rs. {account[3]:,.0f}")
                else:
                    try:
                        new_balance = account[3] - amount
                        update_account_balance(account_number, new_balance)
                        save_transaction(account_number, "withdraw", amount)
                        st.success(f"Withdrawal of Rs. {amount:,.0f} successful! New balance: Rs. {new_balance:,.0f}")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter valid account number and amount")

# TAB 3 - Transfer
with tab3:
    st.subheader("Transfer Funds")
    
    with st.form("transfer_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            from_account = st.text_input("From Account", placeholder="PKR-001")
            amount = st.number_input("Amount (Rs.)", min_value=0.0, step=100.0, key="transfer_amt")
        
        with col2:
            to_account = st.text_input("To Account", placeholder="PKR-002")
        
        submitted = st.form_submit_button("Transfer", use_container_width=True)
        
        if submitted:
            if from_account and to_account and amount > 0:
                if from_account == to_account:
                    st.error("From and To accounts cannot be the same")
                else:
                    source = get_account_by_number(from_account)
                    destination = get_account_by_number(to_account)

                    if not source:
                        st.error(f"Account '{from_account}' not found")
                    elif not destination:
                        st.error(f"Account '{to_account}' not found")
                    elif amount > source[3]:
                        st.error(f"Insufficient balance in '{from_account}'. Available: Rs. {source[3]:,.0f}")
                    else:
                        try:
                            new_source_balance = source[3] - amount
                            new_dest_balance = destination[3] + amount

                            update_account_balance(from_account, new_source_balance)
                            update_account_balance(to_account, new_dest_balance)

                            save_transaction(from_account, "transfer", amount)

                            st.success(
                                f"Transfer of Rs. {amount:,.0f} from {from_account} to {to_account} successful!"
                            )
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
            else:
                st.warning("Please fill all fields with valid data")

# TAB 4 - Transaction History
with tab4:
    st.subheader("Transaction History")
    
    transactions = get_all_transactions()
    
    if transactions:
        tx_data = []
        for tx in transactions:
            tx_data.append({
                "ID": tx[0],
                "Account": tx[1],
                "Type": tx[2].capitalize(),
                "Amount": f"Rs. {tx[3]:,.0f}",
                "Date & Time": tx[4]
            })
        df = pd.DataFrame(tx_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption(f"Total Transactions: {len(transactions)}")
    else:
        st.info("No transactions recorded yet")

st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#64748b; font-size:13px;">Meridian Bank Transaction Management System</div>',
    unsafe_allow_html=True,
)