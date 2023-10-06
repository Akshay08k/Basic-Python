import mysql.connector as mydb

db_name = input("Enter DatabaseName:")

tb_name = input("Enter TableName:")


def create_table():
    pycursor = pydb.cursor()

    pycursor.execute(
        "CREATE TABLE %s (eid int primary key,name varchar(20),salint)" % tb_name
    )

    print("Table %s is created successfully..." % tb_name)

    pycursor.close()

    insert_data()


def insert_data():
    n = int(input("Enter how many rows you want:"))

    for i in range(n):
        pycursor = pydb.cursor()

        eid1 = int(input("Enter Employee id:"))

        name1 = input("Enter Name")

        sal1 = int(input("Enter Salary:"))

        pycursor.execute(
            "insert into {0}(eid,name,sal) values({1},'{2}',{3})".format(
                tb_name, eid1, name1, sal1
            )
        )

        pydb.commit()

        print(pycursor.rowcount, "Row Inserted Successfully")

        pycursor.close()

        select_data()


def select_data():
    pycursor = pydb.cursor()

    pycursor.execute("SELECT * FROM %s" % tb_name)

    res = pycursor.fetchall()

    if pycursor.rowcount:
        print(res, "\n")

    else:
        insert_data()


try:
    pydb = mydb.connect(host="localhost", user="root", passwd="", database=db_name)

except:
    print("Connection error.database name does not exists.")

else:
    try:
        create_table()

    except:
        print("Table %s already exists" % tb_name)

        select_data()

    else:
        print("Data inserted sucessfully")
