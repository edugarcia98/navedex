from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'confirm_password']
        extra_kwargs = {
                'password': {'write_only': True}
        }
    
    def save(self):
        user = User(
                email=self.validated_data['email'],
            )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Senhas devem ser iguais.'})
        user.set_password(password)
        user.save()
        return user