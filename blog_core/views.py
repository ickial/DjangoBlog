from django.shortcuts import render
from django.shortcuts import  render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User

def post_list(request):
    my_posts = {'my_posts': Post.objects.filter(status='published')}
    return render(request,'my_posts.html',my_posts)

def post_detail(request, post):
    get_object_or_404(Post,id=post, status='published')
    my_context = {'my_post': Post.objects.get(id=post, status='published')}
    return render(request, 'detail.html', my_context)

def post_by_author(request, username_str):
    # my_user = User.objects.get(username=username_str)
    # user_posts = Post.objects.filter(author=my_user, status='published')
    user_posts = Post.objects.filter(status='published', author__username=username_str)
    return render(request, 'posts_by_author.html', {'published_posts_by_author': user_posts})

def created_data_posts(request,year_str, mouth_str):
    create_data = Post.objects.filter(status='published', created__year=year_str,created__day=mouth_str)
    return render(request, 'created_data_posts.html', {'term_created_posts': create_data})


# http://127.0.0.1:8000/posts/2003/08