from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.order_by('date_posted')
    context = {'posts': posts}
    return render(request, "static/index.html", context)