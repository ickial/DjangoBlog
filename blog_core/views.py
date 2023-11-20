from django.shortcuts import render
from django.shortcuts import  render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.publish
    # posts =Post.objects.get(id=1)
    posts = Post.objects.filter(status='published')
    print('posts',posts)
    return render(request,'list.html', {'posts': posts})

def post_detail(request, post):
    print(request, post)
    post = get_object_or_404(Post,
                             status='published')
    print('!!!!!!!',post)
                             # publish_year=year,
                             # publish_month=month,
                             # publish_day=day)
    return render(request, 'list.html', {'post': post})
# Create your views here.
