from django.urls import path
from .import views

urlpatterns = [
    path('', views.projects, name="projects-project"),
    path('addProject/', views.addProject, name="projects-addProject"),
]
