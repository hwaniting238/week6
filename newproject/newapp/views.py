from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Newapp
# Create your views here.

def home(request):
    newapps = Newapp.objects.all()
    return render(request, 'home.html', {'newapps': newapps})

def detail(request,id):
    newapp = get_object_or_404(Newapp, pk = id)
    return render(request, 'detail.html', {'newapp':newapp})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Newapp()
    new_blog.title  = request.POST['title']
    new_blog.writer  = request.POST['writer']
    new_blog.body  = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)