import streamlit as st
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.database import save_customer, get_all_customers, get_customer_by_cnic


# st.set_page_config(page_title="Customers - Meridian Bank", layout="wide")


st.title("Customer Management")
st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["Add Customer", "View Customers", "Search Customer"])

# TAB 1 - Add Customer
with tab1:
    st.subheader("Register New Customer")
    
    with st.form("add_customer_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", placeholder="Enter customer name")
            cnic = st.text_input("CNIC", placeholder="42101-1234567-1")
        
        with col2:
            phone = st.text_input("Phone Number", placeholder="03001234567")
        
        submitted = st.form_submit_button("Register Customer", use_container_width=True)
        
        if submitted:
            if name and cnic and phone:
                try:
                    save_customer(name, cnic, phone)
                    st.success(f"Customer '{name}' registered successfully!")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.warning("Please fill all fields")

# TAB 2 - View All Customers
with tab2:
    st.subheader("All Registered Customers")
    
    customers = get_all_customers()
    
    if customers:
        cust_data = []
        for c in customers:
            cust_data.append({
                "ID": c[0],
                "Name": c[1],
                "CNIC": c[2],
                "Phone": c[3]
            })
        df = pd.DataFrame(cust_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption(f"Total Customers: {len(customers)}")
    else:
        st.info("No customers registered yet")

# TAB 3 - Search Customer
with tab3:
    st.subheader("Search Customer by CNIC")
    
    search_cnic = st.text_input("Enter CNIC", placeholder="42101-1234567-1")
    
    if st.button("Search", use_container_width=True):
        if search_cnic:
            result = get_customer_by_cnic(search_cnic)
            if result:
                st.success("Customer Found!")
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("ID", result[0])
                with col2:
                    st.metric("Name", result[1])
                with col3:
                    st.metric("CNIC", result[2])
                with col4:
                    st.metric("Phone", result[3])
            else:
                st.warning("Customer not found")
        else:
            st.warning("Please enter CNIC")

st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#64748b; font-size:13px;">Meridian Bank Customer Management System</div>',
    unsafe_allow_html=True,
)
