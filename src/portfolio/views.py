from django.shortcuts import render
from .models import Project


def projects(request):
    return render(request, 'portfolio/index.html', {'projects': Project.objects.all()})
