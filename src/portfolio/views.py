from django.shortcuts import render
from .models import Project


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})
