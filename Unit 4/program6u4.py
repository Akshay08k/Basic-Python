import mysql.connector as mydb

db_name = input("enter DatabaseName: ")

try:
    pydb = mydb.connect(host="localhost", user="root", passwd="")

except:
    print("there is a problem in connecting mysql")

else:
    try:
        pycursor = pydb.cursor()

        pycursor.execute("CREATE DATABASE %s" % db_name)

        pycursor.close()

    except:
        print(
            "database %s already exists,please try to create database with othre name"
            % db_name
        )

    else:
        print("Databas %s sucessfully created" % db_name)
