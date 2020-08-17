from rest_framework import serializers
from rest_framework.response import Response

from userauth.models import *
from userauth.serializers import *

from .models import *

class NaverIndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role']

class ProjectIndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name']

class NaverShowSerializer(serializers.ModelSerializer):
    projects = ProjectIndexSerializer(many=True, read_only=True)

    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'projects']

class NaverStoreSerializer(serializers.ModelSerializer):

    projects = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), many=True)

    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'projects']
    
    def save(self):
        user = self.context['request'].user
        naver = Naver(
                name=self.validated_data['name'],
                birthdate=self.validated_data['birthdate'],
                admission_date=self.validated_data['admission_date'],
                job_role=self.validated_data['job_role'],
                user_creator=user
            )
        
        projects = self.validated_data['projects']

        check = all(item in Project.objects.filter(user_creator=user) for item in projects)
        if not check:
            raise serializers.ValidationError({'projects': 'Os projetos devem pertencer aos criados pelo usuário.'})
        
        naver.save()

        for project in projects:
            naver.projects.add(project)
        
        return naver

class NaverUpdateSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), many=True)

    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'projects']

class ProjectShowSerializer(serializers.ModelSerializer):
    navers = NaverIndexSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'navers']

class ProjectStoreSerializer(serializers.ModelSerializer):

    navers = serializers.PrimaryKeyRelatedField(
        queryset=Naver.objects.all(), many=True
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'navers']
    
    def save(self):
        user = self.context['request'].user
        project = Project(
                name=self.validated_data['name'],
                user_creator=user
            )
        
        navers = self.validated_data['navers']

        check = all(item in Naver.objects.filter(user_creator=user) for item in navers)
        if not check:
            raise serializers.ValidationError({'navers': 'Os navers devem pertencer aos criados pelo usuário.'})
        
        project.save()

        for naver in navers:
            project.navers.add(naver)

        return project

class ProjectUpdateSerializer(serializers.ModelSerializer):

    navers = serializers.PrimaryKeyRelatedField(
        queryset=Naver.objects.all(), many=True
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'navers']
