import mysql.connector
 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "",
    database = "pydbtest"
)
print(mydb) #to check The connection is made or not with the database

query = mydb.cursor() #using these you can execute any command on your database

# query.execute("CREATE DATABASE pydbtest") #creating Database

# query.execute("CREATE TABLE emp(id int PRIMARY KEY AUTO_INCREMENT,name varchar(244),education varchar(244))") #creating table using sql command


# to Insert any data into database 
sql = "INSERT INTO emp(name,education) VALUES(%s,%s)" #specified the columns which you have to enter the data

val = [   #python cursor object only accepts the values in form of tuples
    ("Akshay","BCA"),
    ("Harry","IIT"),
    ("Aman","CS"),
    ("Sharrdha","CS")
]

query.executemany(sql,val) #to execute many command using single line you have to use executemany instead of execute

mydb.commit() #to commit the changes sql topic

print(query.rowcount , "'s Row Inserted") # just for being nice and print how many rows inserted into database
        
