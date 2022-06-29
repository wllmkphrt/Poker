import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="TestPassword!",
  database="Poker"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255), cash DECIMAL(15,2))")
