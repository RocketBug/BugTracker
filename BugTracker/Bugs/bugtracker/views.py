from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import BugItem
from projects.models import ProjectItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def home(request, project_id):

    post_project_id = ProjectItem.objects.all().get(id = project_id)
    all_bugs = BugItem.objects.all().filter(project = post_project_id)
    request.session['session_project_id'] = project_id

    #all_bugs = BugItem.objects.all().order_by('-content_time')
    return render(request, 'bugtracker/home.html', {'all_bugs':all_bugs})

def addBug(request):
    c = request.POST['content']
    bug_level = request.POST['bug_levels']
    bug_description = request.POST['bug_description']
    bug_title = request.POST['bug_title']    
    
    session_project_id = None
    if 'session_project_id' in request.session:
        session_project_id = request.session['session_project_id']
    
    proj = ProjectItem.objects.all().get(id = session_project_id) 
    current_user = request.user
    new_item = BugItem(content = c, content_type = bug_level, content_description = bug_description, content_title = bug_title, author = current_user, project = proj)
    new_item.save()
    return redirect('/home/%d'%session_project_id)

def delBug(request, bug_id):
    del_item = BugItem.objects.get(id = bug_id)
    del_item.delete()
    session_project_id = None
    if 'session_project_id' in request.session:
        session_project_id = request.session['session_project_id']
    
    return redirect('/home/%d'%session_project_id)


def about(request):
    return render(request, 'bugtracker/about.html')
