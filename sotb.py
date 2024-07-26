import mysql.connector

def calculate_sum(table_name, column_name):
    mycursor.execute(f"SELECT SUM({column_name}) FROM {table_name}")
    return mycursor.fetchone()[0]

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass",
    database="ledger_posting"
)
mycursor = db.cursor()

# Define the tables and their respective columns to sum
tables_columns = {
    "Cash": ["debit_rs", "credit_rs"],
    "Account_Payable": ["debit_rs", "credit_rs"],
    "Land": ["debit_rs", "credit_rs"],
    "Owner_Capital": ["debit_rs", "credit_rs"],
    "Owner_withdraw": ["debit_rs", "credit_rs"],
    "Rent": ["debit_rs", "credit_rs"],
    "Service_Revenue": ["debit_rs", "credit_rs"],
    "Supplies": ["debit_rs", "credit_rs"],
    "Utility": ["debit_rs", "credit_rs"],
}

# Iterate over each table and column, calculate the sum and print it
for table, columns in tables_columns.items():
    for column in columns:
        column_sum = calculate_sum(table, column)
        print(f"Sum of {column} in {table}: {column_sum}")

# Close the cursor and database connection
mycursor.close()
db.close()
