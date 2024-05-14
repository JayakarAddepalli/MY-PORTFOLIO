from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def Home(request):

    skills = SkillsModel.objects.all()
    projects = Projects.objects.all()

    if request.method == 'POST':
        f = UserForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
            messages.info(request, 'Message has been sent successfully')
        else:
            messages.error(request, 'Invalid Name or Email or Message')

        f = UserForm()

    return render(request,'Home.html', {'skills':skills,'projects':projects})