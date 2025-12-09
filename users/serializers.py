from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'role', 'phone', 'password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

class CustomTokenserializer(TokenObtainPairSerializer):
    def get_token(cols,user):
        token = super.get_token(user)
        token['name'] = user.name
        token['role'] = user.role
        return token
    


