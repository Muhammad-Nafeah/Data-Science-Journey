import streamlit as st

st.set_page_config(
    page_title="Meridian Bank - Admin Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

pages = [
    st.Page("dashboard.py", title="Dashboard"),
    st.Page("ui/customers.py", title="Customers"),
    st.Page("ui/accounts.py", title="Accounts"),
    st.Page("ui/transactions.py", title="Transactions"),
    st.Page("ui/analytics.py", title="Analytics"),
]

nav = st.navigation(pages, position="hidden")

# Custom sidebar styling
st.markdown("""
<style>
    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }

    /* Sidebar header / brand */
    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 18px 20px 16px 20px;
        border-bottom: 1px solid #1e293b;
        margin-bottom: 8px;
    }
    .sidebar-brand .text h2 {
        color: #ffffff;
        font-size: 40px;
        font-weight: 700;
        margin: 0;
        line-height: 1.2;
    }
    .sidebar-brand .text span {
        color: #64748b;
        font-size: 20px;
    }

    /* Section label */
    .nav-label {
        color: #ffffff;
        font-size: 20px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin: 16px 20px 8px 20px;
    }

    /* Page links - target all links inside sidebar nav */
    section[data-testid="stSidebar"] a {
        border-radius: 8px !important;
        margin: 2px 12px !important;
        padding: 10px 14px !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        transition: all 0.15s ease !important;
        text-decoration: none !important;
    }

    section[data-testid="stSidebar"] a,
    section[data-testid="stSidebar"] a span,
    section[data-testid="stSidebar"] a p,
    section[data-testid="stSidebar"] a div {
        color: #e2e8f0 !important;
    }

    section[data-testid="stSidebar"] a:hover {
        background-color: #334155 !important;
    }
    section[data-testid="stSidebar"] a:hover,
    section[data-testid="stSidebar"] a:hover span,
    section[data-testid="stSidebar"] a:hover p,
    section[data-testid="stSidebar"] a:hover div {
        color: #ffffff !important;
    }

    /* Active page link */
    section[data-testid="stSidebar"] a[aria-current="page"] {
        background-color: #b91c1c !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 6px rgba(185, 28, 28, 0.4) !important;
    }
    section[data-testid="stSidebar"] a[aria-current="page"],
    section[data-testid="stSidebar"] a[aria-current="page"] span,
    section[data-testid="stSidebar"] a[aria-current="page"] p,
    section[data-testid="stSidebar"] a[aria-current="page"] div {
        color: #ffffff !important;
    }

    /* Sidebar footer */
    .sidebar-footer {
        position: fixed;
        bottom: 16px;
        left: 0;
        width: inherit;
        padding: 0 40px;
        color: #ffffff;
        font-size: 15px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="text">
                <h2>Meridian Bank</h2>
                <span>Admin Panel</span>
            </div>
        </div>
        <p class="nav-label">Navigation Menu</p>
        """,
        unsafe_allow_html=True
    )
    for page in pages:
        st.page_link(page)

    st.markdown(
        '<div class="sidebar-footer">© 2025 Meridian Bank<br>v1.0.0</div>',
        unsafe_allow_html=True
    )

nav.run()