import json

from .models import User
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

def registerUser(self):
    data = {
            "email": "user@test.com",
            "password": "user_pwd",
            "confirm_password": "user_pwd"
        }

    response = self.client.post('/auth/users/', data)
    return response

class RegistrationTestCase(APITestCase):

    def test_user_registration(self):

        #Registro correto
        responseRight = registerUser(self)

        #Registro errado
        data = {
            "email": "user2@test.com",
            "password": "user_pwd",
            "confirm_password": "user_pwd_dif"
        }

        responseWrong = self.client.post('/auth/users/', data)

        self.assertEqual(responseRight.status_code, status.HTTP_201_CREATED)
        self.assertEqual(responseWrong.status_code, status.HTTP_400_BAD_REQUEST)

class LoginTestCase(APITestCase):

    def test_user_right_login(self):
        response = registerUser(self)
        
        data = {
            "email": "user@test.com",
            "password": "user_pwd"
        }

        response = self.client.post('/auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_wrong_login(self):
        data = {
            "email": "wronguser@test.com",
            "password": "user_wrong_pwd"
        }

        response = self.client.post('/auth/login/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)