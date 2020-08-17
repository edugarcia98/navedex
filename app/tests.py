from django.test import TestCase

from .models import *
from .serializers import *

from userauth.tests import registerUser

from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

def userLoginAuthorization(self):
    response = registerUser(self)

    data = {
            "email": "user@test.com",
            "password": "user_pwd"
        }

    response = self.client.post('/auth/login/', data)
    #headers = {'Authorization': 'Bearer ' + response.data['access']}
    return response.data['access']

def createNaver(self, projectCreated):
    projects = [getProjectCreatedId(self)] if projectCreated else []

    data = {
        "name": "New Naver",
        "birthdate": "1999-05-15",
        "admission_date": "2020-06-12",
        "job_role": "Desenvolvedor",
        "projects": projects
    }

    response = self.client.post('/api/navers/create/', data)
    return response

def getNaverCreatedId(self):
    response = self.client.get('/api/navers/')
    return response.data[0]['id']

def createProject(self, naverCreated):
    navers = [getNaverCreatedId(self)] if naverCreated else []

    data = {
        "name": "New Project",
        "navers": navers
    }

    response = self.client.post('/api/projects/create/', data)
    return response

def getProjectCreatedId(self):
    response = self.client.get('/api/projects/')
    return response.data[0]['id']


class NaverTestCases(APITestCase):

    def test_naver_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))

        #Criação correta
        responseProject = createProject(self, False)
        responseRight = createNaver(self, True)

        #Criação errada
        data = {
            "name": "",
            "birthdate": "1999-05-15",
            "admission_date": "2020-06-12",
            "job_role": "",
            "projects": []
        }
        responseWrong = self.client.post('/api/navers/create/', data)

        self.assertEqual(responseRight.status_code, status.HTTP_201_CREATED)
        self.assertEqual(responseWrong.status_code, status.HTTP_400_BAD_REQUEST)

    def test_naver_index(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))
        
        response = createNaver(self, False)

        response = self.client.get('/api/navers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Naver.objects.count(), 1)
    
    def test_naver_show(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))

        response = createNaver(self, False)
        response = self.client.get('/api/navers/' + str(getNaverCreatedId(self)) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_naver_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))

        responseNaver = createNaver(self, False)

        data = {
            "name": "New Naver - upd",
            "birthdate": "1999-05-15",
            "admission_date": "2020-06-12",
            "job_role": "Desenvolvedor - upd",
            "projects": []
        }
        
        response = self.client.put('/api/navers/update/' + str(getNaverCreatedId(self)) + '/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_naver_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))
        responseNaver = createNaver(self, False)

        response = self.client.delete('/api/navers/' + str(getNaverCreatedId(self)) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProjectTestCases(APITestCase):

    def test_project_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))

        #Criação correta
        responseRight = createNaver(self, False)

        #Criação errada
        data = {
            "name": "",
            "navers": []
        }

        responseWrong = self.client.post('/api/projects/create/', data)

        self.assertEqual(responseRight.status_code, status.HTTP_201_CREATED)
        self.assertEqual(responseWrong.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_project_index(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))
        
        response = createProject(self, False)

        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.count(), 1)
    
    def test_project_show(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))

        response = createProject(self, False)
        response = self.client.get('/api/projects/' + str(getProjectCreatedId(self)) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_project_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))

        responseProject = createProject(self, False)

        data = {
            "name": "New Project - upd",
            "navers": []
        }
        
        response = self.client.put('/api/projects/update/' + str(getProjectCreatedId(self)) + '/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + userLoginAuthorization(self))
        responseProject = createProject(self, False)

        response = self.client.delete('/api/projects/' + str(getProjectCreatedId(self)) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)