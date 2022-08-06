import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sanyosamsung22mysqldatabasecom",
    )

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE login_datas")

# to show the databses

my_cursor.execute("SHOW DTABASES")

for db in my_cursor:
    print(db)