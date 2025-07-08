# SpendSmart – Simple CLI Expense Tracker

SpendSmart is a beginner-friendly command-line tool to help you track and manage your expenses locally using Python and SQLite. It allows you to add, view, filter, and summarize expenses with minimal setup.

---

##  Description


This project is designed as a simple yet functional personal finance tracker. It runs entirely on your local machine and stores expenses in an SQLite database file (`expenses.db`). You can interact with the tool directly from the terminal using intuitive commands.

---

##  Features

- Add expenses with amount, category, date, and description
- View all expenses sorted by date
- Filter expenses by category
- Get a monthly category-wise spending summary
- Simple help menu for command reference

---

##  Requirements


- Python 3.7 or later
- No external libraries required (uses built-in `sqlite3`, `datetime`, `sys`)

---

##  How to Use

### Run from terminal using:
```bash
python3 spend.py <command> [arguments...]
```

### 📄 Supported Commands


| Command   | Description                                              | Example                                                       |
|-----------|----------------------------------------------------------|---------------------------------------------------------------|
| `add`     | Add a new expense with amount, category, date, and description | `python3 spend.py add 200 food today "Lunch at cafe"`   |
| `view`    | View all recorded expenses                               | `python3 spend.py view`                                       |
| `filter`  | Show expenses filtered by category                       | `python3 spend.py filter travel`                              |
| `summary` | Monthly spending summary by category                     | `python3 spend.py summary 07 2025`                            |
| `help`    | Display usage instructions                               | `python3 spend.py help`                                       |

> 💡 **Note:** All 4 arguments are required for the `add` command: `amount`, `category`, `date`, and `description`.  
> You can use `'today'` as a shortcut for the current date.


## Screenshots


<img width="1055" alt="image" src="https://github.com/user-attachments/assets/506b7368-76fe-4cfb-b068-720622d0099c" />


## Author

Developed by Aryan Khudlain — inspired by real-world personal finance needs and aligned with software development internships involving backend logic, database design, and command-line utilities.




