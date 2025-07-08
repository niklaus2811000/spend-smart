import sqlite3
from datetime import datetime
import sys

DB_NAME = 'expenses.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(amount, category, date_str, description):
    try:
        if not date_str:
            date_str = datetime.today().strftime('%Y-%m-%d')
        datetime.strptime(date_str, '%Y-%m-%d')
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (amount, category, date, description)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, date_str, description))
        conn.commit()
        conn.close()
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid input. Please try again.\n")

def view_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses recorded yet.\n")
        return

    print("\nAll Expenses:")
    print("ID | Amount | Category | Date | Description")
    print("-- | ------ | -------- | ---- | -----------")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    print()

def filter_by_category(category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses WHERE category = ? ORDER BY date DESC', (category,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print(f"No expenses found in category: {category}\n")
        return

    print(f"\nExpenses in category '{category}':")
    print("ID | Amount | Category | Date | Description")
    print("-- | ------ | -------- | ---- | -----------")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    print()

def monthly_summary(month, year):
    try:
        datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.\n")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category, SUM(amount) FROM expenses
        WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY category
    ''', (month, year))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses found for that month.\n")
        return

    print(f"\nMonthly Summary for {month}-{year}:")
    print("Category | Total Spent")
    print("-------- | ------------")
    for row in rows:
        print(f"{row[0]} | {row[1]}")
    print()

def show_help():
    print("\nSpendSmart - Simple CLI Expense Tracker")
    print("Run this script using:")
    print("  python3 spend.py add <amount> <category> <date or 'today'> <description>")
    print("  python3 spend.py view")
    print("  python3 spend.py filter <category>")
    print("  python3 spend.py summary <MM> <YYYY>")
    print("  python3 spend.py help")
    print("\nExamples:")
    print("  python3 spend.py add 200 travel today Taxi to airport")
    print("  python3 spend.py filter food")
    print("  python3 spend.py summary 07 2025")
    print()

def main():
    init_db()
    args = sys.argv[1:]

    if not args or args[0] == 'help':
        show_help()
    elif args[0] == 'add' and len(args) >= 5:
        amount = float(args[1])
        category = args[2]
        date_str = datetime.today().strftime('%Y-%m-%d') if args[3] == 'today' else args[3]
        description = ' '.join(args[4:])
        add_expense(amount, category, date_str, description)
    elif args[0] == 'view':
        view_expenses()
    elif args[0] == 'filter' and len(args) == 2:
        filter_by_category(args[1])
    elif args[0] == 'summary' and len(args) == 3:
        monthly_summary(args[1], args[2])
    else:
        show_help()

if __name__ == "__main__":
    main()
