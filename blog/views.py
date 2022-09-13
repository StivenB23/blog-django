from django.shortcuts import render, get_list_or_404
from .models import Post
# Create your views here.
def showPost(request):
    posts=Post.objects.all()
    return render(request, 'posts.html',{'posts':posts})

def showPostById(request, post_id):
    post=get_list_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'posts':post})

