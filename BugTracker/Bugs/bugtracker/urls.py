from django.urls import path
from .import views


urlpatterns = [
    path('<int:project_id>/', views.home, name="bugtracker-home"),
    path('about/', views.about, name="bugtracker-about"),
    path('addBug/', views.addBug, name="bugtracker-addBug"),
    path('delBug/<int:bug_id>/', views.delBug, name="bugtracker-delBug"),
]
