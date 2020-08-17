from django.http import Http404, HttpResponse
from django.shortcuts import render

from rest_framework import generics

from .models import *
from .serializers import *

# Create your views here.

class UserList(generics.CreateAPIView):
    serializer_class = UserSerializer
