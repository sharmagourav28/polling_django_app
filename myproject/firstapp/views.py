
from django.shortcuts import render
from django.http import HttpResponse
from .models import poll

# Create your views here.

def home(request):
    return HttpResponse("Welcome to first Django app")

def index(request):
    polls = poll.objects.all()  # fetch all polls from database
    return render(request, 'index.html', {'polls': polls})
