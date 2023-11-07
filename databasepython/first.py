import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",  # Changed 'username' to 'user'
    passwd="",  # You might need to provide your MySQL password here
    database="pydbtest",
)

mycursor = mydb.cursor()

val = [("Akshay", "Akshay123"), ("user2", "user123"), ("user3", "user234")]

sql = "SELECT password FROM user WHERE name = 'Akshay'"

mycursor.execute(sql)

result = mycursor.fetchone()

compare = result[0]


print(compare)
name = input("Enter Your Name : ")
password = input("Enter Your password : ")

if password == compare:
    print("You Are Logged In")
else:
    print("No You cant login")
