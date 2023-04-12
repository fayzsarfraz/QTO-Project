from django.shortcuts import render

# Create your views here.
from .models import Project

def index(request):
    # return render(request,'index.html')
    obj = Project.objects.all()
    context={
        "obj":obj
    }
    return render(request, 'home/index.html',context)
