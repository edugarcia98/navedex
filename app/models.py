from django.db import models

from navedex import settings

# Create your models here.
class Naver(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    birthdate = models.DateField(verbose_name="Data de Nascimento")
    admission_date = models.DateField(verbose_name="Data de Admissão")
    job_role = models.CharField(max_length=100, verbose_name = "Cargo")
    user_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='naver')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Naver")
        verbose_name_plural = ("Navers")

# colocar many to many no project
# fazer a relação many dos dois

class Project(models.Model):
    name = models.CharField(max_length=500, verbose_name="Nome")
    navers = models.ManyToManyField(Naver, verbose_name="Navers", related_name="projects", through='NaverProject')
    user_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

class NaverProject(models.Model):
    naver = models.ForeignKey(Naver, verbose_name="Naver", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.naver) + ' - ' + str(self.project)
    
    class Meta:
        verbose_name = ("Naver-Project")
        verbose_name = ("Navers-Projects")
