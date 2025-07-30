from urllib import request

from fastapi import FastAPI
import psycopg2
from psycopg2 import connect
import fastDB


app = FastAPI()

cp= fastDB.ConnectionProvider()

@app.post('/forPut')
def forPut():
    name = request.form.get('name')
    password = request.form.get('password')

    try:
        conn=cp.getConnection()
        cursor = conn.cursor()
        cursor.execute("insert into users values ('"+name+"','"+password+"')")
        cursor.execute("select * from users ")
        print(cursor.fetchall())
        conn.commit()

    except Exception as e:
        print(e)
        msg= 'failure'
        n=404
    else :
        msg= 'success'
        n=200
    return msg,n





@app.route('/forGet')
def forGet():

    try:
        conn=cp.getConnection()
        cursor = conn.cursor()
        cursor.execute('select * from users')
        conn.commit()
    except Exception as e:
        print(e)
        msg= 'failure'
        n=404
    else :
        msg=cursor.fetchall()
        n=200
    return msg,n


@app.route('/forDelete/<name>',methods=['DELETE'])
def forDelete(name):

    try:
        conn=cp.getConnection()
        cursor = conn.cursor()
        cursor.execute('delete from users where name=%s',(name))
        conn.commit()
        msg='success'
        n=200
    except Exception as e:
        print(e)
        msg = 'failure'
        n = 404
    return msg,n

@app.route('/forUpdate/<name>',methods=['PUT'])
def forUpdate(name):
    password = request.form.get('password')
    try:
        conn=cp.getConnection()
        cursor = conn.cursor()
        cursor.execute('update users set password=%s where name=%s',(password,name))
        conn.commit()
        msg='success'
        n=200
    except Exception as e:
        print(e)
        msg = 'failure'
        n = 404


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
