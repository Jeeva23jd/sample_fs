from django.shortcuts import render, redirect
from .models import BlogData
from .forms import BlogForm
# Create your views here.
def home(request):
    blogdatas = BlogData.objects.all()
    context = {'object_list':blogdatas}
    return render(request,'blog_webpage.html',context)
def Create_Post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'forms.html', {'form': form})