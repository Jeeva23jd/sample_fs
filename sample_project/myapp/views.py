from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def httphome(request):
    return HttpResponse("<h1>Welcome to Django!</h1>")
def display(request):
    return render(request, 'index.html')

