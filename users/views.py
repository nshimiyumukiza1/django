from django.shortcuts import render
from.models import User
from.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.views import TokenObtainPairView
from.serializers import CustomTokenserializer




class RegisterView (APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Created SUssefuly!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
    
class LoginVeiw(APIView):
    def post(self,request):
        phone = request.data.get('phone')
        password = request.data.get('password')

        #find user by phone
        try:
            user = User.objects.get(phone = phone)
        except User.DoesNotExist:
            return Response({"error":"invald phone or password"},status=status.HTTP_400_BAD_REQUEST)
        # verfy password
        if check_password(password,user.password):
            return Response({
                "message":"Login Successfuly",
                "user":{
                    "id":user.id,
                    "name":user.name,
                    "role":user.role
                }
            })
        return Response({"error":"Invalid phone  or password"},status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    def get(self,request):
        user = User.objects.all()
        serializer= UserSerializer(user,many=True)
        return Response(serializer.data)
    

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenserializer   





     


