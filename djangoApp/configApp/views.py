import json
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from configApp.models import MyUsers


class loginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=401)

class ViewUsers(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def getAllUsers(request):
        try:
            response = MyUsers.objects.all()
            return HttpResponse(response, status=200)
        except Exception as ex:
            print(ex)
            return HttpResponse('something went wrong', status=500)

class RegisterView(APIView):
    @csrf_exempt
    def post(self, request):
        if request.method == "POST":
            try:
                username = request.POST.get('username')
                password1 = request.POST.get('password')
                email = request.POST.get('email')
                print(username, password1, email)
                password=make_password(password1)

                obj = MyUsers(username=username, password=password, email=email)
                obj.save()
                return HttpResponse("Successfully uploaded data", status=200)
            except Exception as ex:
                print(ex)
                return HttpResponse("Something went wrong", status=500)
        else:
            return HttpResponse("Invalid method", status=405)
            print("Exception:", ex)

class UpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    @csrf_exempt
    def put(request, username):
        try:
            print(id)
            updates = json.loads(request.body)
            email = updates.get('email')
            user = MyUsers.objects.get(username=username)
            user.email = email
            user.save()
            return HttpResponse("sucessfully data uploaded", status=200)
        except Exception as ex:
            print(ex)
            return HttpResponse("error", status=500)

class DeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def delete(request, username):
        try:
            print(id)
            MyUsers.objects.get(username=username).delete()
            return HttpResponse("sucessfully data deleted", status=200)
        except Exception as ex:
            print(ex)
            return HttpResponse("something went wrong", status=500)





