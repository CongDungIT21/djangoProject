from django.shortcuts import render
from .models import Post 

# Create your views here.

def home(request):
    posts = Post.objects.all() 
    context = {'posts': posts}
    tmp = Post.objects.last()
    return render(request, 'web/index.html',context)