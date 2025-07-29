import sqlite3
from flask import Flask,request
import psycopg2

connection_info="host=localhost dbname=db1 user=rghv password=rghv"
conn=psycopg2.connect(connection_info)
cursor=conn.cursor()

cursor.execute("create table if not exists users (name text primary key, password text)")
conn.commit()
conn.close()

app = Flask(__name__)


@app.route('/forPut',methods=['POST'])
def forPut():
    name = request.form.get('name')
    password = request.form.get('password')

    try:
        conn2 = psycopg2.connect(connection_info)
        cursor = conn2.cursor()
        cursor.execute("insert into users values ('"+name+"','"+password+"')")
        cursor.execute("select * from users ")
        print(cursor.fetchall())
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





@app.route('/forGet')
def forGet():

    try:
        conn3 = psycopg2.connect(connection_info)
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


@app.route('/forDelete/<name>',methods=['DELETE'])
def forDelete(name):
    conn4 = psycopg2.connect(connection_info)

    try:
        cursor = conn4.cursor()
        cursor.execute('delete from users where name=%s',(name))
        conn4.commit()
        msg='success'
        n=200
    except Exception as e:
        print(e)
        msg = 'failure'
        n = 404
    finally:
        conn4.close()
    return msg,n

@app.route('/forUpdate/<name>',methods=['PUT'])
def forUpdate(name):
    conn5 = psycopg2.connect(connection_info)
    password = request.form.get('password')
    try:
        cursor = conn5.cursor()
        cursor.execute('update users set password=%s where name=%s',(password,name))
        conn5.commit()
        msg='success'
        n=200
    except Exception as e:
        print(e)
        msg = 'failure'
        n = 404
    finally:
        conn5.close()

    return msg,n

@app.route('/forPatch/<name>',methods=['PATCH'])
def forPatch(name):
    conn6 = psycopg2.connect(connection_info)
    password = request.form.get('password')
    try:
        cursor = conn6.cursor()
        cursor.execute('update users set password=%s where name=%s',(password,name))
        conn6.commit()
        msg='success'
        n=200
    except Exception as e:
        print(e)
        msg = 'failure'
        n = 404
    finally:
        conn6.close()

    return msg,n





if __name__ == '__main__': app.run()
