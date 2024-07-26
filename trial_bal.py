import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass",
    database="trail_balance"
)
mycursor = db.cursor()

# Creating tables
mycursor.execute("CREATE TABLE IF NOT EXISTS Cash (debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Cash (debit_rs, credit_rs) VALUES (%s, %s)", (37050, 31800))

mycursor.execute("CREATE TABLE IF NOT EXISTS Account_Payable (debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Account_Payable(debit_rs, credit_rs) VALUES (%s, %s)", (100, 350))


mycursor.execute("CREATE TABLE IF NOT EXISTS Land(debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Land(debit_rs, credit_rs) VALUES (%s, %s)", (30000, 0))


mycursor.execute("CREATE TABLE IF NOT EXISTS Owner_Capital (debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Owner_Capital (debit_rs, credit_rs) VALUES (%s, %s)", (0, 35000))


mycursor.execute("CREATE TABLE IF NOT EXISTS Owner_withdrawal(debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Owner_withdrawal(debit_rs, credit_rs) VALUES (%s, %s)", (0, 1200))


mycursor.execute("CREATE TABLE IF NOT EXISTS Rent (debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Rent (debit_rs, credit_rs) VALUES (%s, %s)", (400, 0))


mycursor.execute("CREATE TABLE IF NOT EXISTS Service_Revenue(debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Service_Revenue(debit_rs, credit_rs) VALUES (%s, %s)", (0, 1900))

mycursor.execute("CREATE TABLE IF NOT EXISTS Supplies (debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Supplies (debit_rs, credit_rs) VALUES (%s, %s)", (350, 150))

mycursor.execute("CREATE TABLE IF NOT EXISTS Utility (debit_rs SMALLINT UNSIGNED, credit_rs SMALLINT UNSIGNED)")
mycursor.execute("INSERT INTO Utility (debit_rs, credit_rs) VALUES (%s, %s)", (100, 0))

# Committing the changes
db.commit()
