from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def focus(request):
    return HttpResponse("<h1>Hello Everyone !</h1><p>Welcome to the platform to learn django!</p>")
def sample(request):
    return render(request,'in.html')
def sample1(request):
    return render(request,'new.html')

