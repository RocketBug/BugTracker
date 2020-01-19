from django.shortcuts import render, redirect
from .models import ProjectItem

def projects(request):
    all_projects = ProjectItem.objects.all()
    return render(request, 'projects/project.html', {'all_projects':all_projects})

def addProject(request):
    project_title = request.POST['project_title']
    project_description = request.POST['project_description']
    current_user = request.user
    new_item = ProjectItem(project_title = project_title, project_description = project_description, author = current_user)
    new_item.save()
    return redirect('projects-project')