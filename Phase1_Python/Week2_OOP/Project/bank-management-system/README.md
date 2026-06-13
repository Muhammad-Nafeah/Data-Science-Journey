
# Meridian Bank - Management System

A simple banking management system built with **Python (OOP)**, **SQLite**, and **Streamlit**. This admin dashboard allows managing customers, accounts, and transactions with a clean, multi-page interface.

## Features

- **Dashboard** – Overview of key metrics (total customers, deposits, withdrawals, transactions) and recent activity
- **Customers** – Register and view customer records (name, CNIC, phone)
- **Accounts** – Open new Savings/Current accounts, view all accounts, and delete accounts (with balance and confirmation checks)
- **Transactions** – Deposit, withdraw, and transfer funds between accounts, with live balance updates and full transaction history
- **Analytics** – Visual insights into bank activity

## Tech Stack

- **Python 3.11** – Core logic (OOP-based account models)
- **SQLite** – Lightweight local database
- **Streamlit** – Web-based UI framework
- **Pandas** – Data display and formatting

## Project Structure

```
bank-management-system/
├── main.py                 # Entry point - navigation & routing
├── dashboard.py             # Main dashboard page
├── ui/
│   ├── customers.py         # Customer management page
│   ├── accounts.py          # Account management page
│   ├── transactions.py      # Transaction management page
│   └── analytics.py         # Analytics page
├── models/
│   ├── savings_account.py   # SavingAccount class
│   └── current_account.py   # CurrentAccount class
├── database/
│   └── database.py          # SQLite connection & queries
└── requirements.txt
```

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/bank-management-system.git
cd bank-management-system
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

## Database

The app uses SQLite (`database/bank.db`), created automatically on first run via `create_tables()`. It contains three tables:

- `customers` – customer records (name, CNIC, phone)
- `accounts` – account records (account number, type, balance, linked customer)
- `transactions` – transaction history (deposits, withdrawals, transfers)

## Author

**Syed Muhammad Abdul Nafeah**