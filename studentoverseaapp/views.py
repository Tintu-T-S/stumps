from django.shortcuts import render
from . models import imigration, team_staff

# Create your views here.

def demo(request):
    obj = imigration.objects.all()
    dt = team_staff.objects.all()
    return render(request,"index.html",{'result':obj,'res':dt})

