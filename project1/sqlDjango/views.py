from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
def sqlData(request):
    return HttpResponse("Hello, welcome to SQL page for this project")
def display(request):
    per=Person.objects.all()
    return render(request,'display.html',{'per':per})