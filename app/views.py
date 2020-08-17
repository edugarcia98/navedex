from django.http import Http404, HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.

# NAVER
#==================================================================================================================================

class NaversIndex(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = NaverIndexSerializer

    def get_queryset(self):
        return Naver.objects.filter(user_creator=self.request.user)
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'admission_date', 'job_role']

class NaverStore(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = NaverStoreSerializer

    def get_queryset(self):
        return Naver.objects.filter(user_creator=self.request.user)

class NaverUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Naver.objects.filter(user_creator=self.request.user)

    def put(self, request, pk):
        naver = self.get_object()

        try:
            projects = request.data['projects']
            check = all(item in Project.objects.filter(user_creator=request.user).values_list('id', flat=True) for item in projects)

            if not check:
                return Response({'projects': 'Os projetos devem pertencer aos criados pelo usuário.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        serializer = NaverUpdateSerializer(naver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NaverShow(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = NaverShowSerializer

    def get_queryset(self):
        return Naver.objects.filter(user_creator=self.request.user)

# NAVER
#==================================================================================================================================

class ProjectsIndex(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = ProjectIndexSerializer

    def get_queryset(self):
        return Project.objects.filter(user_creator=self.request.user)
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class ProjectStore(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = ProjectStoreSerializer

    def get_queryset(self):
        return Project.objects.filter(user_creator=self.request.user)

class ProjectUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Project.objects.filter(user_creator=self.request.user)
    
    def put(self, request, pk):
        project = self.get_object()

        try:
            navers = request.data['navers']
            check = all(item in Naver.objects.filter(user_creator=request.user).values_list('id', flat=True) for item in navers)

            if not check:
                return Response({'navers': 'Os navers devem pertencer aos criados pelo usuário.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        serializer = ProjectUpdateSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectShow(generics.RetrieveUpdateDestroyAPIView):
    permission_classe = (IsAuthenticated, )

    serializer_class = ProjectShowSerializer

    def get_queryset(self):
        return Project.objects.filter(user_creator=self.request.user)
