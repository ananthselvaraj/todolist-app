from django.shortcuts import render,redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('index')
    return render(request,'index.html',{'tasks':tasks})
