from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('navers/', views.NaversIndex.as_view()),
    path('navers/<int:pk>/', views.NaverShow.as_view()),
    path('navers/create/', views.NaverStore.as_view()),
    path('navers/update/<int:pk>/', views.NaverUpdate.as_view()),

    path('projects/', views.ProjectsIndex.as_view()),
    path('projects/<int:pk>/', views.ProjectShow.as_view()),
    path('projects/create/', views.ProjectStore.as_view()),
    path('projects/update/<int:pk>/', views.ProjectUpdate.as_view()),
]
