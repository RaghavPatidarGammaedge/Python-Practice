import sqlite3
from flask import Flask,request
import requests



conn1=sqlite3.connect('flaskDB.db')
cursor=conn1.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, password TEXT)")
conn1.commit()
conn1.close()

app = Flask(__name__)

@app.teardown_appcontext
@app.route('/forPut',methods=['POST'])
def forPut():
    name = request.form.get('name')
    password = request.form.get('password')

    try:
        conn2 = sqlite3.connect('flaskDB.db')
        cursor = conn2.cursor()
        cursor.execute('insert into users values (?,?)',(name,password))
        x=cursor.execute("select * from users ")
        print(x.fetchall())
        conn2.commit()
    except Exception as e:
        print(e)
        msg= 'failure'
        n=404
    else :
        msg= 'success'
        n=200
    finally:
        conn2.close()
    return msg,n





@app.teardown_appcontext
@app.route('/forGet')
def forGet():

    try:
        conn3 = sqlite3.connect('flaskDB.db')
        cursor = conn3.cursor()
        cursor.execute('select * from users')
        conn3.commit()
    except Exception as e:
        print(e)
        msg= 'failure'
        n=404
    else :
        msg=cursor.fetchall()
        n=200
    finally:
        conn3.close()
    return msg,n

if __name__ == '__main__': app.run()
