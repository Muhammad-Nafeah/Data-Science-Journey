import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "bank.db")

def get_connection():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    return connection, cursor

def create_tables():

    connection, cursor = get_connection()

    # customers table
    cursor.execute("""
                   
        CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                cnic TEXT,
                phone TEXT
                )
            """)
    
    # accounts table
    cursor.execute("""
                   
        CREATE TABLE IF NOT EXISTS accounts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT,
                account_type TEXT,
                balance REAL,
                customer_cnic TEXT
                )
            """)
    
    # transaction table
    cursor.execute("""
                   
        CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT,
                type TEXT,
                amount REAL,
                date TEXT
                )
            """)
    
    connection.commit()
    connection.close()
    print("Tables created successfully!")


def save_customer(name, cnic, phone):

    connection, cursor = get_connection()

    cursor.execute("""

        INSERT INTO customers (name, cnic, phone)
        VALUES (?, ?, ?)
        """, (name, cnic, phone))
    connection.commit()
    connection.close()
    print(f"Customer {name} saved successfully!")

def save_account(account_number, account_type, balance, customer_cnic):

    connection, cursor = get_connection()

    cursor.execute("""
        INSERT INTO accounts (account_number, account_type, balance, customer_cnic)
        VALUES (?, ?, ?, ?)
        """,(account_number, account_type, balance, customer_cnic))
    
    connection.commit()
    connection.close()
    print(f"Account {account_number} saved successfully!")


def save_transaction(account_number, type, amount):

    connection, cursor = get_connection()

    date = str(datetime.now())

    cursor.execute("""
        INSERT INTO transactions(account_number, type, amount, date)
        VALUES (?, ?, ?, ?)
        """,(account_number, type, amount, date))
    
    connection.commit()
    connection.close()
    print(f"Transaction saved! Type: {type}, Amount: Rs.{amount}")

def get_all_customers():

    connection, cursor = get_connection()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    connection.close()
    return rows

def get_all_accounts():
    connection, cursor = get_connection()
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    connection.close()
    return rows

def get_customer_by_cnic(cnic):

    connection, cursor = get_connection()
    cursor.execute("""
        SELECT *
        FROM customers
        where cnic = ?
    """, (cnic,)) #(cnic,) -> tuple
    row = cursor.fetchone() ## fetchone() — only one customer per CNIC
    connection.close()
    return row

def get_all_transactions():

    connection, cursor = get_connection()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete_account(account_number):
    connection, cursor = get_connection()
    cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
    connection.commit()
    connection.close()
    print(f"Account {account_number} deleted successfully!")

def get_account_by_number(account_number):
    connection, cursor = get_connection()
    cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
    row = cursor.fetchone()
    connection.close()
    return row

def update_account_balance(account_number, new_balance):
    connection, cursor = get_connection()
    cursor.execute(
        "UPDATE accounts SET balance = ? WHERE account_number = ?",
        (new_balance, account_number)
    )
    connection.commit()
    connection.close()
    print(f"Account {account_number} balance updated to Rs.{new_balance}")
