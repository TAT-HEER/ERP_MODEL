import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass",
    database="ledger_posting"
)
mycursor = db.cursor()

# Creating tables
mycursor.execute("CREATE TABLE IF NOT EXISTS Cash (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Cash (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by owner capital", 35000, 0))
mycursor.execute("INSERT INTO Cash (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by land", 0, 30000))
mycursor.execute("INSERT INTO Cash (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by service revenue", 1900, 0))
mycursor.execute("INSERT INTO Cash (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by account payable", 0, 100))
mycursor.execute("INSERT INTO Cash (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by rent and utility", 0, 500))
mycursor.execute("INSERT INTO Cash (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by supplies", 150, 0))
mycursor.execute("INSERT INTO Cash (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by owner withdrawal", 0, 1200))

mycursor.execute("CREATE TABLE IF NOT EXISTS Owner_Capital (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Owner_Capital (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 0, 35000))

mycursor.execute("CREATE TABLE IF NOT EXISTS Land (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Land (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 30000, 0))

mycursor.execute("CREATE TABLE IF NOT EXISTS Service_Revenue (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Service_Revenue (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 0, 1900))

mycursor.execute("CREATE TABLE IF NOT EXISTS Account_Payable (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Account_Payable (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 100, 0))
mycursor.execute("INSERT INTO Account_Payable (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by supplies", 0, 350))

mycursor.execute("CREATE TABLE IF NOT EXISTS Rent (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Rent (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 400, 0))

mycursor.execute("CREATE TABLE IF NOT EXISTS Utility (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Utility (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 100, 0))

mycursor.execute("CREATE TABLE IF NOT EXISTS Supplies (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Supplies (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 0, 150))
mycursor.execute("INSERT INTO Supplies (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by account payable", 350, 0))

mycursor.execute("CREATE TABLE IF NOT EXISTS Owner_withdraw (Particulars VARCHAR(50), debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Owner_withdraw (Particulars, debit_rs, credit_rs) VALUES (%s, %s, %s)", ("by cash", 0, 1200))

# Committing the changes
db.commit()
