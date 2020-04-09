from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    context = {
        'blog': Post.objects.all()
        
    }
    return render(request, 'mainblog.html', context)