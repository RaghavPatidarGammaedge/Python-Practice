import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import django_project1.djangoDB
def get(request):
    try:
        cp=django_project1.djangoDB.ConnectionProvider()
        conn=cp.getConnection()
        cursor=conn.cursor()
        cursor.execute("select * from users")
        response=cursor.fetchall()
        return HttpResponse(response,status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse('something went wrong',status=500)

@csrf_exempt
def post(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            password = request.POST.get('password')
            print(name)
            print(password)
            cp = django_project1.djangoDB.ConnectionProvider()
            conn = cp.getConnection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
            conn.commit()
            return HttpResponse("Successfully uploaded data", status=200)
        except Exception as ex:
            return HttpResponse("Something went wrong", status=500)
    else:
        return HttpResponse("Invalid method", status=405)
        print("Exception:", ex)
@csrf_exempt
def put(request,id):
    try:
        print(id)
        updates = json.loads(request.body)
        password=updates.get('password')
        cp=django_project1.djangoDB.ConnectionProvider()
        conn=cp.getConnection()
        cursor=conn.cursor()
        cursor.execute("update users set password=%s where name=%s",(password,id))
        conn.commit()
        return HttpResponse("sucessfully data uploaded",status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse("error",status=500)


@csrf_exempt
def delete(request,id):
    try:
        print(id)
        cp=django_project1.djangoDB.ConnectionProvider()
        conn=cp.getConnection()
        cursor=conn.cursor()
        cursor.execute("delete from users where name='"+id+"'")
        conn.commit()
        return HttpResponse("sucessfully data deleted",status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse("something went wrong",status=500)
