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
    def post(self, request):
        phone = request.data.get('phone')
        role = request.data.get('role')

        # Validate required fields
        if not phone or not role:
            return Response(
                {"error": "phone and role are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Find user with matching phone + role
        try:
            user = User.objects.get(phone=phone, role=role)
        except User.DoesNotExist:
            return Response(
                {"error": "invalid phone or role"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Successful login
        return Response({
            "message": "Login successfully",
            "user": {
                "id": user.id,
                "name": user.name,
                "role": user.role
            }
        }, status=status.HTTP_200_OK)

class UserList(APIView):
    def get(self,request):
        user = User.objects.all()
        serializer= UserSerializer(user,many=True)
        return Response(serializer.data)
    

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenserializer   





     


