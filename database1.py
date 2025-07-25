import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
print()
try:

    cursor.execute("CREATE TABLE IF NOT EXISTS coustmer_details (coustId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS order_details (orderId INTEGER PRIMARY KEY AUTOINCREMENT, coustId INTEGER, orderName TEXT)")

    cursor.execute("INSERT OR IGNORE INTO coustmer_details VALUES (0,'raj','indore')")
    cursor.execute("INSERT OR IGNORE INTO coustmer_details VALUES (1,'raghav','bholaram')")
    cursor.execute("INSERT OR IGNORE INTO coustmer_details VALUES (2,'Aditya','dhmnd')")
    cursor.execute("INSERT OR IGNORE INTO coustmer_details VALUES (3,'Naveen','mhow')")
    cursor.execute("INSERT OR IGNORE INTO coustmer_details VALUES (4,'janhvi','bihar')")


    cursor.execute("INSERT OR IGNORE INTO order_details VALUES (0,1,'smart phone')")
    cursor.execute("INSERT OR IGNORE INTO order_details VALUES (1,1,'TV')")
    cursor.execute("INSERT OR IGNORE INTO order_details VALUES (2,3,'fridge')")

    cursor.execute(''' select * from coustmer_details ''')
    for i in cursor.fetchall():
        print(i)
    print()
    cursor.execute(''' select * from order_details ''')
    for i in cursor.fetchall():
        print(i)
    print()
    cursor.execute("SELECT * FROM coustmer_details inner join order_details on coustmer_details.coustId = order_details.coustId")
    for i in cursor.fetchall():
        print(i)
    print()


    cursor.execute("Update coustmer_details set name='vijay' where coustId=1")
    cursor.execute("Update coustmer_details set name='sanjay' where coustId=3")
    cursor.execute("SELECT * FROM coustmer_details inner join order_details on coustmer_details.coustId = order_details.coustId")
    for i in cursor.fetchall():
        print(i)
    print()

    a=cursor.execute("delete from coustmer_details where coustId=1")

    cursor.execute(
        "SELECT * FROM coustmer_details inner join order_details on coustmer_details.coustId = order_details.coustId")
    for i in cursor.fetchall():
        print(i)
    print()


except Exception as e:
    print(e)
    conn.rollback()
else:
    print("transaction completed")
finally:
    conn.commit()
    conn.close()
