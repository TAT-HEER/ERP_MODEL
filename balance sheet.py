import mysql.connector

def calculate_sum(table_name, column_name):
    mycursor.execute(f"SELECT SUM({column_name}) FROM {table_name}")
    return mycursor.fetchone()[0] or 0  # Handle None

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass",
    database="ledger_posting"
)
mycursor = db.cursor()

# Calculate sums for Assets
cash_debit_sum = calculate_sum("Cash", "debit_rs")
cash_credit_sum = calculate_sum("Cash", "credit_rs")
cash_balance = cash_debit_sum - cash_credit_sum

land_debit_sum = calculate_sum("Land", "debit_rs")
land_credit_sum = calculate_sum("Land", "credit_rs")
land_balance = land_debit_sum - land_credit_sum

supplies_debit_sum = calculate_sum("Supplies", "debit_rs")
supplies_credit_sum = calculate_sum("Supplies", "credit_rs")
supplies_balance = supplies_debit_sum - supplies_credit_sum

total_assets = cash_balance + land_balance + supplies_balance

# Calculate sums for Liabilities
account_payable_debit_sum = calculate_sum("Account_Payable", "debit_rs")
account_payable_credit_sum = calculate_sum("Account_Payable", "credit_rs")
account_payable_balance = account_payable_credit_sum - account_payable_debit_sum

total_liabilities = account_payable_balance

# Calculate sums for Equity
owner_capital_debit_sum = calculate_sum("Owner_Capital", "debit_rs")
owner_capital_credit_sum = calculate_sum("Owner_Capital", "credit_rs")
owner_capital_balance = owner_capital_credit_sum - owner_capital_debit_sum

owner_withdraw_debit_sum = calculate_sum("Owner_withdraw", "debit_rs")
owner_withdraw_credit_sum = calculate_sum("Owner_withdraw", "credit_rs")
owner_withdraw_balance = owner_withdraw_credit_sum - owner_withdraw_debit_sum

total_equity = owner_capital_balance - owner_withdraw_balance

# Create the balance sheet
balance_sheet = {
    "Assets": {
        "Cash": cash_balance,
        "Land": land_balance,
        "Supplies": supplies_balance,
        "Total Assets": total_assets,
    },
    "Liabilities": {
        "Account Payable": account_payable_balance,
        "Total Liabilities": total_liabilities,
    },
    "Equity": {
        "Owner Capital": owner_capital_balance,
        "Owner Withdraw": owner_withdraw_balance,
        "Total Equity": total_equity,
    },
}

# Print the balance sheet
print("Balance Sheet")
print("-------------")
print("Assets")
for key, value in balance_sheet["Assets"].items():
    print(f"{key}: {value}")

print("\nLiabilities")
for key, value in balance_sheet["Liabilities"].items():
    print(f"{key}: {value}")

print("\nEquity")
for key, value in balance_sheet["Equity"].items():
    print(f"{key}: {value}")

# Close the cursor and database connection
mycursor.close()
db.close()
